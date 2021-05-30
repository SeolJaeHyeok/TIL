import { connect } from "react-redux";
import Create from "../components/Create";

function mapDispatchToProps(dispatch) {
  return {
    onSubmit: function (title, desc) {
      dispatch({ type: "CREATE_PROCESS", title, desc });
    },
  };
}

export default connect(null, mapDispatchToProps)(Create);
