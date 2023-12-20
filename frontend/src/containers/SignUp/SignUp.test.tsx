import { act, fireEvent } from "@testing-library/react-native";
import { NavigationContainer } from "@react-navigation/native";
import { createStackNavigator } from "@react-navigation/stack";

import SignUp from "./SignUp";
import { renderWithProviders } from "../../test-utils/test-utils";

jest.mock("react-native-gesture-handler", () => ({
  PanGestureHandler: "PanGestureHandler",
}));

const Stack = createStackNavigator();

const render = () => {
  return renderWithProviders(
    <NavigationContainer>
      <Stack.Navigator>
        <Stack.Screen name="SignUp" component={SignUp} />
        <Stack.Screen name="Main" component={SignUp} />
      </Stack.Navigator>
    </NavigationContainer>
  );
};

describe("<SignUp />", () => {
  it("should render SignUp component", () => {
    render();
  });

  it("should handle SignUp", async () => {
    const { getByText } = render();

    const signUpButton = getByText("가입하기");
    
    await act(async () => {
        fireEvent.press(signUpButton);
        });
  });

  it("should handle change texts", async () => {
    const { getByPlaceholderText } = render();

    const username = getByPlaceholderText("아이디");
    const phoneNumber = getByPlaceholderText("전화번호");
    const password = getByPlaceholderText("비밀번호");
    const passwordCheck = getByPlaceholderText("비밀번호 확인");

    await act(async () => {
      fireEvent.changeText(username, "test");
      fireEvent.changeText(phoneNumber, "01012345678");
      fireEvent.changeText(password, "test");
      fireEvent.changeText(passwordCheck, "test");
    });
  });
});
