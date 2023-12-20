import { useState } from "react";
import {
  KeyboardAvoidingView,
  View,
  TextInput,
  Platform,
  Text,
} from "react-native";
import { StackNavigationProp } from "@react-navigation/stack";

import TextButton from "../../components/Button/TextButton";
import LogoTitle from "../../components/Title/LogoTitle";
import { RootStackParamList } from "../../variables/navigation";
import { viewStyles, textStyles, containerStyles } from "../styles";

type LoginNavigationProp = StackNavigationProp<RootStackParamList, "Login">;
interface Props {
  navigation: LoginNavigationProp;
}

export default function Login({ navigation }: Props) {
  const [username, setUsername] = useState<string>("");
  const [password, setPassword] = useState<string>("");
  const [errorMessage, setErrorMessage] = useState<string>("");

  const handleSignIn = async () => {
    navigation.navigate("Main");
  };
  const handleRegister = async () => {
    navigation.navigate("SignUp");
  };

  const TextInputFields = () => {
    return (
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
    );
  };

  const Buttons = () => {
    return (
      <View style={containerStyles.buttonContainer}>
        <TextButton text="로그인" onPress={handleSignIn} />
        {errorMessage ? (
          <Text style={textStyles.errorText}>{errorMessage}</Text>
        ) : null}
        <Text style={textStyles.normalText}>계정이 없으신가요?</Text>
        <TextButton text="회원가입" onPress={handleRegister} />
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
      <LogoTitle title="로그인 화면" />
      <TextInputFields />
      <Buttons />
    </KeyboardAvoidingView>
  );
}
