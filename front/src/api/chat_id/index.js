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
