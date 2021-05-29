import { createStore } from "redux";

let initState = {
  mode: "WELCOME",
  welcome_content: {
    title: "WEB",
    desc: "Hello, WEB",
  },
  selected_content_id: 1,
  content: [
    { id: 1, title: "HTML", desc: "HTML is ..." },
    { id: 2, title: "CSS", desc: "CSS is ..." },
    { id: 3, title: "JS", desc: "JS is ..." },
  ],
};

function reducer(state = initState, action) {
  return state;
}

export default createStore(reducer);
