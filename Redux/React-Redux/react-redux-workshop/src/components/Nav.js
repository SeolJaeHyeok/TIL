import React, { Component } from "react";

export default class Nav extends Component {
  render() {
    var tags = [];
    var data = this.props.data;
    for (let i = 0; i < data.length; i++) {
      var d = data[i];
      tags.push(
        <li key={d.id}>
          <a
            href={`#${d.title}`}
            data-id={d.id}
            onClick={function (e) {
              this.props.onClick(e.target.dataset.id);
            }.bind(this)}
          >
            {d.title}
          </a>
        </li>
      );
    }
    return (
      <nav>
        <ol>{tags}</ol>
      </nav>
    );
  }
}
