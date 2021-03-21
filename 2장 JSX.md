# 2021.03.03

## 2.1 코드 이해하기

```react
import React from "react";
import logo from "./logo.svg";
import "./App.css";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;

```

리액트 프로젝트를 생성했을 때 만들어지는 여러 파일 중 src/App.js의 전체 코드이다.

위 전체 코드를 분리하여 설명을 해보자면 

```react
import React from 'react';
```

- 위 코드는 리액트를 불러와서 사용할 수 있게 해줍니다. 리액트 프로젝트를 만들 때 node_modules 디렉토리도 함께 생성이 되는데 node_modules 디렉토리 안에 react 모듈이 설치가 되고 import를 통해 불러와서 사용할 수 있게 되는 것이다.

- 여기서 한 가지 알아 둘 점은 이렇게 모듈을 불러와서 사용하는 것은 원래 브라우저에는 없던 기능인데 이처럼 브라우저가 아닌 환경에서 자바스크립트를 실행할 수 있게 해 주는 환경인 Node.js에서 지원하는 기능이다. 

  (참고로 Node.js에서는 import가 아닌 require라는 구문으로 패키지를 불러 올 수 있다.)

- 이러한 기능을 브라우저에서도 사용하기 위해 번들러(bundler)를 사용한다. bundle을 묶는다는 뜻으로 즉 파일(모듈)을 묶듯이 연결하는 것을 말한다.

- 이러한 번들러로는 대표적으로 웹팩, Parcel, browserify라는 도구들이 있으며 리액트에서는 편의성과 확장성이 다른 도구보다 뛰어나기 때문에 웹팩을 사용하는 추세다.

- 번들러 도구를 사용하면 import로 모듈을 불러왔을 때 불러온 모듈을 모두 합쳐서 하나의 파일을 생성해 주고 또 최적화 과정에서 여러 개의 파일로 분리 될 수도 있다.

``` react
import logo from './logo.svg';
import './App.css';
```

- 웹팩을 사용하면 SVG 파일과 CSS 파일도 불러와서 사용할 수 있다.이렇게 파일들을 불러오는 것은 웹팩의 로더(loader)라는 기능이 담당한다. 로더에는 여러가지 종류가 있는데 css-loader는 CSS 파일을 불러올 수 있게 해 주고, file-loader는 웹 폰트나 미디어 파일 등을 불러올 수 있게 해준다. 

- 특히 babel-loader는 자바스크립트 파일들을 불러오면서 최신 자바스크립트 문법으로 작성된 코드를 바벨이라는 도구를 사용하여 ES5 문법으로 변화을 해준다.

  > 💬
  >
  >  babel을 가지고 최신 자바스크립트 코드로 작성된 코드를 변환하는 이유는 ES5는 이전 버전의 자바스크립트를 말하는데 최신 JS문법을 ES5 형태로 변환하는 것은 구버전 웹 브라우저와 호환하기 위해서이다.
  >
  >  현재 대부분의 웹 브라우저에서는 최신 JS문법을 바로 실행할 수 있지만, 구 버전 웹브라우저에서는 실행이 되지 않기 때문에 사전에 변환해줘야한다.  앞으로 배우게 되는 리액트 컴포넌트에서 사용하는 JSX라는 문법도 정식 자바스크립트 문법이 아니므로 ES5 형태의 코드로 변환해야 한다.

``` react
function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}
```

- 위 코드는 Function 키워드를 사용해 함수형 컴포넌트로 App이라는 Component를 만들어 준다.
- 프로젝트에서 Component를 rendering(== 보여주다)하면 함수가 return하고 있는 내용을 나타낸다.
- 마치 HTML코드와 유사해 보이지만 HTML코드가 아닌 리액트에서 사용하는 문법인 JSX이다.

## 2.2 JSX

- JSX란 자바스크립트의 확장 문법이며 XML과 아주 유사하게 생겼다.
- 이렇게 작성한 코드가 브라우저에서 실행되기 전 코드가 번들링되는 과정에서 바벨을 사용하여 일반 자바스크립트 코드로 변환된다.

``` react
function App() {
  return (
  <div>
      Hello<b>react</b>
  </div>
  );
}
```

위와 같이 작성된 JSX는 

``` react
function App(){
  return React.createElement("div",null, "Hello", React.createElement("b", null, "react"));
}
```

와 같이 변환된다.

만약 Component를 렌더링할 때마다 JSX 코드를 작성하는 것이 아니라 매번 React.createElement 함수를 사용해야 한다면 매우 불편할 것이다. 따라서 JSX를 사용하면 아주 편하게 UI를 렌더링할 수가 있다.

## 2.3 JSX의 장점

1. 보기 쉽고 익숙하다.
   - 딱 보기에도 우리가 일반적으로 사용하는 HTML코드와 비슷해 보이기 때문에 더욱 가독성도 높고 작성하기도 쉽다. 이것이 우리가 JSX를 사용하는 주된 이유다.
2. 더욱 높은 활용도
   - JSX에서는 우리가 알고 있는 div나 span 같은 HTML 태그를 사용할 수 있을 뿐만 아니라, 앞으로 만들  Component도 JSX 안에서 작성할 수 있다. 
   - 아래 코드를 보면 App Component를 마치 HTML 태그 쓰듯이 그냥 작성하는 것을 볼 수 있다.

``` react
import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);
```

> 💬 
>
>  ReactDOM.render는 Component를 페이지에 렌더링하는 역할을 하며, react-dom 모듈을 불러와 사용할 수 있다. 이 함수의 첫 번째 파라미터에는 페이지에 렌더링할 내용을 JSX형태로 작성하고 두번째 파라미터에는 해당 JSX를 렌더링할 document 내부 요소를 설정한다. 여기서는 id가 root인 요소 안에 렌더링 하도록 설정했다. 
>
>  React.StrictMode는 리액트 프로젝트에서 리액트의 레거시 기능들을 사용하지 못하게 하는 기능이다. 이 기능을 사용하게 되면 문자열 ref, componentWillMount 등 나중에는 완전히 사라지게 될 옛날 기능을 사용했을 때 경고를 출력한다. 

# 2021.03.04

## 2.4 JSX 문법

### 2.4.1 감싸인 요소

- 컴포넌트에 여러 요소가 있다면 반드시 부모 요소 하나로 감싸야 한다.

``` react
import React from "react";

function App() {
  return (
    <h1>리액트 안녕!</h1>
    <h2>잘 작동하니?</h2>
  )
}

export default App;
```

위 코드를 실행하면 요소 여러개가 부모 요소 하나에 의하여 감싸져 있지 않기 때문에 오류가 발생한다.

이를 해결하기 위해서

``` react
import React from "react";

function App() {
  return (
    <div>
    	<h1>리액트 안녕!</h1>
      <h2>잘 작동하니?</h2>
    </div>
  )
}

export default App;
```

이와 같이 부모 요소로 감싸줌으로써 해결할 수 있다.

그렇다면 리액트 컴포넌트에서 요소 여러 개를 왜 하나의 요소로 꼭 감싸 주어야 할까? 그것은 Virtual DOM에서 컴포넌트 변화를 감지해 낼 때 효율적으로 비교할 수 있도록 <b>컴포넌트 내부는 하나의 DOM트리 구조로 이루어져야 한다</b>는 규칙이 있기 때문이다.

div요소를 사용하고 싶지 않다면 리액트 v16이상부터 도입된 Fragment라는 기능을 사용하면 된다.

```react
import React, {Fragment} from "react"

function App() {
  return (
    <Fragment>
    	<h1>리액트 안녕!</h1>
      <h2>잘 작동하니?</h2>
    </Fragment>
  )
}

export default App;
```

위와 같이 Fragment를 import 시켜서 사용하는 방법과 아래와 같이 사용하는 방법도 있다.

```react
import React from "react"

function App() {
  return (
    <>
    	<h1>리액트 안녕!</h1>
      <h2>잘 작동하니?</h2>
    </>
  )
}

export default App;
```

### 2.4.2 자바스크립트 표현

- JSX에서는 자바스크립트 표현식을 쓸 수 있다. 방법은 JSX 내부에서 코드를 {}로 감싸면 된다.

```react
import React from "react"

function App() {
  const name = "리액트"
  return (
    <>
    	<h1>{name} 안녕!</h1>
      <h2>잘 작동하니?</h2>
    </>
  )
}

export default App;
```

위와 같이 자바스크립트로 표현하는 것이 가능하다.

### 2.4.3 if문 대신 조건부 연산자

- JSX 내부의 자바스크립트 표현식에서는 if문을 사용할 수 없다.
- 조건에 따라 렌더링이 필요할 때는 JSX 밖에서 if문을 사용하여 사전에 값을 설정하거나, {} 안에 조건부 연산자(=삼항연산자)를 사용하면 된다.

```react
import React from "react"

function App() {
  const name = "리액트"
  return (
  	<div>
  		{name === "리액트" ? (
          <h1>리액트입니다.</h1>
          ) : (
          <h1>리액트가 아닙니다.</h1>
         	)}
    </div>
   );
}

export default App;
```

위 코드를 출력하면 화면에 ""리액트입니다." 라고 출력된 것을 확인할 수 있고 

name의 값을 아래와 같이 다른 값으로 바꿔주면 

```
const name = "자바스크립트";
```

''리액트가 아닙니다." 라는 문구가 나타난다.

### 2.4.4 AND 연산자(&&)를 사용한 조건부 렌더링

- 특정조건에 만족할 때는 내용을 보여주고 만족하지 않으면 아무것도 렌더링하지 않아야할 경우가 발생할 수 있다.

이럴 때도 조건부 연산자를 통해 구현할 수 있는데 아래 코드를 보면 name값이 조건에 맞지 않으면 아무것도 출력되지 않는 것을 확인할 수 있다.

```react
import React from "react";

function App() {
  const name = '리액트';
  return <div>{name === '리액트' ? <h1>리액트입니다.</h1> : null}</div>;
}

export default App;
```

하지만 이보다 더 짧게 코드를 작성할 수 있는데 아래 코드블럭을 보면 똑같은 결과가 나오는 걸 알  수 있다.

```react
import React from "react";

function App() {
  const name = '리액트';
  return <div>{name === "리액트" && <h1>리액트입니다.</h1>}</div>;
}

export default App;
```

&& 연산자로 조건부 렌더링을 할 수 있는 이유는 리액트에서 false를 렌더링할 때는 null과 마찬가지로 아무것도 나타나지 않기 때문이다. 여기서 한가지 주의할 점은 falsy한 값이 0은 예외적으로 화면에 나타난다는 점이다.

```react
const number = 0;
return number && <div>내용</div>;
```

예를 들어 이런 코드는 화면에 0을 보여준다.

> 💬
>
> <b>JSX는 언제 괄호로 감싸야 할까?</b>
>
> JSX를 작성할 때 (<div>Hello World</div>)와 같이 괄호로 감쌀 때도 있고, 감싸지 않을 때도 있는데 JSX를 여러 줄로 작성할 때 괄호로 감싸고, 한 줄로 표현할 수 있는 JSX는 감싸지 않는다. JSX를 괄호로 감싸는 것은 필수사항은 아니지만 에디터를 사용한다면 코드를 저장할 때 자동으로 괄호가 생기는걸 볼 수 있을 것이다.

### undefined를 렌더링하지 않기

- 리액트 컴포넌트에서는 함수에서 undefined만 반환하는 상황을 만들면 안된다.

```react
import React from "react";

function App() {
  const name = undefined;
  return name;
}

export default App;
```

위와 같은 코드는 오류를 일으킨다. 

어떤 값이 undefined일 수도 있다면 OR(||) 연산자를 사용하면 해당 값이 undefined일 때 사용할 값을 지정할 수 있으므로 간단하게 오류를 방지할 수 있다.

```react
import React from "react";

function App() {
  const name = undefined;
  return name || "값이 undefined입니다.";
}

export default App;
```

하지만 JSX 내부에서 undefined를 렌더링하는 것은 괜찮다.

```react
import React from "react";

function App() {
  const name = undefined;
  return <div>{name}</div>;
}

export default App;
```

만약 name 값이 undefined일 때 보여주고 싶은 문구가 있다면 아래와 같이 코드를 작성하면 된다.

```react
import React from "react";

function App() {
  const name = undefined;
  return <div>{name || "리액트"}</div>;
}

export default App;
```

### 2.4.6 인라인 스타일링

- 리액트에서 DOM요소에 스타일을 적용할 때는 일반적으로 css 요소를 추가하는 방법처럼 문자열 형태로 넣는 것이 아니라 객체 형태로 넣어 줘야 한다.
- 스타일 이름 중 background-color와 같이 - 문자가 포함되는 이름들은 -를 없애고 카멜 표기법으로 작성해야한다. 따라서 background-color는 backgroundColor로 작성한다.

```react
import React from "react";

function App() {
  const name = "리액트";
  const style = {
    backgroundColor: "black",
    color: "aqua",
    fontSize: "48px",
    fontWeight: "bold",
    padding: 16,
  };
  return <div style={style}>{name}</div>;
}

export default App;
```

위 코드 처럼 style 객체를 미리 선언하고 div의 style값을 지정해줬는데 미리 선언하지 않고 바로 style 값을 지정하고 싶다면 아래와 같이 작성하면 된다.

```react
import React from "react";

function App() {
  const name = "리액트";
  return <div style={{
    backgroundColor: "black",
    color: "aqua",
    fontSize: "48px",
    fontWeight: "bold",
    padding: 16,
  }}>
    {name}
  </div>;
}

export default App;
```

### class 대신 className

- 리액트에서는 태그에 class를 선언할 때 class 대신 className을 사용해야한다.
- class를 사용해도 스타일이 적용되긴 하지만 브라우저의 콘솔창에 경고메세지가 나온다.

### 꼭 닫아야 하는 태그

- HTML 코드를 작성할 때는 가끔 태그를 닫지 않은 상태로 코드를 작성하는 경우도 있다. 예를 들어 input 태그나 br태그는 </input>, </br> 처럼 닫아주지 않아도 문제가 없다.
- 하지만 리액트에서는 태그를 닫지 않으면 오류가 발생한다.

```react
import React from "react";

function App() {
  const name = undefined;
  return 
  	<>
  		<div className="react">{name}</div>
  		<input></input> // 또는 <input /> => 이러한 경우를 self-closing 태그라고 부른다.
  	</>;
}

export default App;
```

## 2.5 정리

- JSX는 HTML과 비슷하지만 완전히 똑같지는 않다. 코드로 보면 XML형식이지만 실제로는 자바스크립트 객체이며, 용도도 다르고 문법도 조금씩 차이가 난다.
