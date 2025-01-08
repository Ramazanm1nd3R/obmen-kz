import React, { useEffect, useState } from "react";
import apiClient from "../api/api";
import { toast } from "react-toastify";

const ProfilePage = () => {
  const [profile, setProfile] = useState(null);

  useEffect(() => {
    apiClient
      .get("/users/me/")
      .then((response) => setProfile(response.data))
      .catch((error) => {
        console.error("Error fetching profile:", error);
        toast.error("Failed to load profile.");
      });
  }, []);

  const handleLogout = () => {
    localStorage.removeItem("accessToken");
    localStorage.removeItem("refreshToken");
    toast.success("Logged out successfully!");
    window.location.href = "/login";
  };

  if (!profile) {
    return <p>Loading...</p>;
  }

  return (
    <div>
      <h1>Welcome, {profile.username}</h1>
      <p>Email: {profile.email}</p>
      <p>Phone: {profile.phone_number}</p>
      <button onClick={handleLogout}>Logout</button>
    </div>
  );
};

export default ProfilePage;
