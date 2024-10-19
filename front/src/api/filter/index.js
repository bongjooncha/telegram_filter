import axios from "axios";

const BASE_URL = process.env.REACT_APP_BUILD_BASE_URL;

export async function getAllFilter() {
  try {
    const response = await axios.get(`${BASE_URL}/filter/get_filter`);
    return response.data;
  } catch (error) {
    console.error(error);
    throw error;
  }
}

export async function getFilter(filter) {
  try {
    const response = await axios.get(`${BASE_URL}/filter/get_filter/${filter}`);
    return response.data;
  } catch (error) {
    console.error(error);
    throw error;
  }
}

export async function deleteFilter(filter) {
  try {
    const response = await axios.delete(
      `${BASE_URL}/filter/delete_filter/${filter}`
    );
    return response.data;
  } catch (error) {
    console.error(error);
    throw error;
  }
}

export async function updateFilter(filter_info) {
  try {
    const response = await axios.post(
      `${BASE_URL}/filter/edit_filter`,
      filter_info
    );
    return response.data;
  } catch (error) {
    console.error(error);
    throw error;
  }
}
