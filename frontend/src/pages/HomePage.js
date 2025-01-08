import React, { useEffect, useState } from "react";
import apiClient from "../api/api";
import { Link } from "react-router-dom";

const HomePage = () => {
  const [carts, setCarts] = useState([]);

  useEffect(() => {
    apiClient.get("/carts/")
      .then((response) => setCarts(response.data))
      .catch((error) => console.error("Error fetching carts:", error));
  }, []);

  return (
    <div>
      <h1>Объявления</h1>
      <ul>
        {carts.map((cart) => (
          <li key={cart.id}>
            <Link to={`/cart/${cart.id}`}>
              {cart.title} - {cart.price} KZT
            </Link>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default HomePage;
