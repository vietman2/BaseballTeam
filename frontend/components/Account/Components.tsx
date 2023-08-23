import { Text, TouchableOpacity, View, Image } from "react-native";

import { containerStyles, viewStyles, textStyles } from "./styles";

interface buttonProps {
  text: string;
  onPress: () => void;
}

export const MyButton = (props: buttonProps) => {
  return (
    <TouchableOpacity style={viewStyles.button} onPress={props.onPress}>
      <Text style={textStyles.buttonText}>{props.text}</Text>
    </TouchableOpacity>
  );
};

interface TopBoxProps {
    title: string;
}

export const TopBox = (props: TopBoxProps) => {
  return (
    <View style={containerStyles.topBoxContainer}>
      <Image
        source={require("../../assets/logo.jpg")}
        style={viewStyles.logo}
      />
      <Text style={textStyles.titleText}>{props.title}</Text>
    </View>
  );
};