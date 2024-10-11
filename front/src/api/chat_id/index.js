import axios from "axios";

const BASE_URL = process.env.REACT_APP_BUILD_BASE_URL;

export async function getAllChatId() {
  try {
    const response = await axios.get(`${BASE_URL}/get_all_chat_ids`);
    return response.data;
  } catch (error) {
    console.error(error);
    throw error;
  }
}

export async function reloadChatIds() {
  try {
    const response = await axios.get(`${BASE_URL}/synchronize_chat_ids`);
    return response.data;
  } catch (error) {
    console.error(error);
    throw error;
  }
}

export async function getGroupNames() {
  try {
    const response = await axios.get(`${BASE_URL}/get_group_names`);
    return response.data;
  } catch (error) {
    console.error(error);
    throw error;
  }
}

export async function updateChatGroups(chatGroups) {
  try {
    const response = await axios.post(
      `${BASE_URL}/edit_chat_group`,
      chatGroups
    );
    return response.data;
  } catch (error) {
    console.error(error);
    throw error;
  }
}
