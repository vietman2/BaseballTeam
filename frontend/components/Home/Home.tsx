import { View, Text } from "react-native";
import { BottomTabScreenProps } from "@react-navigation/bottom-tabs";
import { RootTabParamList } from "../../containers/MainContainer";

type HomeProps = BottomTabScreenProps<RootTabParamList, "Home">;

export default function Home({ navigation }: HomeProps) {
  return (
    <View style={{ flex: 1, justifyContent: "center", alignItems: "center" }}>
      <Text>홈 화면</Text>
    </View>
  );
}
