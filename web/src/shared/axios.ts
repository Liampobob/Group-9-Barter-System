import axios from "axios";

export default axios.create({
  baseURL: "http://localhost:8080/api", // TODO update with actual port
  headers: {
    "Content-type": "application/json",
  },
});
