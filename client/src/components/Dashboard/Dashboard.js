import React from "react";

import "./Dashboard.css";
import Chart from "../chart";
import Card from "../../elements/Card";
import { Link } from "react-router-dom";

export default function Dashboard() {
  return (
    <section className="container">
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
      <section className="chart-container">
        <Card>
          <Chart />
        </Card>
      </section>
    </section>
  );
}
