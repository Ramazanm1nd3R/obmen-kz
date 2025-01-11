import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import apiClient from "../api/api";
import "../styles/SellerPage.css";

const SellerPage = () => {
  const { id } = useParams(); // ID продавца
  const [seller, setSeller] = useState(null);
  const [carts, setCarts] = useState([]);
  const [error, setError] = useState(false);

  useEffect(() => {
    // Загружаем данные о продавце
    apiClient
      .get(`/users/${id}/`)
      .then((response) => setSeller(response.data))
      .catch((err) => {
        console.error("Error fetching seller:", err);
        setError(true);
      });

    // Загружаем объявления продавца
    apiClient
      .get(`/carts/`)
      .then((response) =>
        setCarts(response.data.filter((cart) => cart.user === parseInt(id)))
      )
      .catch((err) => {
        console.error("Error fetching seller's carts:", err);
        setError(true);
      });
  }, [id]);

  if (error) {
    return <p>Ошибка при загрузке данных. Попробуйте позже.</p>;
  }

  if (!seller) {
    return <p>Загрузка информации о продавце...</p>;
  }

  return (
    <div className="seller-page">
      <div className="seller-info">
        <img
          src="https://via.placeholder.com/150"
          alt={seller.username}
          className="seller-avatar"
        />
        <h1>{seller.username}</h1>
        <p>Рейтинг: {seller.average_rating?.toFixed(1) || "Нет рейтинга"} / 5</p>
      </div>

      <div className="seller-carts">
        <h2>Объявления продавца</h2>
        <ul>
          {carts.length > 0 ? (
            carts.map((cart) => (
              <li key={cart.id} className="cart-item">
                <a href={`/cart/${cart.id}`}>
                  <strong>{cart.title}</strong> -{" "}
                  {Number(cart.price).toLocaleString()} KZT
                </a>
              </li>
            ))
          ) : (
            <p>У продавца пока нет объявлений.</p>
          )}
        </ul>
      </div>
    </div>
  );
};

export default SellerPage;
