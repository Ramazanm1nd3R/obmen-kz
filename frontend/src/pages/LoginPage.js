import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "../api/api";
import { toast } from "react-toastify";

const LoginPage = () => {
  const [formData, setFormData] = useState({ email: "", password: "" });
  const navigate = useNavigate();

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post("/users/auth/token/", formData);
      localStorage.setItem("accessToken", response.data.access);
      localStorage.setItem("refreshToken", response.data.refresh);
      toast.success("Успешный вход!");
      navigate("/");
    } catch (error) {
      toast.error("Ошибка входа. Проверьте данные.");
    }
  };

  return (
    <div>
      <h1>Вход</h1>
      <form onSubmit={handleSubmit}>
        <label>Email:</label>
        <input
          type="email"
          name="email"
          value={formData.email}
          onChange={handleChange}
          required
        />
        <label>Пароль:</label>
        <input
          type="password"
          name="password"
          value={formData.password}
          onChange={handleChange}
          required
        />
        <button type="submit">Войти</button>
      </form>
    </div>
  );
};

export default LoginPage;
