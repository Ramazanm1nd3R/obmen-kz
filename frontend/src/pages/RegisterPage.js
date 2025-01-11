import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "../api/api";
import { toast } from "react-toastify";

const RegisterPage = () => {
  const [formData, setFormData] = useState({
    username: "",
    email: "",
    password: "",
    confirmPassword: "",
  });
  const navigate = useNavigate();

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (formData.password !== formData.confirmPassword) {
      toast.error("Пароли не совпадают!");
      return;
    }
    try {
      await axios.post("/users/register/", {
        username: formData.username,
        email: formData.email,
        password: formData.password,
      });
      toast.success("Регистрация успешна! Теперь войдите.");
      navigate("/login");
    } catch (error) {
      toast.error("Ошибка регистрации. Проверьте данные.");
    }
  };

  return (
    <div>
      <h1>Регистрация</h1>
      <form onSubmit={handleSubmit}>
        <label>Имя пользователя:</label>
        <input
          type="text"
          name="username"
          value={formData.username}
          onChange={handleChange}
          required
        />
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
        <label>Подтвердите пароль:</label>
        <input
          type="password"
          name="confirmPassword"
          value={formData.confirmPassword}
          onChange={handleChange}
          required
        />
        <button type="submit">Зарегистрироваться</button>
      </form>
    </div>
  );
};

export default RegisterPage;
