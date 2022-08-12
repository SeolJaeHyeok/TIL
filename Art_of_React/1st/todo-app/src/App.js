import { useCallback, useReducer, useRef } from "react";
import "./App.css";
import ToDoInsert from "./components/ToDoInsert";
import ToDoLIst from "./components/ToDoList";
import ToDoTemplate from "./components/ToDoTemplate";

function createBulkTodos() {
  const array = [];

  for (let i = 1; i <= 10; i++) {
    array.push({
      id: i,
      text: `할 일 ${i}`,
      checked: false,
    });
  }
  return array;
}

function todoReducer(todos, action) {
  switch(action.type) {
    case 'INSERT':
      return todos.concat(action.todo)
    case 'REMOVE':
      return todos.filter(todo => todo.id !== action.id)
    case 'TOGGLE':
      return todos.map(todo => todo.id === action.id ? {...todo, checked: !todo.checked} : todo)
    default: 
      return todos;
  }
}

const App = () => {
  const initialState = createBulkTodos();
  const [todos, dispatch] = useReducer(todoReducer, initialState);

  // 고윳값으로 사용될 id
  // ref를 사용하여 변수 담기
  const nextId = useRef(2501);

  const onInsert = useCallback((text) => {
    const todo = {
      id: nextId.current,
      text,
      checked: false
    };
    dispatch({type: "INSERT", todo})
    nextId.current += 1;
  }, []);

  const onRemove = useCallback((id) => {
    dispatch({ type: "REMOVE", id });
  }, []);

  const onToggle = useCallback((id) => {
    dispatch({ type: "TOGGLE", id });
  }, []);

  return (
    <ToDoTemplate>
      <ToDoInsert onInsert={onInsert} />
      <ToDoLIst todos={todos} onRemove={onRemove} onToggle={onToggle} />
    </ToDoTemplate>
  );
};

export default App;
