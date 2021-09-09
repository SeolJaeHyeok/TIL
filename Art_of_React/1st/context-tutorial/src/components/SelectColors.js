import React, { Component } from "react";
import ColorContext from "../contexts/color";

const colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"];

class SelectColors extends Component {
  static contextType = ColorContext;

  handleSetColor = (color) => {
    this.state.actions.setColor(color);
  };

  handleSetSubcolor = (color) => {
    this.state.actions.setSubcolor(color);
  };

  render() {
    return (
      <div>
        <h2>색상을 선택하세요.</h2>

        {({ actions }) => (
          <div style={{ display: "flex" }}>
            {colors.map((color) => (
              <div
                key={color}
                style={{
                  background: color,
                  width: "24px",
                  height: "24px",
                  cursor: "pointer",
                }}
                onClick={this.handleSetColor(color)}
                onContextMenu={(e) => {
                  e.preventDefault(); // 마우스 오른쪽 클릭 시 메뉴가 뜨는 것을 무시함
                  this.handleSetSubcolor(color);
                }}
              />
            ))}
          </div>
        )}

        <hr />
      </div>
    );
  }
}

export default SelectColors;
