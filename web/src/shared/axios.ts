import axios from "axios";

export default axios.create({
  baseURL: "http://localhost:8000/api/",
  headers: {
    "Content-type": "application/json",
    // "Authorization": `Token ${localStorage.getItem('token')}`
  },
  xsrfCookieName: 'XSRF-TOKEN', // default
  // `xsrfHeaderName` is the name of the http header that carries the xsrf token value
  xsrfHeaderName: 'X-XSRF-TOKEN', // default
  withCredentials: true
});

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'
axios.defaults.withCredentials = true

const auth_headers = {
  "Content-type": "application/json",
  "Authorization": `Token ${localStorage.getItem('token')}`
}

export { auth_headers };
