import "./App.css";
import Article from "./components/article";
import Header from "./components/Header";
import NavContainer from "./containers/NavContainer";

function App() {
  return (
    <div className="App">
      <Header />
      <NavContainer />
      <Article />
    </div>
  );
}

export default App;
