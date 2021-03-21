import React, { useCallback, useState } from "react";
import { MdAdd } from "react-icons/md";
import "./ToDoInsert.scss";

const ToDoInsert = ({ onInsert }) => {
  const [value, setValue] = useState("");

  const onChange = useCallback((e) => {
    setValue(e.target.value);
  }, []);

  const onSubmit = useCallback(
    (e) => {
      onInsert(value);
      setValue(""); // value 값 초기화
      // submit이벤트는 브라우저를 새로고침 한다.
      // 이를 방지하기 위해 preventDefault 함수를 호출한다.
      e.preventDefault();
    },
    [onInsert, value]
  );

  return (
    <form className="ToDoInsert" onSubmit={onSubmit}>
      <input
        placeholder="할 일을 입력하세요."
        value={value}
        onChange={onChange}
      />
      <button type="submit">
        <MdAdd />
      </button>
    </form>
  );
};

export default ToDoInsert;
