import React, { Component } from "react";

export default class Create extends Component {
  render() {
    return (
      <form
        onSubmit={function (e) {
          e.preventDefault();
          var title = e.target.title.value;
          var desc = e.target.desc.value;
          this.props.onSubmit(title, desc);
        }.bind(this)}
      >
        <p>
          <input type="text" placeholder="title" name="title" />
        </p>
        <p>
          <textarea type="text" placeholder="description" name="desc" />
        </p>
        <p>
          <input type="submit" />
        </p>
      </form>
    );
  }
}
