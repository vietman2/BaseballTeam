import { CommonActions } from "@react-navigation/native";
import { createBottomTabNavigator } from "@react-navigation/bottom-tabs";
import { BottomNavigation } from "react-native-paper";
import Ionicons from "react-native-vector-icons/Ionicons";

import HomeScreen from "../components/Home/Home";
import TrainingScreen from "../components/Training/Training";
import MyPageScreen from "../components/MyPage/MyPage";
import CalendarScreen from "../components/Calendar/Calendar";

type MainTabParamList = {
  Home: undefined;
  Training: undefined;
  MyPage: undefined;
  Calendar: undefined;
};

const Tab = createBottomTabNavigator<MainTabParamList>();

export default function MainContainer() {
  return (
      <Tab.Navigator
        initialRouteName="Home"
        screenOptions={() => ({
          headerShown: false,
        })}
        tabBar={({ navigation, state, descriptors, insets }) => (
          <BottomNavigation.Bar
            navigationState={state}
            safeAreaInsets={insets}
            onTabPress={({ route, preventDefault }) => {
              const event = navigation.emit({
                type: "tabPress",
                target: route.key,
                canPreventDefault: true,
              });

              if (event.defaultPrevented) {
                preventDefault();
              } else {
                navigation.dispatch({
                  ...CommonActions.navigate(route.name, route.params),
                  target: state.key,
                });
              }
            }}
            renderIcon={({ route, focused, color }) => {
              const { options } = descriptors[route.key];
              if (options.tabBarIcon) {
                return options.tabBarIcon({ focused, color, size: 24 });
              }

              return null;
            }}
            getLabelText={({ route }) => {
              const label = route.name;
              return label;
            }}
          />
        )}
      >
        <Tab.Screen
          name="Home"
          component={HomeScreen}
          options={{
            tabBarIcon: ({ color, size }) => {
              return <Ionicons name="home" size={size} color={color} />;
            },
          }}
        />
        <Tab.Screen
          name="Training"
          component={TrainingScreen}
          options={{
            tabBarIcon: ({ color, size }) => {
              return <Ionicons name="baseball" size={size} color={color} />;
            },
          }}
        />
        <Tab.Screen
          name="Calendar"
          component={CalendarScreen}
          options={{
            tabBarIcon: ({ color, size }) => {
              return <Ionicons name="calendar" size={size} color={color} />;
            },
          }}
        />
        <Tab.Screen
          name="MyPage"
          component={MyPageScreen}
          options={{
            tabBarIcon: ({ color, size }) => {
              return <Ionicons name="person" size={size} color={color} />;
            },
          }}
        />
      </Tab.Navigator>
  );
}
