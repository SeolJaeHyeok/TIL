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
  switch (action.type) {
    case "WELCOME":
      return {
        ...state,
        mode: "WELCOME",
      };
    case "READ":
      return {
        ...state,
        mode: "READ",
        selected_content_id: parseInt(action.id),
      };
    case "CREATE":
      return {
        ...state,
        mode: "CREATE",
      };
    case "CREATE_PROCESS":
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
    case "UPDATE":
      return {
        ...state,
        mode: "UPDATE",
      };
    case "UPDATE_PROCESS":
      var updatedContent = [...state.contents];
      for (let i = 0; i < updatedContent.length; i++) {
        if (updatedContent[i].id === action.id) {
          updatedContent[i].title = action.title;
          updatedContent[i].desc = action.desc;
        }
      }
      return {
        ...state,
        contents: updatedContent,
        mode: "READ",
        selected_content_id: action.id,
      };
    case "DELETE_PROCESS":
      var deletedContents = state.contents.filter((content) => {
        if (content.id === state.selected_content_id) {
          return false;
        }
        return true;
      });
      return {
        ...state,
        contents: deletedContents,
        mode: "WELCOME",
      };
    default:
      return state;
  }
}

export default createStore(
  reducer,
  window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__()
);
