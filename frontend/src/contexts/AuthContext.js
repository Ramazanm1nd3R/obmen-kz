import React, { createContext, useState, useEffect } from "react";
import apiClient from "../api/api";

export const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);

  useEffect(() => {
    const token = localStorage.getItem("accessToken");
    if (token) {
      apiClient
        .get("/users/me/")
        .then((response) => setUser(response.data))
        .catch(() => {
          localStorage.removeItem("accessToken");
          setUser(null);
        });
    }
  }, []);

  const login = (userData, token) => {
    localStorage.setItem("accessToken", token);
    setUser(userData);
  };

  const logout = () => {
    localStorage.removeItem("accessToken");
    setUser(null);
  };

  return (
    <AuthContext.Provider value={{ user, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};
