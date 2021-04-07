import { combineReducers } from "redux";
import counter from "./couter";

const rootReducer = combineReducers({
  counter,
});

export default rootReducer;
