import { PropsWithChildren, ReactElement } from "react";
import { Provider } from "react-redux";
import { PaperProvider } from "react-native-paper";
import { SafeAreaProvider } from "react-native-safe-area-context";
import { PreloadedState } from "@reduxjs/toolkit";
import { render, RenderOptions } from "@testing-library/react-native";

import { RootState, AppStore } from "../store/store";
import { setupStore } from "../store/slices/index";

interface ExtendedRenderOptions extends Omit<RenderOptions, "queries"> {
  preloadedState?: PreloadedState<RootState>;
  store?: AppStore;
}

export function renderWithProviders(
  ui: ReactElement,
  {
    preloadedState = {},
    store = setupStore(preloadedState),
    ...renderOptions
  }: ExtendedRenderOptions = {}
) {
  function Wrapper({ children }: PropsWithChildren): JSX.Element {
    return (
      <Provider store={store}>
        <PaperProvider>
          <SafeAreaProvider>{children}</SafeAreaProvider>
        </PaperProvider>
      </Provider>
    );
  }

  return { store, ...render(ui, { wrapper: Wrapper, ...renderOptions }) };
}
