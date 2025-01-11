import React, { useEffect, useState } from "react";
import apiClient from "../api/api";
import { Link } from "react-router-dom";
import "../styles/HomePage.css"; // Стили для блока объявлений
import defaultImage from "../assets/default-image.png"; // Импорт базового изображения

const HomePage = () => {
  const [carts, setCarts] = useState([]);
  const [error, setError] = useState(false);

  useEffect(() => {
    apiClient
      .get("/carts/")
      .then((response) => setCarts(response.data))
      .catch((err) => {
        console.error("Error fetching carts:", err);
        setError(true);
      });
  }, []);

  const handleImageError = (event) => {
    event.target.src = defaultImage;
  };

  if (error) {
    return <p>Ошибка при загрузке данных. Попробуйте позже.</p>;
  }

  return (
    <div className="homepage-container">
      <h1>Объявления</h1>
      {carts.length > 0 ? (
        <div className="cart-list">
          {carts.map((cart) => (
            <div key={cart.id} className="cart-item">
              {/* Ссылка на карточку товара через изображение */}
              <Link to={`/cart/${cart.id}`}>
                <img
                  src={cart.image || defaultImage}
                  alt={cart.title}
                  onError={handleImageError}
                  className="cart-image"
                />
              </Link>
              <div>
                {/* Ссылка на карточку товара через название */}
                <Link to={`/cart/${cart.id}`}>
                  <strong>{cart.title}</strong>
                </Link>
                <p>{Number(cart.price).toLocaleString()} KZT</p>
              </div>
            </div>
          ))}
        </div>
      ) : (
        <p>Пока нет объявлений.</p>
      )}
    </div>
  );
};

export default HomePage;
