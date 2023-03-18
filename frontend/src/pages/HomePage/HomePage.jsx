import React from "react";
import { useNavigate } from "react-router-dom";
import { useEffect, useState } from "react";
import useAuth from "../../hooks/useAuth";

const HomePage = () => {
  // The "user" value from this Hook contains the decoded logged in user information (username, first name, id)
  // The "token" value is the JWT token that you will send in the header of any request requiring authentication
  //TODO: Add an AddCars Page to add a car for a logged in user's garage

// Hooks
  const [user, token] = useAuth();
  const [userType, setUserType] = useState("");
  const navigate = useNavigate();

// Functions
  const selectClientView = () => {
    setUserType("Client");
    navigate("/clientpage")
  };

  const selectProviderView = () => {
    setUserType("Provider");
    navigate("/providerpage")
  };

  return (
    <div>
      {!userType && (
        <div>
          <h1>Are you a Client or a Provider?</h1>
          <button onClick={selectClientView}>Client</button>
          <button onClick={selectProviderView}>Provider</button>
        </div>
      )}
    </div>
  );
};

export default HomePage;
