import { View, Text } from "react-native";
import { BottomTabScreenProps } from "@react-navigation/bottom-tabs";
import { RootTabParamList } from "../../containers/MainContainer";

type TrainingProps = BottomTabScreenProps<RootTabParamList, "Training">;

export default function Training({ navigation }: TrainingProps) {
  return (
    <View style={{ flex: 1, justifyContent: "center", alignItems: "center" }}>
      <Text>훈참표 화면</Text>
    </View>
  );
}
