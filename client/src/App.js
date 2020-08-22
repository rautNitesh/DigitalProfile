import React from "react";

import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import { Provider } from "react-redux";
import jwt_decode from "jwt-decode";

import Login from "./components/accounts/Login";
import store from "./store";
import PrivateRoute from "./elements/PrivateRoute";
import { SECRET_KEY } from "./config";
import { setCurrentUser } from "./action/authAction";

function App() {
  if (localStorage.token) {
    const decoded = jwt_decode(localStorage.token, SECRET_KEY);
    store.dispatch(setCurrentUser(decoded));
    const current = new Date() / 1000;
    if (decoded.exp < current) {
      store.dispatch(setCurrentUser({}));
      localStorage.removeItem("token");
    }
  }
  return (
    <Provider store={store}>
      <Router>
        <Switch>
          <Route path="/login" component={Login} />
          <Route path="/" component={PrivateRoute} />

          {/* <Route path="/login" component={() => <h1>App</h1>} /> */}
        </Switch>
      </Router>
    </Provider>
  );
}

export default App;
