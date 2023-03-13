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
  const [activeClient, setActiveClient] = useState();

  useEffect(() => {
    const fetchClients = async () => {
      try {
        let response = await axios.get("http://127.0.0.1:8000/api/clients/", {
          headers: {
            Authorization: "Bearer " + token,
          },
        });
        setClients(response.data);
        console.log("ASYNC Clients: ", response.data[0])
      } catch (error) {
        console.log(error);
      }
    };
    fetchClients();
  }, []);

  useEffect(() => {
    const makeClientActive = () => {
      try {
        if (clients.length == 1) {
          setActiveClient(clients[0]);
        }
        console.log("Active Client: ", activeClient)
      } catch (error) {
        console.log("Active Client ERROR: ", error);
      }
    };
    makeClientActive();
  }, [token, clients]);

  useEffect(() => {
    const fetchJobs = async () => {
      try {
        let response = await axios.get(
          `http://127.0.0.1:8000/api/clients/${activeClient.id}/jobs/`,
          {
            headers: {
              Authorization: "Bearer " + token,
            },
          }
        );
        setJobs(response.data);
        console.log("ASYNC Jobs: ", response.data);
      } catch (error) {
        console.log(error);
      }
    };
    fetchJobs();
    // console.log("Active Client:", activeClient);
    // console.log("Client Id:", activeClient.id);
    // console.log("Client First Name:", activeClient.first_name);
  }, [token, activeClient]);

  console.log("Clients:", clients);
  return (
    <div>
      {activeClient && (
        <div className="container">
          <h1>Home Page for {activeClient.first_name}!</h1>
          {jobs &&
            jobs.map((job, i) => (
              <p key={job.id}>
                {(i += 1)} {job.address} {job.total_price} {job.paid}
              </p>
            ))}
        </div>
      )}
    </div>
  );
};

export default HomePage;
