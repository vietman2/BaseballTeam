import { useState } from "react";
import {
  KeyboardAvoidingView,
  View,
  TextInput,
  Platform,
  Text,
} from "react-native";
import { NativeStackScreenProps } from "@react-navigation/native-stack";

import { AuthStackParamList } from "../../containers/AccountContainer";
import { viewStyles, textStyles, containerStyles } from "./styles";
import { MyButton, TopBox } from "./Components";

type Props = NativeStackScreenProps<AuthStackParamList, "Login">;

export default function Login({ navigation }: Props) {
  const [username, setUsername] = useState<string>("");
  const [password, setPassword] = useState<string>("");
  const [errorMessage, setErrorMessage] = useState<string>("");

  const handleSignIn = async () => {
    /* Error 1: username or password is empty
    if (username === "" || password === "") {
      setErrorMessage("아이디와 비밀번호를 입력해주세요.");
      return;
    } */
    // Error 2: username or password is wrong
    // Error 3: server error
    // Error 4: network error
    // Error 5: unknown error
    // If there is no error, navigate to the main page
  };
  const handleRegister = async () => {
    navigation.navigate("SignUp");
  };

  // const TextInputFields = () => {
  //   return (
  //     <View style={containerStyles.textInputContainer}>
  //       <TextInput
  //         style={viewStyles.textInputField}
  //         placeholder="아이디"
  //         onChangeText={(text) => setUsername(text)}
  //         value={username}
  //       />
  //       <TextInput
  //         style={viewStyles.textInputField}
  //         placeholder="비밀번호"
  //         onChangeText={(text) => setPassword(text)}
  //         value={password}
  //       />
  //     </View>
  //   );
  // };

  const Buttons = () => {
    return (
      <View style={containerStyles.buttonContainer}>
        <MyButton text="로그인" onPress={handleSignIn} />
        {errorMessage ? (
          <Text style={textStyles.errorText}>{errorMessage}</Text>
        ) : null}
        <Text style={textStyles.normalText}>계정이 없으신가요?</Text>
        <MyButton text="회원가입" onPress={handleRegister} />
      </View>
    );
  };

  return (
    <KeyboardAvoidingView
      style={containerStyles.mainContainer}
      behavior={Platform.OS === "ios" ? "padding" : "height"}
      keyboardVerticalOffset={Platform.OS === "ios" ? 0 : 20}
      enabled
    >
      <TopBox title="로그인" />
      <View style={containerStyles.textInputContainer}>
        <TextInput
          style={viewStyles.textInputField}
          placeholder="아이디"
          onChangeText={(text) => setUsername(text)}
          value={username}
        />
        <TextInput
          style={viewStyles.textInputField}
          placeholder="비밀번호"
          onChangeText={(text) => setPassword(text)}
          value={password}
        />
      </View>
      <Buttons />
    </KeyboardAvoidingView>
  );
}
