import React, { Component } from "react";

class LifeCycleSample extends Component {
  state = {
    number: 0,
    color: null,
  };

  myRef = null; // ref를 설정할 부분

  // 생성자 메서드
  constructor(props) {
    super(props);
    console.log("constructor");
  }

  // props로 받아 온 값을 state에 동기화 시키는 메서드, 컴포넌트가 마운트될 때와 업데이트될 때 호출
  static getDerivedStateFromProps(nextProps, prevState) {
    console.log("getDerivedStateFromProps");
    if (nextProps.color !== prevState.color) {
      return { color: nextProps.color };
    }
    return null;
  }

  // 컴포넌트의 초기 렌더링이 완료된 이후에 호출, state의 변화를 줄 때 사용
  componentDidMount() {
    console.log("componentDidMount");
  }

  // 컴포넌트를 리렌더링 할지 말지를 결정하는 메서드
  shouldComponentUpdate(nextProps, nextState) {
    console.log("shouldComponentUpdate", nextProps, nextState);
    // 숫자의 마지막 자리가 4면 리렌더링하지 않는다.
    return nextState.number % 10 !== 4;
  }

  // 컴포넌트를 DOM에서 제거할 때 사용하는 메서드
  componentWillUnmount() {
    console.log("componentWillUnmount");
  }

  // 클릭했을 때 실행할 함수
  handleClick = () => {
    this.setState({
      number: this.state.number + 1,
    });
  };

  // 주로 업데이트하기 직전의 값을 참고할 일이 있을 때 사용하는 메서드
  getSnapshotBeforeUpdate(prevProps, prevState) {
    console.log("getSnapshotBeforeUpdate");
    if (prevProps.color !== this.props.color) {
      return this.myRef.style.color;
    }
    return null;
  }

  // 리렌더링을 완료한 후에 실행, DOM 관련 처리 무방, 이전에 가졌던 데이터에 접근 가능
  componentDidUpdate(prevProps, prevState, snapshot) {
    console.log("componentDidUpdate", prevProps, prevState);
    if (snapshot) {
      console.log("업데이트되기 직전 색상: ", snapshot);
    }
  }
  // 컴포넌트 모양새 정의, this.props 및 this.state에 접근 가능, 리액트 요소 반환, DOM 접근 불가
  render() {
    console.log("render");

    const style = {
      color: this.props.color,
    };

    return (
      <div>
        {/* 에러 발생 시켜보기 {this.state.missing.value} */}
        <h1 style={style} ref={(ref) => (this.myRef = ref)}>
          {this.state.number}
        </h1>
        <p>color : {this.state.color}</p>
        <button onClick={this.handleClick}>더하기</button>
      </div>
    );
  }
}

export default LifeCycleSample;
