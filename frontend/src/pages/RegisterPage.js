import React, { useState } from "react";
import apiClient from "../api/api";
import { useNavigate } from "react-router-dom";
import "../styles/RegisterPage.css";

const RegisterPage = () => {
  const [formData, setFormData] = useState({ username: "", email: "", password: "", password_confirm: "" });
  const [error, setError] = useState(null);
  const navigate = useNavigate();

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    apiClient
      .post("/users/register/", formData)
      .then(() => navigate("/login"))
      .catch(() => setError("Ошибка при регистрации."));
  };

  return (
    <div className="register-page">
      <h2>Регистрация</h2>
      {error && <p className="error-message">{error}</p>}
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="username"
          placeholder="Имя пользователя"
          onChange={handleChange}
          required
        />
        <input type="email" name="email" placeholder="Email" onChange={handleChange} required />
        <input type="password" name="password" placeholder="Пароль" onChange={handleChange} required />
        <input
          type="password"
          name="password_confirm"
          placeholder="Подтверждение пароля"
          onChange={handleChange}
          required
        />
        <button type="submit">Зарегистрироваться</button>
      </form>
    </div>
  );
};

export default RegisterPage;
