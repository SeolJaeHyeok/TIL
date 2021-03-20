import React from "react";
import ToDoListItem from "./ToDoListItem";
import "./ToDoList.scss";

const ToDoLIst = () => {
  return (
    <div className="ToDoList">
      <ToDoListItem />
      <ToDoListItem />
      <ToDoListItem />
    </div>
  );
};

export default ToDoLIst;
