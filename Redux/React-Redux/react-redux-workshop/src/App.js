import "./App.css";
import ArticleContainer from "./containers/ArticleContainer";
import Header from "./components/Header";
import NavContainer from "./containers/NavContainer";

function App() {
  return (
    <div className="App">
      <Header />
      <NavContainer />
      <ArticleContainer />
    </div>
  );
}

export default App;
