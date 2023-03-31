// General Imports
import React from "react";
import { useNavigate, Link } from "react-router-dom";
import { useEffect, useState } from "react";
import useAuth from "../../hooks/useAuth";
import axios from "axios";

// Page Imports

const ProviderPage = () => {
      // State Functions
  const [user, token] = useAuth();
console.log("User", user)
  return (
    <>
      <div className="container">
        <h3>Snow Remover</h3>
        <Link to="/clientpage">Switch to Client</Link>
        <h1>
            Home Page for {user.first_name} {user.name}!
        </h1>
      </div>
    </>
  );
};

export default ProviderPage;
