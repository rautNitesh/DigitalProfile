import React from "react";
import { connect } from "react-redux";

import ChartUI from "./Chart.component";
import fetchCitizen from "../../action/citizenAction";

function Chart(props) {
  const { fetchCitizen, citizens } = props;
  React.useEffect(() => {
    fetchCitizen();
  }, []);

  return citizens ? <ChartUI citizens={citizens} /> : "Loading...";
}
const mapStateToProps = (state) => ({
  citizens: state.citizens,
});
export default connect(mapStateToProps, { fetchCitizen })(Chart);
