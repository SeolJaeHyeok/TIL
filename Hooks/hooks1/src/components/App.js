import React from "react";
import { useState } from "../context";
import Add from "./Add";
import List from "./List";
import ToDo from "./ToDo";

function App() {
  const { toDos, completed } = useState();
  return (
    <>
      <Add />
      <List name={"To Dos"}>
        {toDos.map((toDo) => (
          <ToDo key={toDo.id} text={toDo.text} id={toDo.id} />
        ))}
      </List>
      <List name={completed.length !== 0 ? "Completed" : ""}>
        {completed.map((toDo) => (
          <ToDo
            key={toDo.id}
            text={toDo.text}
            id={toDo.id}
            isCompleted={true}
          />
        ))}
      </List>
    </>
  );
}

export default App;
