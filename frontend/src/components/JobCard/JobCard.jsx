// General Imports
import React from "react";
import { useNavigate, Link } from "react-router-dom";
import { useEffect, useState } from "react";
import useAuth from "../../hooks/useAuth";
import axios from "axios";

const JobCard = ({ job, providers }) => {
  // State Functions
  const [user, token] = useAuth();
  const [jobProvider, setJobProvider] = useState([null]);

  // UseEffects
  useEffect(() => {
    const createJobProvider = () => {
      try {
        if (providers.length > 0) {
          let temp = providers.filter((id) => job.provider_id);
          if (job.provider_id == null) {
            setJobProvider(null);
            console.log("No Job Provider: ", jobProvider);
          } else {
            setJobProvider(temp[0]);
            console.log("Found Job Provider", temp[0]);
          }
        } else {
          setJobProvider(null);
        }
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
  console.log("Job Provider", jobProvider);

  return (
    <>
      <td> {date} </td>
      <td> </td>
      <td> {job.address} </td>
      <td> </td>
      <td> {job.date_completed ? "Complete" : "No"} </td>
      <td> </td>
      <td> {job.date_completed ? `${job.date_completed}` : "TBD"} </td>
      <td> </td>
      <td>
        {" "}
        {job.provider_id
          ? `${jobProvider.first_name} ${jobProvider.last_name}`
          : null}
      </td>
      <td> </td>
      <td> {job.recurring ? "Yes" : "No"} </td>
      <td> </td>
      <td> ${job.total_price} </td>
      <td> </td>
      <td> {paid} </td>
    </>
  );
};

export default JobCard;
