import { View, Text } from "react-native";
import { BottomTabScreenProps } from "@react-navigation/bottom-tabs";
import { RootTabParamList } from "../../containers/MainContainer";

type MyPageProps = BottomTabScreenProps<RootTabParamList, "MyPage">;

export default function MyPage({ navigation }: MyPageProps) {
  return (
    <View style={{ flex: 1, justifyContent: "center", alignItems: "center" }}>
      <Text>마이페이지 화면</Text>
    </View>
  );
}
