import { configureStore, getDefaultMiddleware } from "@reduxjs/toolkit";
import thunk from "redux-thunk";

import authReducer, { login, logout } from "./authSlice";
import { users } from "../../variables/dummy_data";

const createStore = () => {
  return configureStore({
    reducer: {
      auth: authReducer,
    },
    middleware: (getDefaultMiddleware) => getDefaultMiddleware().concat(thunk),
  });
};

describe("authSlice", () => {
  it("should handle initial state", () => {
    expect(authReducer(undefined, { type: "unknown" })).toEqual({
      token: null,
      user: null,
    });
  });

  it("should handle login", async () => {
    const store = createStore();
    const token = "token";
    const user = users[0];

    await store.dispatch(login({ token, user }));

    const state = store.getState().auth;
    expect(state.token).toEqual(token);
    expect(state.user).toEqual(user);
  });

  it("should handle logout", async () => {
    const store = createStore();
    const token = "token";
    const user = users[0];

    await store.dispatch(login({ token, user }));
    await store.dispatch(logout());

    const state = store.getState().auth;
    expect(state.token).toEqual(null);
    expect(state.user).toEqual(null);
  });
});
