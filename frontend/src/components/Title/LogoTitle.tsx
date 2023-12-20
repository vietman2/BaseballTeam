import { View, Image, Text, StyleSheet } from "react-native";

interface LogoTitleProps {
  title: string;
}

export default function LogoTitle(props: LogoTitleProps) {
  return (
    <View style={styles.container}>
      <Image source={require("assets/images/logo.jpg")} style={styles.logo} />
      <Text style={styles.titleText}>{props.title}</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    marginTop: 30,
    alignItems: "center",
    justifyContent: "center",
  },
  logo: {
    width: 150,
    height: 150,
    alignSelf: "center",
    marginTop: 100,
  },
  titleText: {
    fontSize: 30,
    fontWeight: "bold",
    alignSelf: "center",
    marginTop: 20,
  },
});
