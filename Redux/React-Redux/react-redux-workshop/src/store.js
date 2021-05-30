import { createStore } from "redux";

var initState = {
  mode: "WELCOME",
  welcome_content: {
    title: "WEB",
    desc: "Hello, WEB",
  },
  selected_content_id: 1,
  max_contents_id: 3,
  contents: [
    { id: 1, title: "HTML", desc: "HTML is ..." },
    { id: 2, title: "CSS", desc: "CSS is ..." },
    { id: 3, title: "JS", desc: "JS is ..." },
  ],
};

function reducer(state = initState, action) {
  if (action.type === "WELCOME") {
    return {
      ...state,
      mode: "WELCOME",
    };
  }
  if (action.type === "READ") {
    return {
      ...state,
      mode: "READ",
      selected_content_id: parseInt(action.id),
    };
  }
  if (action.type === "CREATE") {
    return {
      ...state,
      mode: "CREATE",
    };
  }
  if (action.type === "CREATE_PROCESS") {
    var newId = state.max_contents_id + 1;
    var newContents = [
      ...state.contents,
      { id: newId, title: action.title, desc: action.desc },
    ];
    return {
      ...state,
      contents: newContents,
      max_contents_id: newId,
      mode: "READ",
      selected_content_id: newId,
    };
  }
  return state;
}

export default createStore(
  reducer,
  window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__()
);
