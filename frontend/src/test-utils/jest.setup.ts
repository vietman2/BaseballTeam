import mockSafeAreaContext from "react-native-safe-area-context/jest/mock";

jest.mock("react-native/Libraries/Animated/NativeAnimatedHelper");
jest.mock("react-native/Libraries/Animated/Easing");
jest.mock("react-native/Libraries/Animated/animations/TimingAnimation");
jest.mock("react-native-gesture-handler", () => ({
  createGestureHandler: jest.fn(),
  dropGestureHandler: jest.fn(),
  GestureHandlerRootView: jest.fn(),
}));
jest.mock("react-native-safe-area-context", () => mockSafeAreaContext);
jest.mock("axios")
