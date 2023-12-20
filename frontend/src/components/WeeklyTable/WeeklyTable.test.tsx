import { render } from "@testing-library/react-native";

import WeeklyTable from "./WeeklyTable";

describe("<WeeklyTable />", () => {
  it("should render correctly", () => {
    render(<WeeklyTable />);
  });

  it("should return data correctly", () => {
    const { getByText } = render(<WeeklyTable />);
  });
});
