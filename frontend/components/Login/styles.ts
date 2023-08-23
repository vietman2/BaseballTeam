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
  button: {
    height: 40,
    backgroundColor: "#00aeef",
    borderRadius: 5,
    alignItems: "center",
    justifyContent: "center",
    marginVertical: 10,
  },
  logo: {
    width: 150,
    height: 150,
    alignSelf: "center",
    marginTop: 100,
  },
});

const textStyles = StyleSheet.create({
  titleText: {
    fontSize: 30,
    fontWeight: "bold",
    alignSelf: "center",
    marginTop: 20,
  },
  buttonText: {
    fontSize: 20,
    fontWeight: "bold",
  },
  normalText: {
    fontSize: 15,
    fontWeight: "normal",
    alignSelf: "center",
    marginTop: 20,
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
  topBoxContainer: {
    marginTop: 70,
    alignItems: "center",
    justifyContent: "center",
  },
  buttonContainer: {
    marginHorizontal: 50,
    alignItems: "stretch",
    justifyContent: "center",
  },
});


export { viewStyles, textStyles, containerStyles };