import axios from "axios";

import { login } from "./account";

jest.mock("@react-native-async-storage/async-storage", () => ({
  setItem: jest.fn(),
  getItem: jest.fn(),
  removeItem: jest.fn(),
}));

describe("Accounts Service", () => {
  it("should login and return tokens", async () => {
    jest.spyOn(axios, "post").mockImplementation(() =>
      Promise.resolve({
        data: {
          access_token: "token",
          refresh_token: "token",
        },
      })
    );
    const email = "email";
    const password = "password";
    await login(email, password);
  });

  it("should handle login error", async () => {
    jest.spyOn(axios, "post").mockImplementation(() =>
      Promise.reject({
        response: {
          data: {
            message: "error",
          },
        },
      })
    );
    const email = "email";
    const password = "password";
    await login(email, password);
  });
});
