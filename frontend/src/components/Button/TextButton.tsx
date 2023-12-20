import { Text, TouchableOpacity, StyleSheet } from "react-native";

interface TextButtonProps {
  text: string;
  onPress: () => void;
}

export default function TextButton(props: TextButtonProps) {
  return (
    <TouchableOpacity style={styles.button} onPress={props.onPress}>
      <Text style={styles.buttonText}>{props.text}</Text>
    </TouchableOpacity>
  );
}

const styles = StyleSheet.create({
  button: {
    height: 40,
    backgroundColor: "#00aeef",
    borderRadius: 5,
    alignItems: "center",
    justifyContent: "center",
    marginVertical: 10,
  },
  buttonText: {
    fontSize: 20,
    fontWeight: "bold",
  },
});
