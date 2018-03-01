import axios from 'axios'
export const myApi = axios.create({
  baseURL: 'http://192.168.5.24:5000/api',
  timeout: 10000,
  // withCredentials: true,
  transformRequest: [(data) => JSON.stringify(data)],
  headers: {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
  }
})
