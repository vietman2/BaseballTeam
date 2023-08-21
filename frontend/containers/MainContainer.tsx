import { NavigationContainer } from "@react-navigation/native";
import { createBottomTabNavigator } from "@react-navigation/bottom-tabs";

import HomeScreen from "../components/Home/Home";
import TrainingScreen from "../components/Training/Training";
import MyPageScreen from "../components/MyPage/MyPage";
import CalendarScreen from "../components/Calendar/Calendar";

export type RootTabParamList = {
    Home: undefined;
    Training: undefined;
    MyPage: undefined;
    Calendar: undefined;
};

const Tab = createBottomTabNavigator<RootTabParamList>();

export default function MainContainer() {
    return (
        <NavigationContainer>
            <Tab.Navigator
                initialRouteName="Home"
                screenOptions={({ route }) => ({
                    headerShown: false,
                })}
            >
                <Tab.Screen name="Home" component={HomeScreen} />
                <Tab.Screen name="Training" component={TrainingScreen} />
                <Tab.Screen name="MyPage" component={MyPageScreen} />
                <Tab.Screen name="Calendar" component={CalendarScreen} />
            </Tab.Navigator>
        </NavigationContainer>
    );
}
