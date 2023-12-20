import { createMaterialBottomTabNavigator } from "react-native-paper/react-navigation";
import MaterialCommunityIcons from "react-native-vector-icons/MaterialCommunityIcons";

import HomeScreen from "./Home/Home";
import TrainingScreen from "./Training/Training";
import MyPageScreen from "./MyPage/MyPage";
import CalendarScreen from "./Calendar/Calendar";
import { BottomTabParamList } from "../../variables/navigation";

const Tab = createMaterialBottomTabNavigator<BottomTabParamList>();

export default function Tabs() {
  return (
      <Tab.Navigator
        initialRouteName="Home"
        barStyle={{ marginBottom: -15 }}
        >
        <Tab.Screen
          name="Home"
          component={HomeScreen}
          options={{
            tabBarLabel: "Home",
            tabBarIcon: ({ color }) => (
              <MaterialCommunityIcons name="ios-home" color={color} size={26} />
            ),
          }}
        />
        <Tab.Screen
          name="Training"
          component={TrainingScreen}
          options={{
            tabBarLabel: "Training",
            tabBarIcon: ({ color }) => (
              <MaterialCommunityIcons name="ios-fitness" color={color} size={26} />
            ),
          }}
        />
        <Tab.Screen
          name="Calendar"
          component={CalendarScreen}
          options={{
            tabBarLabel: "Calendar",
            tabBarIcon: ({ color }) => (
              <MaterialCommunityIcons name="ios-calendar" color={color} size={26} />
            ),
          }}
        />
        <Tab.Screen
          name="MyPage"
          component={MyPageScreen}
          options={{
            tabBarLabel: "MyPage",
            tabBarIcon: ({ color }) => (
              <MaterialCommunityIcons name="ios-person" color={color} size={26} />
            ),
          }}
        />
      </Tab.Navigator>
  );
}
