import React from "react";
import { Pie } from "react-chartjs-2";

function ChartUI(props) {
  const { citizens } = props;
  return (
    <section className="chart-container">
      <Pie
        data={citizens}
        width={50}
        height={300}
        options={{ maintainAspectRatio: false }}
      />
    </section>
  );
}

export default ChartUI;
