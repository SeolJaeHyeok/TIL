import React, { useState } from "react";
import { DEL, COMPLETE, UNCOMPLETE, EDIT } from "../actions";
import Svgs from "./Svgs";
import { useDispatch } from "../context";
import styled from "@emotion/styled";

const Li = styled.li`
  display: flex;
  padding-left: 10px;
  margin-bottom: 5px;
`;

const Dot = styled.span`
  color: #86d3dd;
  font-size: 10px;
  margin-right: 10px;
`;

const Todo = styled.input`
  all: unset;
  padding: 5px 0;
`;
const Completed = styled.input`
  all: unset;
  padding: 5px 0;
  text-decoration: line-through;
  color: rgba(127, 140, 141, 0.8);
`;

const Button = styled.button`
  all: unset;
  margin-left: 10px;
  cursor: pointer;
  :hover {
    svg {
      stroke-width: 1.5px;
    }
  }
`;
const ButtonBack = styled.button`
  all: unset;
  margin-left: 65px;
  cursor: pointer;
  :hover {
    svg {
      stroke-width: 1.5px;
    }
  }
`;

export default ({ id, text, isCompleted }) => {
  const [editedToDo, setEditedToDo] = useState(text);
  const dispatch = useDispatch();

  const onChange = (e) => {
    const {
      target: { value },
    } = e;
    setEditedToDo(value);
  };
  const onSubmit = (e) => {
    e.preventDefault();
    const { target } = e;
    dispatch({ type: EDIT, payload: target[0].value, id });
    target[0].disabled = true;
  };

  const editHandler = (e) => {
    const { target } = e;
    switch (target.nodeName) {
      case "BUTTON":
        const input = target.previousSibling[0];
        input.disabled = false;
        input.focus();
        break;
      case "svg":
        const inputA = target.parentNode.previousSibling[0];
        inputA.disabled = false;
        inputA.focus();
        break;
      case "path":
        const inputB = target.parentNode.parentNode.previousSibling[0];
        inputB.disabled = false;
        inputB.focus();
        break;
      default:
        return;
    }
  };

  return (
    <>
      <Li key={id}>
        <form onSubmit={onSubmit}>
          <Dot>●</Dot>
          {!isCompleted ? (
            <Todo type="text" value={editedToDo} onChange={onChange} disabled />
          ) : (
            <Completed
              type="text"
              value={editedToDo}
              onChange={onChange}
              disabled
            />
          )}
        </form>
        {!isCompleted ? (
          <>
            <Button onClick={editHandler}>
              <Svgs.Edit />
            </Button>
            <Button onClick={() => dispatch({ type: DEL, payload: id })}>
              <Svgs.Delete />
            </Button>
            <Button onClick={() => dispatch({ type: COMPLETE, payload: id })}>
              <Svgs.Check />
            </Button>
          </>
        ) : (
          <>
            <ButtonBack
              onClick={() => dispatch({ type: UNCOMPLETE, payload: id })}
            >
              <Svgs.Back />
            </ButtonBack>
          </>
        )}
      </Li>
    </>
  );
};
