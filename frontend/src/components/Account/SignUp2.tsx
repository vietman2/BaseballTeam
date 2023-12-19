import { useState } from "react";
import { KeyboardAvoidingView, Platform, TextInput, View } from "react-native";

import { TopBox, MyButton } from "./Components";
import { containerStyles, viewStyles } from "./styles";
import { Checkbox } from "react-native-paper";

export default function SignUp2() {
  const [studentID, setStudentID] = useState<string>("");
  const [department, setDepartment] = useState<string>("");
  const [position, setPosition] = useState<string>("");
  const [isPitcher, setIsPitcher] = useState<boolean>(false);

  const handleSignUp = async () => {};

  const TextInputFields = () => {
    return (
      <View style={containerStyles.textInputContainer}>
        <View>
          <TextInput
            style={viewStyles.textInputField}
            placeholder="학번"
            onChangeText={(text) => setStudentID(text)}
            value={studentID}
          />
          <TextInput
            style={viewStyles.textInputField}
            placeholder="학과"
            onChangeText={(text) => setDepartment(text)}
            value={department}
          />
          <TextInput
            style={viewStyles.textInputField}
            placeholder="포지션"
            onChangeText={(text) => setPosition(text)}
            value={position}
          />
          <Checkbox 
            status={isPitcher ? 'checked' : 'unchecked'}
            onPress={() => {
              setIsPitcher(!isPitcher);
            }}
          />
        </View>
      </View>
    );
  }  

  const Buttons = () => {
    return (
      <View style={containerStyles.buttonContainer}>
        <MyButton text="회원가입" onPress={handleSignUp} />
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
      <TopBox title="회원가입" />
      <TextInputFields />
      <Buttons />
    </KeyboardAvoidingView>
  );
}
