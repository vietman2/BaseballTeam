import { View, Text } from "react-native";
import { BottomTabScreenProps } from "@react-navigation/bottom-tabs";
import { RootTabParamList } from "../../containers/MainContainer";

type CalendarProps = BottomTabScreenProps<RootTabParamList, "Calendar">;

export default function Calendar({ navigation }: CalendarProps) {
  return (
    <View style={{ flex: 1, justifyContent: "center", alignItems: "center" }}>
      <Text>캘린더 화면</Text>
    </View>
  );
}
