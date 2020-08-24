import axios from "axios";

import { API } from "../config";

export const DigitalProfile = axios.create({
  baseURL: API,
  headers: {
    "Content-Type": "application/json",
  },
});
