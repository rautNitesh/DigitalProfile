import React from "react";
import { Pie } from "react-chartjs-2";

function Chart() {
  const [chartData, setChartData] = React.useState({
    labels: ["x", "y", "z"],
    datasets: [
      {
        label: "population",
        data: [10, 20, 30],
        backgroundColor: [
          "rgba(255, 55, 50, 0.6)",
          "rgba(155, 55, 50, 0.6)",
          "rgba(55, 55, 50, 0.6)",
        ],
      },
    ],
  });
  return (
    <section className="chart-container">
      <Pie
        data={chartData}
        width={50}
        height={300}
        options={{ maintainAspectRatio: false }}
      />
    </section>
  );
}
export default Chart;
