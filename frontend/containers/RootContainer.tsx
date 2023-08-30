import { NavigationContainer } from "@react-navigation/native";
import { createNativeStackNavigator } from "@react-navigation/native-stack";

import AccountContainer from "../containers/AccountContainer";
import MainContainer from "../containers/MainContainer";
import { AuthProvider } from "../components/Account/AuthProvider/AuthProvider";

export type RootStackParamList = {
  Account: undefined;
  Main: undefined;
};

const RootStack = createNativeStackNavigator<RootStackParamList>();

export default function RootContainer() {
    return (
      <AuthProvider>
        <NavigationContainer>
          <RootStack.Navigator
            initialRouteName="Account"
            screenOptions={{
              headerShown: false,
            }}
          >
            
            <RootStack.Screen name="Account" component={AccountContainer} />
            <RootStack.Screen name="Main" component={MainContainer} />
          </RootStack.Navigator>
        </NavigationContainer>
      </AuthProvider>
    );
    }
    