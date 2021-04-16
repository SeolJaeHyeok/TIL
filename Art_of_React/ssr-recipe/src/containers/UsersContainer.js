import React, { useEffect } from "react";
import Users from "../components/Users";
import { connect } from "react-redux";
import { getUsers } from "../modules/users";

const UsersContainer = ({ users, getUsers }) => {
  // 컴포넌트가 마운트 되고 나서 호출
  useEffect(() => {
    if (users) return; // users가 이미 유효하다면 요청하지 않음
    getUsers();
  }, [getUsers, users]);
  return <Users users={users} />;
};

export default connect(
  // 익명 함수 형태로 connect 안에서 mapStateToProps 함수 바로 구현
  (state) => ({
    users: state.users.users,
  }),
  {
    // mapDispatchToProps 따로 정의하지 않고 액션 생성 함수로 이루어진 객체 넣어 주기
    // 이렇게 하면 connect 함수가 내부적으로 bindActionCreators 작업을 대신 해준다.
    getUsers,
  }
)(UsersContainer);
