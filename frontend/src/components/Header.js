import React from "react";
import { Link } from "react-router-dom";

const Header = () => {
  return (
    <header>
      <nav>
        <Link to="/">Главная</Link>
        <Link to="/login">Вход</Link>
        <Link to="/register">Регистрация</Link>
      </nav>
    </header>
  );
};

export default Header;
