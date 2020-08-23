import React, { useState } from "react";
import { connect } from "react-redux";
import { useHistory } from "react-router";

import Input from "../../elements/Input";
import "./login.css";
import Button from "../../elements/Button";
import { loginUser } from "../../action/authAction";

function Login(props) {
  const history = useHistory();
  const [isLoading, setLoading] = useState(false);
  const usernameRef = React.useRef(null);
  const passwordRef = React.useRef(null);
  // I've used useRef hook to optimize the onchange event, now it only re-render on submit on every input change.
  // const onchange = (name, value) => {
  //   setData((prev) => ({ ...prev, [name]: value }));
  // };
  const handleSubmit = (e) => {
    e.preventDefault();

    setLoading(true);

    const userData = {
      username: usernameRef.current.value,
      password: passwordRef.current.value,
    };
    setTimeout(() => {
      props.loginUser(userData, history);
      console.log(isLoading);
      setLoading(false);
    }, 1000);
  };

  if (props.auth.isAuthenticated) {
    props.history.push("/dashboard");
  }
  let color = null;
  if (props.errors.hasError) color = "#EF5350";

  console.log("login");

  return (
    <section className="form-container">
      {isLoading ? (
        "Loading..."
      ) : (
        <form className="form form-control" onSubmit={handleSubmit}>
          <Input
            forwardRef={usernameRef}
            color={color}
            label={
              props.errors.hasError ? "Enter valid credentials" : "Username"
            }
            name="username"
            type="text"
            placeholder="Enter your email"
            classname="input"
            // onChange={onchange}
          />
          <Input
            forwardRef={passwordRef}
            label={props.errors.hasError ? "" : "Password"}
            color={color}
            name="password"
            type="password"
            placeholder="Enter your password"
            classname="input"
            // onChange={onchange}
          />
          <Button type="submit" classname="btn btn-submit" />
        </form>
      )}
    </section>
  );
}

const mapStateToProps = (state) => ({
  auth: state.auth,
  errors: state.errors,
});
export default connect(mapStateToProps, { loginUser })(Login);
