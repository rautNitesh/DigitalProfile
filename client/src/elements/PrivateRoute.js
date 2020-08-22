import React from "react";
import { Route, Redirect, Switch } from "react-router-dom";
import { connect } from "react-redux";
import Dashboard from "../components/Dashboard/Dashboard";

function PrivateRoute(props) {
  const { auth } = props;
  if (!auth.isAuthenticated) {
    return <Redirect to="/login" />;
  }
  return (
    <Switch>
      <Route exact path="/" component={() => <h1>Home</h1>} />
      <Route path="/dashboard" component={Dashboard} />
    </Switch>
  );
}

const mapStateToProps = (state) => ({
  auth: state.auth,
});

export default connect(mapStateToProps)(PrivateRoute);
