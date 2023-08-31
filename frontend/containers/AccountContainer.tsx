import { createNativeStackNavigator } from "@react-navigation/native-stack";

import Login from "../components/Account/Login";
import SignUp from "../components/Account/SignUp";
import SignUp2 from "../components/Account/SignUp2";

export type AuthStackParamList = {
  Login: undefined;
  SignUp: undefined;
  SignUp2: undefined;
};

const AuthStack = createNativeStackNavigator<AuthStackParamList>();

export default function AuthContainer() {
  return (
      <AuthStack.Navigator
        initialRouteName="Login"
        screenOptions={{
          headerShown: false,
        }}
      >
        <AuthStack.Screen name="Login" component={Login} />
        <AuthStack.Screen name="SignUp" component={SignUp} />
        <AuthStack.Screen name="SignUp2" component={SignUp2} />
      </AuthStack.Navigator>
  );
}
