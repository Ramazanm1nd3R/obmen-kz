import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import apiClient from "../api/api";

const CartDetails = () => {
  const { id } = useParams();
  const [cart, setCart] = useState(null);

  useEffect(() => {
    apiClient.get(`/carts/${id}/`)
      .then((response) => setCart(response.data))
      .catch((error) => console.error("Error fetching cart details:", error));
  }, [id]);

  if (!cart) {
    return <p>Loading...</p>;
  }

  return (
    <div>
      <h1>{cart.title}</h1>
      <p>{cart.description}</p>
      <p>Price: {cart.price} KZT</p>
    </div>
  );
};

export default CartDetails;
