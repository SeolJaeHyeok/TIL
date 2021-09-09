import React, { useCallback } from "react";
import { List } from "react-virtualized";
import ToDoListItem from "./ToDoListItem";
import "./ToDoList.scss";

const ToDoLIst = ({ todos, onRemove, onToggle }) => {
  const rowRenderer = useCallback(
    ({ index, key, style }) => {
      const todo = todos[index];
      return (
        <ToDoListItem
          todo={todo}
          key={key}
          onRemove={onRemove}
          onToggle={onToggle}
          style={style}
        />
      );
    },
    [todos, onRemove, onToggle]
  );

  return (
    <List
      className="ToDoList"
      width={512} // 전체 크기
      height={513} // 전체 높이
      rowCount={todos.length} // 항목 개수
      rowHeight={57} // 항목 높이
      rowRenderer={rowRenderer} // 항목을 렌더링할 때 쓰는 함수
      list={todos} // 배열
      style={{ outline: "none" }} // 리스트에 기본 적용되는 outline 스타일 제거
    />
  );
};

export default React.memo(ToDoLIst);
