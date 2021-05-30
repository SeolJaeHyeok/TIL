import React, { Component } from "react";

export default class Update extends Component {
  state = {
    title: this.props.title,
    desc: this.props.desc,
    id: this.props.id,
  };

  onChangeHandler(e) {
    this.setState({
      [e.target.name]: e.target.value,
    });
  }

  render() {
    return (
      <form
        onSubmit={function (e) {
          e.preventDefault();
          var id = Number(e.target.id.value);
          var title = e.target.title.value;
          var desc = e.target.desc.value;
          this.props.onSubmit(id, title, desc);
        }.bind(this)}
      >
        <input type="hidden" name="id" value={this.state.id}></input>
        <p>
          <input
            type="text"
            placeholder="title"
            name="title"
            value={this.state.title}
            onChange={this.onChangeHandler.bind(this)}
          />
        </p>
        <p>
          <textarea
            type="text"
            placeholder="description"
            name="desc"
            value={this.state.desc}
            onChange={this.onChangeHandler.bind(this)}
          />
        </p>
        <p>
          <input type="submit" />
        </p>
      </form>
    );
  }
}
