import RootScreens from "./RootScreens";
import { renderWithProviders } from "../test-utils/test-utils";

jest.mock("react-native-vector-icons/MaterialCommunityIcons", () => "Icon");
jest.mock("react-native-gesture-handler", () => ({
  PanGestureHandler: "PanGestureHandler",
}));
jest.mock("../containers/Login/Login", () => "Login");
jest.mock("../containers/SignUp/SignUp", () => "SignUp");

describe("RootScreens", () => {
  it("renders correctly", () => {
    renderWithProviders(<RootScreens />);
  });
});
