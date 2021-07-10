import React from "react";
import { useState } from "../context";
import ToDoForm from "./ToDoForm";
import List from "./List";
import ListItems from "./ListItems";
import Progress from "./Progress";
import Wrapper from "./Wrapper";
import styled from "@emotion/styled";

const Lists = styled.section`
  display: grid;
  grid-template-rows: 50vh;
  grid-template-columns: repeat(2, 1fr);
  column-gap: 30px;
  justify-items: center;
  @media (max-width: 768px) {
    width: 70%;
    grid-auto-flow: column;
    grid-template-columns: 1fr;
    grid-template-rows: repeat(2, 1fr);
    justify-items: start;
  }
  @media (max-width: 414px) {
    width: 95%;
  }
`;

function App() {
  const { toDos, completed } = useState();

  return (
    <Wrapper>
      <ToDoForm />
      <Progress />

      <Lists>
        <List title={toDos.length > 0 ? "To Dos" : ""}>
          {toDos.map((toDo) => (
            <ListItems key={toDo.id} id={toDo.id} text={toDo.text} />
          ))}
        </List>
        <List title={completed.length > 0 ? "Completed!" : ""}>
          {completed.map((complete) => (
            <ListItems
              key={complete.id}
              id={complete.id}
              text={complete.text}
              isCompleted
            />
          ))}
        </List>
      </Lists>
    </Wrapper>
  );
}

export default App;
