import React from "react";
import { MdCheckBoxOutlineBlank, MdRemoveCircleOutline } from "react-icons/md";
import "./ToDoListItem.scss";

const ToDoListItem = () => {
  return (
    <div className="ToDoListItem">
      <div className="checkbox">
        <MdCheckBoxOutlineBlank />
        <div className="text">할 일</div>
      </div>
      <div className="remove">
        <MdRemoveCircleOutline />
      </div>
    </div>
  );
};

export default ToDoListItem;
