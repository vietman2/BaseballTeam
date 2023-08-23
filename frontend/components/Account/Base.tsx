import { NavigationContainer } from "@react-navigation/native";
import { createNativeStackNavigator } from "@react-navigation/native-stack";

import Login from "./Login";
import SignUp from "./SignUp";

export type AuthStackParamList = {
  Login: undefined;
  SignUp: undefined;
};

const AuthStack = createNativeStackNavigator<AuthStackParamList>();

export default function AuthContainer() {
  return (
    <NavigationContainer>
      <AuthStack.Navigator
        initialRouteName="Login"
        screenOptions={{
          headerShown: false,
        }}
      >
        {<AuthStack.Screen name="Login" component={Login} />}
        {<AuthStack.Screen name="SignUp" component={SignUp} />}
      </AuthStack.Navigator>
    </NavigationContainer>
  );
}
