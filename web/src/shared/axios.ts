import axios from "axios";

const instance = axios.create({
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

// Set the AUTH token for any authentificated request
instance.interceptors.request.use(function (config) {
  const token = localStorage.getItem('token');
  config.headers.Authorization = token ? `Token ${token}` : '';
  return config;
});

const authHeaders = {
  "Content-type": "application/json",
  "Authorization": `Token ${localStorage.getItem('token')}`
}

export default instance;

export { authHeaders };
