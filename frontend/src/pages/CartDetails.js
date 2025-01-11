import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import apiClient from "../api/api";
import "../styles/CartDetails.css";

const CartDetails = () => {
  const { id } = useParams();
  const [cart, setCart] = useState(null);
  const [seller, setSeller] = useState(null);

  useEffect(() => {
    // Получение данных о товаре
    apiClient
      .get(`/carts/${id}/`)
      .then((response) => {
        setCart(response.data);

        // Запрос информации о продавце
        return apiClient.get(`/users/${response.data.user}/`);
      })
      .then((response) => setSeller(response.data))
      .catch((error) => console.error("Error fetching data:", error));
  }, [id]);

  if (!cart || !seller) {
    return <p>Loading...</p>;
  }

  return (
    <div className="cart-details-container">
      <div className="cart-image">
        <img
          src="https://via.placeholder.com/600x400.png?text=No+Image"
          alt={cart.title}
        />
      </div>
      <div className="cart-info">
        <h1>{cart.title}</h1>
        <p className="cart-price">{Number(cart.price).toLocaleString()} KZT</p>
        <p className="cart-description">{cart.description}</p>
        <button
          className="contact-seller-button"
          onClick={() => alert(`Написать продавцу: ${seller.username}`)}
        >
          Написать продавцу
        </button>
        <div className="seller-info">
          <p>
            Продавец: <strong>{seller.username}</strong>
          </p>
          <p>Рейтинг: {seller.average_rating.toFixed(1)} / 5</p>
        </div>
      </div>
    </div>
  );
};

export default CartDetails;
