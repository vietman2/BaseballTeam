import { useEffect } from "react";
import AsyncStorage from "@react-native-async-storage/async-storage";
import { Provider as ReduxProvider } from "react-redux";

import MainContainer from "./navigation/MainContainer"
import Login from "./components/Login/Login";
import { AuthProvider } from "./components/AuthProvider/AuthProvider";
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
  return(
    <AuthProvider>
      <ReduxProvider store={store}>
        <Login/>
      </ReduxProvider>
    </AuthProvider>
    
    // <MainContainer/>
  );
}
export default App;