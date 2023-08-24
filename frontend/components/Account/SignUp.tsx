import { useState } from "react";
import { Text, KeyboardAvoidingView, Platform, View, TextInput } from "react-native";
import { NativeStackScreenProps } from "@react-navigation/native-stack";

import { MyButton, TopBox } from "./Components";
import { AuthStackParamList } from "./Base";
import { containerStyles, viewStyles } from "./styles";

type Props = NativeStackScreenProps<AuthStackParamList, "SignUp">;

export default function SignUp({ navigation }: Props) {
  const [username, setUsername] = useState<string>("");
  const [phoneNumber, setPhoneNumber] = useState<string>("");
  const [password, setPassword] = useState<string>("");
  const [passwordCheck, setPasswordCheck] = useState<string>("");
  const [errorMessage, setErrorMessage] = useState<string>("");

  const handleNext = async () => {
    if (password !== passwordCheck) {
      setErrorMessage("비밀번호가 일치하지 않습니다.");
      return;
    }
    navigation.navigate("SignUp2");
  };

  const TextInputFields = () => {
    return (
      <View style={containerStyles.textInputContainer}>
        <View>
          <TextInput
            style={viewStyles.textInputField}
            placeholder="아이디"
            onChangeText={(text) => setUsername(text)}
            value={username}
          />
          <TextInput
            style={viewStyles.textInputField}
            placeholder="전화번호 (주장단 기록용)"
            onChangeText={(text) => setPhoneNumber(text)}
            value={phoneNumber}
          />
          <TextInput
            style={viewStyles.textInputField}
            placeholder="비밀번호"
            onChangeText={(text) => setPassword(text)}
            value={password}
          />
          <TextInput
            style={viewStyles.textInputField}
            placeholder="비밀번호 확인"
            onChangeText={(text) => setPasswordCheck(text)}
            value={passwordCheck}
          />
        </View>
      </View>
    );
  }

  const Buttons = () => {
    return (
      <View style={containerStyles.buttonContainer}>
        <MyButton text="계속하기 (1/2)" onPress={handleNext} />
      </View>
    );
  }

  return (
    <KeyboardAvoidingView
      style={containerStyles.mainContainer}
      behavior={Platform.OS === "ios" ? "padding" : "height"}
      keyboardVerticalOffset={Platform.OS === "ios" ? 0 : 20}
      enabled
    >
      <TopBox title="회원가입" />
      <TextInputFields />
      <Buttons />
      {errorMessage ? <Text>{errorMessage}</Text> : null}
    </KeyboardAvoidingView>
  );
}
