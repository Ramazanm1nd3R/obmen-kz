import React, { useEffect, useState } from "react";
import apiClient from "../api/api";
import { Link } from "react-router-dom";
import "../styles/HomePage.css"; // Стили для блока объявлений

const HomePage = () => {
  const [carts, setCarts] = useState([]);

  useEffect(() => {
    apiClient
      .get("/carts/")
      .then((response) => setCarts(response.data))
      .catch((error) => console.error("Error fetching carts:", error));
  }, []);

  return (
    <div className="homepage-container">
      <h1>Объявления</h1>
      <div className="cart-grid">
        {carts.map((cart) => (
          <div className="cart-card" key={cart.id}>
            {/* Место для изображения */}
            <div className="cart-image">
              {/* Пока изображений нет, можно оставить заглушку */}
              <img
                src="https://via.placeholder.com/300x200.png?text=No+Image"
                alt={cart.title}
              />
            </div>
            {/* Название объявления */}
            <h3 className="cart-title">
              <Link to={`/cart/${cart.id}`}>{cart.title}</Link>
            </h3>
            {/* Цена */}
            <p className="cart-price">{Number(cart.price).toLocaleString()} KZT</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default HomePage;
