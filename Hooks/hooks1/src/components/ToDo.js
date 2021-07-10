import React from "react";
import { COMPLETE, DEL, UNCOMPLETE } from "../actions";
import { useDispatch } from "../context";

export default ({ text, id, isCompleted }) => {
  const dispatch = useDispatch();
  return (
    <>
      <li>
        <span>{text}</span>
        <button onClick={() => dispatch({ type: DEL, payload: id })}>❌</button>
        <button
          onClick={() =>
            dispatch({ type: isCompleted ? UNCOMPLETE : COMPLETE, payload: id })
          }
        >
          {isCompleted ? "🙅‍♂️" : "✅"}
        </button>
      </li>
    </>
  );
};
