import React from "react";
import Header from "./Header";

const Layout = ({ children }) => {
  return (
    <>
      <Header />
      <main style={{ padding: "20px", minHeight: "calc(100vh - 60px)" }}>
        {children}
      </main>
    </>
  );
};

export default Layout;
