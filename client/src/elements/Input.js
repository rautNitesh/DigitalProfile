import React from "react";
import "./Input.css";

export default function Input(props) {
  // const [value, setValue] = React.useState("");

  // const handleChange = (event) => {
  //   setValue(props.forwardRef.current.value);
  //   props.onChange(event.target.name, inputRef.current.value);
  // };
  // React.useEffect(() => {
  //   console.log(value);
  // }, []);
  console.log(props.color);
  return (
    <div className="input input-container">
      {props.label && <span style={{ color: props.color }}>{props.label}</span>}
      <input
        style={{ border: `1px solid ${props.color}` }}
        ref={props.forwardRef}
        name={props.name}
        type={props.type}
        placeholder={props.placeholder}
        // onChange={handleChange}
        className={props.classname}
        // value={value}
      />
    </div>
  );
}

Input.defaultProps = {
  name: "",
  type: "text",
  placeholder: "",
  className: "input",
};
