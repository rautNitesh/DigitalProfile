import React from "react";
import { Link } from "react-router-dom";
import "./Dashboard.css";

export default function Dashboard() {
  return (
    <section>
      <aside>
        <ul>
          <li>
            <Link to="#">
              <img src="" alt="userImage" />
              <span>Username</span>
            </Link>
          </li>
          <li>
            <Link to="/">Home</Link>
          </li>
          <li>
            <Link to="/">Services</Link>
          </li>
          <li>
            <Link to="/">About us</Link>
          </li>
        </ul>
      </aside>
    </section>
  );
}
