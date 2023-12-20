import { NavigationContainer } from "@react-navigation/native";
import { createNativeStackNavigator } from "@react-navigation/native-stack";

import Tabs from "./tabs/Tabs";
import Login from "../containers/Login/Login";
import SignUp from "../containers/SignUp/SignUp";
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
      </RootStack.Navigator>
    </NavigationContainer>
  );
}
