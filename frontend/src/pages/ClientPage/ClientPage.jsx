// General Imports
import React from "react";
import { useNavigate } from "react-router-dom";
import { useEffect, useState } from "react";
import useAuth from "../../hooks/useAuth";
import axios from "axios";

// Page Imports
import ClientCard from "../../components/ClientCard/ClientCard";
import JobCard from "../../components/JobCard/JobCard";

const ClientPage = () => {
  // State Functions
  const [user, token] = useAuth();
  const [jobs, setJobs] = useState([]);
  const [clients, setClients] = useState([]);
  const [activeClient, setActiveClient] = useState();
  const navigate = useNavigate();

  // UseEffects
  useEffect(() => {
    const fetchClients = async () => {
      try {
        let response = await axios.get("http://127.0.0.1:8000/api/clients/", {
          headers: {
            Authorization: "Bearer " + token,
          },
        });
        setClients(response.data);
        // console.log("ASYNC Clients: ", response.data[0]);
      } catch (error) {
        console.log(error);
      }
    };
    fetchClients();
  }, [token]);

  useEffect(() => {
    const makeClientActive = () => {
      try {
        if (clients.length === 1) {
          setActiveClient(clients[0]);
        }
        console.log("Active Client: ", activeClient);
      } catch (error) {
        console.log("Active Client ERROR: ", error);
      }
    };
    makeClientActive();
  }, [token, clients, activeClient]);

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

  // Console Logs:
  console.log("Clients:", clients);

  return (
    <>
      {activeClient && (
        <>
          <div className="container">
            <h1>
              Home Page for {activeClient.first_name} {activeClient.last_name}!
            </h1>
          </div>
          <>
            <ClientCard />
            History
            {jobs && (
              <table>
                <thead>
                  <th>Date</th>
                  <th> </th>
                  <th>Address</th>
                  <th> </th>
                  <th>Cost</th>
                  <th> </th>
                  <th>Paid?</th>
                </thead>
                {jobs.map((job, i) => (
                  <tbody key={job.id}>
                    <JobCard job={job} />
                  </tbody>
                ))}
              </table>
            )}
          </>
        </>
      )}
    </>
  );
};

export default ClientPage;
