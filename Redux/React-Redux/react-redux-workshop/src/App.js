import "./App.css";
import ArticleContainer from "./containers/ArticleContainer";
import Header from "./components/Header";
import NavContainer from "./containers/NavContainer";
import ControlContainer from "./containers/ControlContainer";

function App() {
  return (
    <div className="App">
      <Header />
      <NavContainer />
      <ControlContainer />
      <ArticleContainer />
    </div>
  );
}

export default App;
