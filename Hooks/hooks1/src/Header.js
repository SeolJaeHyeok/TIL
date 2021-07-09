import React, { useContext } from "react";
import { UserContext } from "./context";

const Header = () => {
  const {
    user: { name, loggedIn },
  } = useContext(UserContext);
  return (
    <header>
      <a href="#">Home</a>Hello, {name} You are{" "}
      {loggedIn ? "logged In" : "anonymous"}
    </header>
  );
};

export default Header;
