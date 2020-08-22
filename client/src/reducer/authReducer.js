import { SET_CURRENT_USER } from "../action/types";

import isValueEmpty from "../validation/isValueEmpty";

const initialState = {
  isAuthenticated: false,
  users: {},
};

export default (state = initialState, action) => {
  switch (action.type) {
    case SET_CURRENT_USER:
      return {
        ...state,
        isAuthenticated: !isValueEmpty(action.payload),
        users: action.payload,
      };
    default:
      return state;
  }
};
