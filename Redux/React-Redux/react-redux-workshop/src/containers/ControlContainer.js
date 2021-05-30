import Control from "../components/Control";
import { connect } from "react-redux";

function mapDispatchToProps(dispatch) {
  return {
    onClick: function (mode) {
      dispatch({ type: mode });
    },
  };
}

export default connect(null, mapDispatchToProps)(Control);
