import { Provider as ReduxProvider } from "react-redux";

import store from "./src/store/store";
import RootScreens from "./src/tabs/RootScreens";

function App() {
  return (
    <ReduxProvider store={store}>
      <RootScreens />
    </ReduxProvider>
  );
}
export default App;
