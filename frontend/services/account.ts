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
        console.log(response.data);
        return response.data;
    } catch (error: any) {
        return error.response.data;
    }
}

export async function logout() {
    // TODO: 로그아웃 API 호출, 토큰 삭제
    const url = `${API_BASE_URL}/api/account/signout/`;
    try{
        const response = await axios.post(url, {
            headers: {
                Authorization: `Bearer ${await AsyncStorage.getItem("accessToken")}`,
            },
        });
        await AsyncStorage.removeItem("accessToken");
        await AsyncStorage.removeItem("refreshToken");
        console.log(response.data);
        return response.data;
    } catch (error: any) {
        return error.response.data;
    }
}

export async function signup (user_type: number, name: string, phone_number: string, major: string, grade: number, position: number, password: string) {
    // TODO: 회원가입 API 호출
    const url = `${API_BASE_URL}/api/account/signup/`;
    try{
        const response = await axios.post(url, {
            user_type, name, phone_number, major, grade, position, password
        });
        await AsyncStorage.setItem("accessToken", response.data.access_token);
        await AsyncStorage.setItem("refreshToken", response.data.refresh_token);
        console.log(response.data);
        return response.data;
    } catch (error: any) {
        return error.response.data;
    }
    }



