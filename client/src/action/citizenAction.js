import { GET_ERRORS } from "./types";
import { LITERACY_BASED_ON_WARD } from "./types";
import { getCitizen } from "../services/citizen";

const fetchCitizen = () => async (dispatch) => {
  try {
    const formattedResponse = await getCitizen();
    console.log(formattedResponse);
    dispatch({
      type: LITERACY_BASED_ON_WARD,
      payload: formattedResponse,
    });
  } catch (error) {
    dispatch({
      type: GET_ERRORS,
      payload: error.response,
    });
  }
};

export default fetchCitizen;
