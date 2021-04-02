import { combineReducers } from "redux";
import counter from "./counter";
import todos from "./todos";

const routeReducer = combineReducers({
  counter,
  todos,
});

export default routeReducer;
