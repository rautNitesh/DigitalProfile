import { DigitalProfile } from "./axiosInstance";
import Endpoint from "../constants/endpoint";

export const getCitizen = async () => {
  const response = await DigitalProfile.get(Endpoint.GET_CITIZEN);
  return {
    labels: formatLabel(response.data),
    datasets: formatDataset(response.data),
  };
};

const formatDataset = (response) => {
  return [{ data: response.map((data) => data.count) }];
};
const formatLabel = (literacy) => {
  return literacy.map((data) => data.literacy);
};
