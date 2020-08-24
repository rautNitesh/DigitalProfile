import { combineReducers } from "redux";

import authReducer from "./authReducer";
import errorReducer from "./errorReducer";
import citizenReducer from "./citizenReducer";

export default combineReducers({
  auth: authReducer,
  errors: errorReducer,
  citizens: citizenReducer,
});
