import { LITERACY_BASED_ON_WARD } from "../action/types";

const intialState = {
  labels: [],
  datasets: [
    {
      data: [],
    },
  ],
};

export default (state = intialState, action) => {
  switch (action.type) {
    case LITERACY_BASED_ON_WARD:
      return {
        ...state,
        labels: action.payload.labels,
        datasets: action.payload.datasets,
      };
    default:
      return state;
  }
};
