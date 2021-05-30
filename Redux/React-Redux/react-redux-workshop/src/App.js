import React, { Component } from "react";
import "./App.css";
import { connect } from "react-redux";
import ReadContainer from "./containers/ReadContainer";
import Header from "./components/Header";
import NavContainer from "./containers/NavContainer";
import ControlContainer from "./containers/ControlContainer";
import CreateContainer from "./containers/CreateContainer";
import UpdateContainer from "./containers/UpdateContainer";

class App extends Component {
  render() {
    var article = null;
    switch (this.props.mode) {
      case "READ":
        article = <ReadContainer />;
        break;
      case "CREATE":
        article = <CreateContainer />;
        break;
      case "UPDATE":
        article = <UpdateContainer />;
        break;
      default:
        article = <ReadContainer />;
    }
    return (
      <div className="App">
        <Header />
        <NavContainer />
        <ControlContainer />
        {article}
      </div>
    );
  }
}

function mapStateToProps(state) {
  return {
    mode: state.mode,
  };
}

export default connect(mapStateToProps)(App);
