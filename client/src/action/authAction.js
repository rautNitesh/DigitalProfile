import axios from "axios";
import jwt_decode from "jwt-decode";

import { SET_CURRENT_USER, GET_ERRORS } from "./types";
import { SECRET_KEY, API } from "../config";

export const loginUser = (userData, history) => (dispatch) => {
  axios
    .post(`${API}/auth/`, userData)
    .then((res) => {
      const { token } = res.data;
      localStorage.setItem("token", token);
      const decoded = jwt_decode(token, SECRET_KEY);
      dispatch(setCurrentUser(decoded));
      history.push("dashboard");
    })
    .catch((err) =>
      dispatch({
        type: GET_ERRORS,
        payload: err.response.data,
      })
    );
};

export const setCurrentUser = (decoded) => {
  return {
    type: SET_CURRENT_USER,
    payload: decoded,
  };
};
