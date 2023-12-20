import axios from "axios";
import AsyncStorage from "@react-native-async-storage/async-storage";
import { API_BASE_URL } from "./apiConfig";

export async function login(email: string, password: string) {
  const url = `${API_BASE_URL}/api/account/signin/`;

  try {
    const response = await axios.post(url, {
      email,
      password,
    });

    await AsyncStorage.setItem("accessToken", response.data.access_token);
    await AsyncStorage.setItem("refreshToken", response.data.refresh_token);

    return response.data;
  } catch (error: any) {
    return error;
  }
}
/*
export async function logout() {
  // TODO: 로그아웃 API 호출, 토큰 삭제
}

export async function signup() {
  // TODO: 회원가입 API 호출
}
*/
