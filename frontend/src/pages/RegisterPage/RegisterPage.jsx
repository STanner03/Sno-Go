import React, { useState, useContext, useEffect } from "react";
import AuthContext from "../../context/AuthContext";
import useCustomForm from "../../hooks/useCustomForm";

const RegisterPage = () => {
  const [password1, setPassword1] = useState("");
  const [email1, setEmail1] = useState("");
  const [show, setShow] = useState(false);
  const { registerUser } = useContext(AuthContext);
  const defaultValues = {
    username: "",
    email: "",
    password: "",
    firstName: "",
    lastName: "",
  };
  const [formData, handleInputChange, handleSubmit] = useCustomForm(
    defaultValues,
    registerUser
  );
  useEffect(() => {
    if (password1 === formData.password && email1 === formData.email) {
      setShow(true);
    } else {
      setShow(false);
    }
  }, [password1, formData.password, email1, formData.email]);
  const validatePassword1 = (e) => {
    e.preventDefault();
    setPassword1(e.target.value);
  };
  const validateEmail = (e) => {
    e.preventDefault();
    setEmail1(e.target.value);
  };

  return (
    <div className="container">
      <form className="form" onSubmit={handleSubmit}>
        <label>
          Username:{" "}
          <input
            type="text"
            name="username"
            value={formData.username}
            onChange={handleInputChange}
          />
        </label>
        <label>
          First Name:{" "}
          <input
            type="text"
            name="firstName"
            value={formData.firstName}
            onChange={handleInputChange}
          />
        </label>
        <label>
          Last Name:{" "}
          <input
            type="text"
            name="lastName"
            value={formData.lastName}
            onChange={handleInputChange}
          />
        </label>
        <label>
          Email:{" "}
          <input
            type="text"
            name="email"
            value={formData.email}
            onChange={handleInputChange}
          />
        </label>
        <label>
          Re-Type Email: {formData.email}
          <input
            type="text"
            name="email"
            value={email1}
            onChange={validateEmail}
          />
        </label>
        <label>
          Password:{" "}
          <input
            type="text"
            name="password"
            value={formData.password}
            onChange={handleInputChange}
          />
        </label>
        <label>
          Re-Type Password:{" "}
          <input
            type="text"
            name="password"
            value={password1}
            onChange={validatePassword1}
          />
        </label>
        <p>NOTE:</p>
        <p style={{ fontSize: "12px" }}>
          Make this an uncommon password with letters, numbers, and special
          characters!
        </p>
        {show ? (
          <button>Register!</button>
        ) : (
          <p>Check Credentials so they match!!!</p>
        )}
      </form>
    </div>
  );
};

export default RegisterPage;
