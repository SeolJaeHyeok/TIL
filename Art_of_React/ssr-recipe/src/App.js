import React from "react";
import { Route } from "react-router-dom";
import RedPage from "./pages/RedPage";
import BluePage from "./pages/BluePage";
import Menu from "./components/Menu";
import UserPage from "./pages/UsersPage";

function App() {
  return (
    <div>
      <Menu />
      <hr />
      <Route path="/red" component={RedPage} />
      <Route path="/blue" component={BluePage} />
      <Route path="/users" component={UserPage} />
    </div>
  );
}

export default App;
