import React from "react";
import { useEffect, useState } from "react";
import useAuth from "../../hooks/useAuth";

import axios from "axios";

const HomePage = () => {
  // The "user" value from this Hook contains the decoded logged in user information (username, first name, id)
  // The "token" value is the JWT token that you will send in the header of any request requiring authentication
  //TODO: Add an AddCars Page to add a car for a logged in user's garage
  const [user, token] = useAuth();
  const [jobs, setJobs] = useState([]);
  const [clients, setClients] = useState([]);

  useEffect(() => {
    const fetchClients = async () => {
      try {
        let response = await axios.get("http://127.0.0.1:8000/api/clients/", {
          headers: {
            Authorization: "Bearer " + token,
          },
        });
        setClients(response.data[0]);
        // console.log("ASYNC", response.data[0])
      } catch (error) {
        console.log(error.response.data);
      }
    };
    fetchClients();
    fetchJobs();
  }, [token]);
   
  const fetchJobs = async () => {
    try {
      let response = await axios.get(`http://127.0.0.1:8000/api/clients/${clients.id}/jobs/`, {
        headers: {
          Authorization: "Bearer " + token,
        },
      });
      setJobs(response.data);
      console.log("ASYNC:", response.data)
    } catch (error) {
      console.log(error.response.data);
    }
  };

  console.log("Client:", clients)
  console.log("Client Id:", clients.id)
  console.log("Client First Name:", clients.first_name)
  return (
    <div className="container">
      <h1>Home Page for {clients.first_name}!</h1>
      {jobs &&
        jobs.map((job, i) => (
          <p key={job.id}>
            {i+=1} {job.address} {job.total_price} {job.paid}
          </p>
        ))}
    </div>
  );
};

export default HomePage;
