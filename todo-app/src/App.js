import "./App.css";
import ToDoInsert from "./components/ToDoInsert";
import ToDoLIst from "./components/ToDoList";
import ToDoTemplate from "./components/ToDoTemplate";

const App = () => {
  return (
    <ToDoTemplate>
      <ToDoInsert />
      <ToDoLIst />
    </ToDoTemplate>
  );
};

export default App;
