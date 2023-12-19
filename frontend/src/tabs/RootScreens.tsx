import { NavigationContainer } from "@react-navigation/native";
import { createNativeStackNavigator } from "@react-navigation/native-stack";

import Tabs from "./Tabs";
import Login from "../components/Account/Login";
import SignUp from "../components/Account/SignUp";
import SignUp2 from "../components/Account/SignUp2";
import { RootStackParamList } from "../variables/navigation";

const RootStack = createNativeStackNavigator<RootStackParamList>();

export default function RootScreens() {
  return (
    <NavigationContainer>
      <RootStack.Navigator
        initialRouteName="Login"
        screenOptions={{
          headerShown: false,
        }}
      >
        <RootStack.Screen name="Main" component={Tabs} />
        <RootStack.Screen name="Login" component={Login} />
        <RootStack.Screen name="SignUp" component={SignUp} />
        <RootStack.Screen name="SignUp2" component={SignUp2} />
      </RootStack.Navigator>
    </NavigationContainer>
  );
}
