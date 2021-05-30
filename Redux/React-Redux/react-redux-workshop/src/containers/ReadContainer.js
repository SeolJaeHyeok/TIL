import { connect } from "react-redux";
import Read from "../components/Read";

function mapStateToProps(state) {
  var title, desc;

  if (state.mode === "WELCOME") {
    title = state.welcome_content.title;
    desc = state.welcome_content.desc;
  } else {
    for (let i = 0; i < state.contents.length; i++) {
      var d = state.contents[i];
      if (d.id === state.selected_content_id) {
        title = d.title;
        desc = d.desc;
        break;
      }
    }
  }
  return {
    title,
    desc,
  };
}

export default connect(mapStateToProps)(Read);
