import React, { useEffect, useState } from "react";
import { useParams, Link } from "react-router-dom";
import apiClient from "../api/api";
import "../styles/SellerPage.css";
import defaultAvatar from "../assets/default-avatar.png";
import defaultImage from "../assets/default-image.png";

const SellerPage = () => {
  const { id } = useParams();
  const [seller, setSeller] = useState(null);
  const [carts, setCarts] = useState([]);
  const [error, setError] = useState(false);

  useEffect(() => {
    apiClient
      .get(`/users/${id}/`)
      .then((response) => setSeller(response.data))
      .catch((err) => {
        console.error("Error fetching seller:", err);
        setError(true);
      });

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

  const handleImageError = (event) => {
    event.target.src = defaultImage;
  };

  const handleAvatarError = (event) => {
    event.target.src = defaultAvatar;
  };

  return (
    <div className="seller-page">
      <div className="seller-info">
        <img
          src={seller.avatar || defaultAvatar}
          alt={seller.username}
          onError={handleAvatarError}
          className="seller-avatar-large"
        />
        <h1>{seller.username}</h1>
        <p>Рейтинг: {seller.average_rating?.toFixed(1) || "Нет рейтинга"} / 5</p>
      </div>

      <div className="seller-carts">
        <h2>Объявления продавца</h2>
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
          <p>У продавца пока нет объявлений.</p>
        )}
      </div>
    </div>
  );
};

export default SellerPage;
