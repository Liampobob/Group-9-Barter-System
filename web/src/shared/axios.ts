import axios from "axios";
import Cookie from 'js-cookie'

export default axios.create({
  baseURL: "http://localhost:8000/api/",
  headers: {
    "Content-type": "application/json",
  },
  xsrfCookieName: 'XSRF-TOKEN', // default
  // `xsrfHeaderName` is the name of the http header that carries the xsrf token value
  xsrfHeaderName: 'X-XSRF-TOKEN', // default
  withCredentials: true
});

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'
axios.defaults.withCredentials = true
axios.interceptors.response.use(response => {
    const sessionCookie = Cookie.get()
    console.log('Cookie', sessionCookie)
    return response
});