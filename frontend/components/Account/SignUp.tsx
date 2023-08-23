import { useState } from "react";
import { Text, KeyboardAvoidingView, Platform, View, TextInput } from "react-native";

import { TopBox } from "./Components";
import { containerStyles, viewStyles } from "./styles";

export default function SignUp() {
  const [username, setUsername] = useState<string>("");
  const [phoneNumber, setPhoneNumber] = useState<string>("");
  const [password, setPassword] = useState<string>("");
  const [passwordCheck, setPasswordCheck] = useState<string>("");
  const [errorMessage, setErrorMessage] = useState<string>("");

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
            placeholder="전화번호"
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

  return (
    <KeyboardAvoidingView
      style={containerStyles.mainContainer}
      behavior={Platform.OS === "ios" ? "padding" : "height"}
      keyboardVerticalOffset={Platform.OS === "ios" ? 0 : 20}
      enabled
    >
      <TopBox />
      <TextInputFields />
      {errorMessage ? <Text>{errorMessage}</Text> : null}
    </KeyboardAvoidingView>
  );
}
