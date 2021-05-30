import Control from "../components/Control";
import { connect } from "react-redux";

function mapDispatchToProps(dispatch) {
  return {
    onClick: function (mode) {
      if (mode === "DELETE_PROCESS") {
        if (!window.confirm("Really?")) {
          return;
        }
      }
      dispatch({ type: mode });
    },
  };
}

export default connect(null, mapDispatchToProps)(Control);
