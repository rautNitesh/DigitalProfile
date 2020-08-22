import { GET_ERRORS } from "../action/types";
import isValueEmpty from "../validation/isValueEmpty";

const initialState = {
  hasError: false,
  errors: {},
};

export default (state = initialState, action) => {
  switch (action.type) {
    case GET_ERRORS:
      return {
        ...state,
        hasError: !isValueEmpty(action.payload),
        errors: action.payload,
      };
    default:
      return state;
  }
};
