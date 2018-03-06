import axios from 'axios'
import settings from '../../settings.json'

export const myApi = axios.create({
  baseURL: `http://${settings.settings.ip_host}:5000/api`,
  timeout: 10000,
  // withCredentials: true,
  transformRequest: [(data) => JSON.stringify(data)],
  headers: {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
  }
})
