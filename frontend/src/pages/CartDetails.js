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
      <div className="cart-info">
        <img
          src={cart.image || defaultImage}
          alt={cart.title}
          onError={handleImageError}
          className="cart-image"
        />
        <h1>{cart.title}</h1>
        <p>{cart.description}</p>
        <p>Цена: {Number(cart.price).toLocaleString()} KZT</p>
        <div className="seller-info">
          <img
            src={seller.avatar || defaultAvatar}
            alt={seller.username}
            onError={handleAvatarError}
            className="seller-avatar"
          />
          <p>
            Продавец:{" "}
            <Link to={`/seller/${seller.id}`} className="seller-link">
              {seller.username}
            </Link>
          </p>
          <p>Рейтинг продавца: {seller.average_rating?.toFixed(1) || "Нет рейтинга"} / 5</p>
        </div>
        <button
          className="contact-seller-button"
          onClick={() => alert(`Написать продавцу: ${seller.username}`)}
        >
          Написать продавцу
        </button>
      </div>
    </div>
  );
};

export default CartDetails;
