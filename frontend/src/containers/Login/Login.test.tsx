import { act, fireEvent } from "@testing-library/react-native";
import { NavigationContainer } from "@react-navigation/native";
import { createStackNavigator } from "@react-navigation/stack";

import Login from "./Login";
import { renderWithProviders } from "../../test-utils/test-utils";

jest.mock("react-native-gesture-handler", () => ({
  PanGestureHandler: "PanGestureHandler",
}));

const Stack = createStackNavigator();

const render = () => {
  return renderWithProviders(
    <NavigationContainer>
      <Stack.Navigator>
        <Stack.Screen name="Login" component={Login} />
      </Stack.Navigator>
    </NavigationContainer>
  );
};

describe("<Login />", () => {
  it("should render Login component", () => {
    render();
  });

  it("should handle Login", async () => {
    const { getByText } = render();

    const loginButton = getByText("로그인");

    await act(async () => {
      fireEvent.press(loginButton);
    });
  });

  it("should handle Register", async () => {
    const { getByText } = render();

    const registerButton = getByText("회원가입");

    await act(async () => {
      fireEvent.press(registerButton);
    });
  });

  it("should handle change texts", async () => {
    const { getByPlaceholderText } = render();

    const username = getByPlaceholderText("아이디");
    const password = getByPlaceholderText("비밀번호");

    await act(async () => {
      fireEvent.changeText(username, "test");
      fireEvent.changeText(password, "test");
    });
  });
});
