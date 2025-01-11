import React, { useEffect, useState } from "react";
import { useParams, Link } from "react-router-dom";
import apiClient from "../api/api";
import "../styles/CartDetails.css";
import defaultAvatar from "../assets/default-avatar.png";
import defaultImage from "../assets/default-image.png";

const CartDetails = () => {
  const { id } = useParams();
  const [cart, setCart] = useState(null);
  const [seller, setSeller] = useState(null);
  const [error, setError] = useState(false);

  useEffect(() => {
    apiClient
      .get(`/carts/${id}/`)
      .then((response) => {
        setCart(response.data);
        return apiClient.get(`/users/${response.data.user}/`);
      })
      .then((response) => setSeller(response.data))
      .catch((err) => {
        console.error("Error fetching data:", err);
        setError(true);
      });
  }, [id]);

  if (error) {
    return <p>Ошибка при загрузке данных. Попробуйте позже.</p>;
  }

  if (!cart || !seller) {
    return <p>Loading...</p>;
  }

  const handleImageError = (event) => {
    event.target.src = defaultImage;
  };

  const handleAvatarError = (event) => {
    event.target.src = defaultAvatar;
  };

  return (
    <div className="cart-details-container">
      <div className="left-block">
        <h1 className="cart-title">{cart.title}</h1>
        <img
          src={cart.image || defaultImage}
          alt={cart.title}
          onError={handleImageError}
          className="cart-image"
        />
        <h3 className="description-heading">Описание</h3>
        <p className="cart-description">{cart.description}</p>
      </div>

      <div className="right-block">
        <p className="cart-price">Цена: {Number(cart.price).toLocaleString()} KZT</p>
        <div className="seller-info">
          <img
            src={seller.avatar || defaultAvatar}
            alt={seller.username}
            onError={handleAvatarError}
            className="seller-avatar"
          />
          <p className="seller-name">
            Продавец: <Link to={`/seller/${seller.id}`}>{seller.username}</Link>
          </p>
          <p className="seller-rating">
            Рейтинг продавца: {seller.average_rating?.toFixed(1) || "Нет рейтинга"} / 5
          </p>
          <button
            className="contact-seller-button"
            onClick={() => alert(`Написать продавцу: ${seller.username}`)}
          >
            Написать продавцу
          </button>
        </div>
      </div>
    </div>
  );
};

export default CartDetails;
