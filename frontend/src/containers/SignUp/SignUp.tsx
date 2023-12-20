import { useState } from "react";
import {
  Text,
  KeyboardAvoidingView,
  Platform,
  View,
  TextInput,
} from "react-native";
import { StackNavigationProp } from "@react-navigation/stack";

import TextButton from "../../components/Button/TextButton";
import LogoTitle from "../../components/Title/LogoTitle";
import { RootStackParamList } from "../../variables/navigation";
import { containerStyles, viewStyles } from "../styles";

type SignUpNavigationProp = StackNavigationProp<RootStackParamList, "SignUp">;
interface Props {
  navigation: SignUpNavigationProp;
}

export default function SignUp({ navigation }: Props) {
  const [username, setUsername] = useState<string>("");
  const [phoneNumber, setPhoneNumber] = useState<string>("");
  const [password, setPassword] = useState<string>("");
  const [passwordCheck, setPasswordCheck] = useState<string>("");
  const [errorMessage, setErrorMessage] = useState<string>("");

  const handleSignUp = async () => {
    navigation.navigate("Main");
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
  };

  const Buttons = () => {
    return (
      <View style={containerStyles.buttonContainer}>
        <TextButton text="가입하기" onPress={handleSignUp} />
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
      <LogoTitle title="회원가입" />
      <TextInputFields />
      <Buttons />
      {errorMessage ? <Text>{errorMessage}</Text> : null}
    </KeyboardAvoidingView>
  );
}
