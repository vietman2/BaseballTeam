import { useState } from "react";
import {
  KeyboardAvoidingView,
  View,
  TextInput,
  Platform,
  TouchableOpacity,
  Text,
  Image,
} from "react-native";
import { NativeStackScreenProps } from "@react-navigation/native-stack";

import { AuthStackParamList } from "../Base";
import { viewStyles, textStyles, containerStyles } from "./styles";


type Props = NativeStackScreenProps<AuthStackParamList, "Login">;

interface buttonProps {
  text: string;
  onPress: () => void;
}

const MyButton = (props: buttonProps) => {
  return (
    <TouchableOpacity style={viewStyles.button} onPress={props.onPress}>
      <Text style={textStyles.buttonText}>{props.text}</Text>
    </TouchableOpacity>
  );
};

export default function Login({ navigation }: Props) {
  const [username, setUsername] = useState<string>("");
  const [password, setPassword] = useState<string>("");
  const [errorMessage, setErrorMessage] = useState<string>("");

  const handleSignIn = async () => {
    // TODO: Implement login
  };
  const handleRegister = async () => {
    navigation.navigate("SignUp");
  };

  const TopBox = () => {
    return (
      <View style={containerStyles.topBoxContainer}>
        <Image
          source={require("../../../assets/logo.jpg")}
          style={viewStyles.logo}
        />
        <Text style={textStyles.titleText}>로그인</Text>
      </View>
    );
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
      <TopBox />
      <TextInputFields />
      <Buttons />
      {errorMessage ? <Text>{errorMessage}</Text> : null}
    </KeyboardAvoidingView>
  );
}
