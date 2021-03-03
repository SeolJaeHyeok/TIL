# 2021.03.03

## 2.1 코드 이해하기

![스크린샷 2021-03-03 오후 8.38.28](/Users/seoljaehyeok/Library/Application Support/typora-user-images/스크린샷 2021-03-03 오후 8.38.28.png)

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

![스크린샷 2021-03-03 오후 9.16.34](/Users/seoljaehyeok/Library/Application Support/typora-user-images/스크린샷 2021-03-03 오후 9.16.34.png)

> 💬 
>
>  ReactDOM.render는 Component를 페이지에 렌더링하는 역할을 하며, react-dom 모듈을 불러와 사용할 수 있다. 이 함수의 첫 번째 파라미터에는 페이지에 렌더링할 내용을 JSX형태로 작성하고 두번째 파라미터에는 해당 JSX를 렌더링할 document 내부 요소를 설정한다. 여기서는 id가 root인 요소 안에 렌더링 하도록 설정했다. 
>
>  React.StrictMode는 리액트 프로젝트에서 리액트의 레거시 기능들을 사용하지 못하게 하는 기능이다. 이 기능을 사용하게 되면 문자열 ref, componentWillMount 등 나중에는 완전히 사라지게 될 옛날 기능을 사용했을 때 경고를 출력한다. 

