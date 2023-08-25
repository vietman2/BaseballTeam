import { Provider as ReduxProvider } from "react-redux";

import Base from "./components/Account/Base";
//import MainContainer from "./containers/MainContainer";
import { AuthProvider } from "./components/Account/AuthProvider/AuthProvider";
import store from "./store/store";

function App(){
  /*
  useEffect(() => {
    const checkToken = async () => {
      const token = AsyncStorage.getItem("token");
      if(token) {// Check if token is valid
        // If valid, navigate to main container
        return (
          <MainContainer/>
        )
        // If not valid, navigate to login
        return (
          <Login/>
        )
    }
    */

  // 아래는 Temporary
  return (
    <AuthProvider>
      <ReduxProvider store={store}>
        {/* <MainContainer /> */}
        <Base />
      </ReduxProvider>
    </AuthProvider>
  );
}
export default App;