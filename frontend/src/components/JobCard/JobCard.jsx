const JobCard = ({ job }) => {
  let date = new Date(job.date_requested).toLocaleDateString("en-US");
  let paid = " ";
  if (job.date_completed == null) {
    paid = "No Payment Needed";
  } else {
    if (job.paid == null || job.paid == false) {
      paid = "Not Paid";
    } else {
      paid = "Paid in Full";
    }
  }
  //   console.log("Date", date);

  return (
    <>
      <td> {date} </td>
      <td> </td>
      <td> {job.address} </td>
      <td> </td>
      <td> ${job.total_price} </td>
      <td> </td>
      <td> {paid} </td>
    </>
  );
};

export default JobCard;
