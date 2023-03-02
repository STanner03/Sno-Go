import React, { useState, useContext, useEffect } from "react";
import AuthContext from "../../context/AuthContext";
import useCustomForm from "../../hooks/useCustomForm";

const RegisterPage = () => {
  const [password1, setPassword1] = useState("");
  const [email1, setEmail1] = useState("");
  const [show, setShow] = useState(false);
  const { registerUser } = useContext(AuthContext);
  let counter = 0
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
      counter+=1
      console.log("Counter:", counter)
    } else {
      setShow(false);
      counter-=1
      console.log("Counter:", counter)
    }
  }, [password1, formData.password, email1, formData.email])
  const validatePassword1 = (e) => {
    e.preventDefault()
    setPassword1(e.target.value) 
  };
  const validateEmail = (e) => {
    e.preventDefault()
    setEmail1(e.target.value)
  }
  console.log("formData:", formData);
  console.log("password1:", password1);
  console.log("formData.password:", formData.password);

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
        <p style={{ fontSize: "12px" }}>
          NOTE: Make this an uncommon password with characters, numbers, and
          special characters!
        </p>
        {show ? <button>Register!</button> : <p>Check Credentials so they match!!!</p>}
      </form>
    </div>
  );
};

export default RegisterPage;
