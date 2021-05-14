import React, { Component } from "react";
import DisplayNumber from "../components/DispalyNumber";
import store from "../store";

export default class DisplayNumberContainer extends Component {
  state = { number: store.getState().number };
  constructor(props) {
    super(props);
    store.subscribe(
      function () {
        this.setState({ number: store.getState().number });
      }.bind(this)
    );
  }
  render() {
    return <DisplayNumber number={this.state.number} />;
  }
}
