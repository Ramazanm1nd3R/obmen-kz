import React from "react";
import defaultAvatar from "../assets/default-avatar.png";

const Avatar = ({ src, alt = "User Avatar", size = 50 }) => {
  const handleImageError = (event) => {
    event.target.src = defaultAvatar; // Если аватарка не загрузилась, ставим базовое изображение
  };

  return (
    <img
      src={src || defaultAvatar}
      alt={alt}
      onError={handleImageError}
      style={{
        width: size,
        height: size,
        objectFit: "cover",
        borderRadius: "50%",
      }}
    />
  );
};

export default Avatar;
