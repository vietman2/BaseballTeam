import { View, StyleSheet } from "react-native";
import { Text } from "react-native-paper";

import WeeklyTable from "../../../components/WeeklyTable/WeeklyTable";

export default function Home() {
  return (
    <View style={styles.container}>
      <Text variant="titleLarge" style={styles.title}>이번주 훈련참가표</Text>
      <WeeklyTable />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    marginTop: 60,
  },
  title: {
    textAlign: "center",
    fontWeight: "bold",
  },
});
