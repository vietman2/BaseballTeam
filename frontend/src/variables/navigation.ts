import { CompositeScreenProps } from "@react-navigation/native";
import { StackScreenProps } from "@react-navigation/stack";

/** 가장 바깥 Navigation 담당 */
export type RootStackParamList = {
  Login: undefined;
  SignUp: undefined;
  SignUp2: undefined;
  Main: undefined;
};
export type RootStackScreenProps<T extends keyof RootStackParamList> =
  StackScreenProps<RootStackParamList, T>;

/** 하단 탭 Navigation 담당 */
export type BottomTabParamList = {
  Home: undefined;
  Training: undefined;
  MyPage: undefined;
  Calendar: undefined;
};
export type BottomTabScreenProps<T extends keyof BottomTabParamList> =
  CompositeScreenProps<
    StackScreenProps<BottomTabParamList, T>,
    RootStackScreenProps<"Main">
  >;
