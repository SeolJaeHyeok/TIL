import React, { Component } from "react";

class Counter extends Component {
  constructor(props) {
    super(props);
    // state의 초깃값 설정
    this.state = {
      number: 0,
      fixedNumber: 0,
    };
  }
  render() {
    const { number, fixedNumber } = this.state; // state를 조회할 때는 this.state로 조회
    return (
      <div>
        <h1>{number}</h1>
        <h1>바뀌는 않는 숫자 : {fixedNumber}</h1>
        <button
          // onClick을 통해 버튼이 클릭되었을 때 호출할 함수 지정
          onClick={() => {
            this.setState((prevState) => {
              return {
                number: prevState.number + 1,
              };
            });
            // 위 코드는 아래 코드와 똑같은 기능
            // 아래 코드는 함수에서 바로 객체를 반환한다는 의미
            this.setState(
              (prevState) => ({
                number: prevState.number + 1,
              }),
              // 콜백 함수 등록해서 this.setState가 끝난 후 특정 작업 실행
              () => {
                console.log("방금 setState가 호출되었습니다.");
                console.log(this.state);
              }
            );
          }}
        >
          Add
        </button>
      </div>
    );
  }
}

export default Counter;
