import { Provider as ReduxProvider } from "react-redux";

import store from "./store/store";
import RootContainer from "./containers/RootContainer";

function App() {
  return <ReduxProvider store={store}>
    <RootContainer />
  </ReduxProvider>;
}
export default App;
