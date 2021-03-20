import React from "react";
import { MdAdd } from "react-icons/md";
import "./ToDoInsert.scss";

const ToDoInsert = () => {
  return (
    <form className="ToDoInsert">
      <input placeholder="할 일을 입력하세요." />
      <button type="submit">
        <MdAdd />
      </button>
    </form>
  );
};

export default ToDoInsert;
