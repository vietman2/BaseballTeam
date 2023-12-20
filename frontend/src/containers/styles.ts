import { StyleSheet } from "react-native";

const viewStyles = StyleSheet.create({
  textInputField: {
    height: 40,
    borderColor: "gray",
    borderWidth: 1,
    borderRadius: 10,
    marginVertical: 10,
    paddingHorizontal: 10,
  },
});

const textStyles = StyleSheet.create({
  normalText: {
    fontSize: 15,
    fontWeight: "normal",
    alignSelf: "center",
    marginTop: 20,
  },
  errorText: {
    fontSize: 15,
    fontWeight: "normal",
    alignSelf: "center",
    marginTop: 10,
    color: "red",
  },
});

const containerStyles = StyleSheet.create({
  mainContainer: {
    flex: 1,
    backgroundColor: "#fff",
  },
  textInputContainer: {
    marginHorizontal: 50,
    alignItems: "stretch",
    justifyContent: "center",
  },

  buttonContainer: {
    marginHorizontal: 50,
    alignItems: "stretch",
    justifyContent: "center",
  },
});

export { viewStyles, textStyles, containerStyles };
