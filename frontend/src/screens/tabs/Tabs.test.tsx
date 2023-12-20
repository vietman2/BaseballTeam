import { NavigationContainer } from "@react-navigation/native";

import Tabs from "./Tabs";
import { renderWithProviders } from "../../test-utils/test-utils";

jest.mock("react-native-vector-icons/MaterialCommunityIcons", () => "Icon");
jest.mock("react-native-gesture-handler", () => ({
  PanGestureHandler: "PanGestureHandler",
}));
jest.mock("./Home/Home", () => "Home");
jest.mock("./Training/Training", () => "Training");
jest.mock("./MyPage/MyPage", () => "MyPage");
jest.mock("./Calendar/Calendar", () => "Calendar");

describe("Tabs", () => {
  it("renders correctly", () => {
    renderWithProviders(
      <NavigationContainer>
        <Tabs />
      </NavigationContainer>
    );
  });
});
