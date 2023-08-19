import { StyleSheet } from "react-native";

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#fff",
  },
  textInputBox: {
    marginTop: 300,
    alignItems: "center",
    justifyContent: "center",
  },
  textInputField: {
    width: 300,
    height: 50,
    marginVertical: 10,
    padding: 10,
    borderWidth: 1,
    borderRadius: 10,
    borderColor: "#00ffff",
  },
  buttonBox: {
    flexDirection: "row",
    justifyContent: "flex-end",
  },
  button: {
    flexDirection: "row",
    justifyContent: "flex-end",
    marginRight: 60,
    marginTop: 10,
    width: 100,
    height: 50,
    padding: 10,
    borderWidth: 1,
    borderRadius: 10,
    borderColor: "#00ffff",
  },
  buttonText: {
    fontSize: 20,
    fontWeight: "bold",
  },
});

export { styles };