import Calendar from "./Calendar";
import { renderWithProviders } from "../../../test-utils/test-utils";

describe("<Calendar />", () => {
  it("should render Calendar", () => {
    renderWithProviders(<Calendar />);
  });
});
