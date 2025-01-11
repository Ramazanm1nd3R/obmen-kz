import axios from "axios";

const apiClient = axios.create({
  baseURL: "/api/v1",
  headers: {
    "Content-Type": "application/json",
  },
});

// Добавляем токен в заголовок (если он есть)
apiClient.interceptors.request.use((config) => {
  const token = localStorage.getItem("accessToken");
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// Обновление токена при 401 ошибке
apiClient.interceptors.response.use(
  (response) => response,
  async (error) => {
    const originalRequest = error.config;
    if (error.response && error.response.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true;
      const refreshToken = localStorage.getItem("refreshToken");
      if (refreshToken) {
        try {
          const response = await axios.post("/api/v1/users/auth/token/refresh/", {
            refresh: refreshToken,
          });
          localStorage.setItem("accessToken", response.data.access);
          originalRequest.headers.Authorization = `Bearer ${response.data.access}`;
          return apiClient(originalRequest); // Повторяем запрос с обновлённым токеном
        } catch (refreshError) {
          console.error("Ошибка обновления токена:", refreshError);
          localStorage.removeItem("accessToken");
          localStorage.removeItem("refreshToken");
          window.location.href = "/login"; // Перенаправляем на страницу логина
        }
      } else {
        console.warn("Отсутствует refresh токен. Переход на страницу входа.");
        window.location.href = "/login"; // Перенаправляем на страницу логина
      }
    }
    return Promise.reject(error);
  }
);

export default apiClient;
