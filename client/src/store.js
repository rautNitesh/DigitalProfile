import { createStore, applyMiddleware } from "redux";

import thunk from "redux-thunk";
import { composeWithDevTools } from "redux-devtools-extension";

import rootReducers from "./reducer";

const middleware = [thunk];

const initialState = {};

export default createStore(
  rootReducers,
  initialState,
  composeWithDevTools(applyMiddleware(...middleware))
);
