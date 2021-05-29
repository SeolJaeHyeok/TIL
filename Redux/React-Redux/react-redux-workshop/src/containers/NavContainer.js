import { connect } from "react-redux";
import Nav from "../components/Nav";

function mapStateToProps(state) {
  return {
    data: state.contents,
  };
}

function mapDispatchToProps(dispatch) {
  return {
    onClick: function (id) {
      dispatch({ type: "READ", id });
    },
  };
}

export default connect(mapStateToProps, mapDispatchToProps)(Nav);
