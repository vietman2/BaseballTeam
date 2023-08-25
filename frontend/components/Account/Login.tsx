import { useState } from "react";
import {
  KeyboardAvoidingView,
  View,
  TextInput,
  Platform,
  Text,
} from "react-native";
import { NativeStackScreenProps } from "@react-navigation/native-stack";

import { AuthStackParamList } from "./Base";
import { viewStyles, textStyles, containerStyles } from "./styles";
import { MyButton, TopBox } from "./Components";

type Props = NativeStackScreenProps<AuthStackParamList, "Login">;

export default function Login({ navigation }: Props) {
  const [username, setUsername] = useState<string>("");
  const [password, setPassword] = useState<string>("");
  const [errorMessage, setErrorMessage] = useState<string>("");

  const handleSignIn = async () => {
    // TODO: Implement login
    setErrorMessage("로그인 기능은 아직 구현되지 않았습니다.");
  };
  const handleRegister = async () => {
    navigation.navigate("SignUp");
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
            placeholder="비밀번호"
            onChangeText={(text) => setPassword(text)}
            value={password}
          />
        </View>
      </View>
    );
  };

  const Buttons = () => {
    return (
      <View style={containerStyles.buttonContainer}>
        <MyButton text="로그인" onPress={handleSignIn} />
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
      <TextInputFields />
      <Buttons />
      {errorMessage ? <Text>{errorMessage}</Text> : null}
    </KeyboardAvoidingView>
  );
}
