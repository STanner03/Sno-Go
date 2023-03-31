// General Imports
import React from "react";
import { useNavigate, Link } from "react-router-dom";
import { useEffect, useState } from "react";
import useAuth from "../../hooks/useAuth";
import axios from "axios";

const JobCard = ({ job, providers }) => {
  // State Functions
  const [user, token] = useAuth();
  const [jobProvider, setJobProvider] = useState([]);

  // UseEffects
  useEffect(() => {
    const createJobProvider = () => {
      try {
        if (providers.length === 1) {
          setJobProvider(providers[0]);
        } else if (providers.length > 1) {
          let temp = providers.filter((id) => job.provider_id);
          setJobProvider(temp);
          console.log("Temp", temp);
        } else {setJobProvider(null)}
        console.log("Job Provider: ", jobProvider);
      } catch (error) {
        console.log("Job Provider ERROR: ", error);
      }
    };
    createJobProvider();
  }, [token]);

  let date = new Date(job.date_requested).toLocaleDateString("en-US");
  let paid = " ";
  if (job.provider_id == null) {
    paid = "Waiting for a Provider to claim.";
  } else {
    if (job.paid == null || job.paid == false) {
      paid = "Not Paid";
    } else {
      paid = "Paid in Full";
    }
  }

  console.log("Job", job);

  return (
    <>
      <td> {date} </td>
      <td> </td>
      <td> {job.address} </td>
      <td> </td>
      <td> {job.date_completed ? "Complete" : "No"} </td>
      <td> </td>
      <td> {job.date_completed} </td>
      <td> </td>
      <td>
        {" "}
        {jobProvider.first_name} {jobProvider.last_name}{" "}
      </td>
      <td> </td>
      <td> {job.recurring} </td>
      <td> </td>
      <td> ${job.total_price} </td>
      <td> </td>
      <td> {paid} </td>
    </>
  );
};

export default JobCard;
