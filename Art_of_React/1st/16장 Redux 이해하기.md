리덕스는 가장 많이 사용하는 상태 관리 라이브러리다. 리덕스를 사용하면 컴포넌트의 상태 업데이트 관련 로직을 다른 파일로 분리시켜서 더욱 효율적으로 관리할 수 있다. 또한, 컴포넌트끼리 똑같은 상태를 공유해야 할 때도 여러 컴포넌트를 거치지 않고 손쉽게 상태 값을 전달하거나 업데이트할 수 있다.

리덕스 라이브러리는 전역 상태를 관리할 때 굉장히 효율적이다. 물론 리덕스를 사용하는 것이 유일한 해결책은 아니다. 이전에 배운 Context API를 통해서도 똑같은 작업을 할 수 있다. Context API가 개선되기 전에는 사용 방식이 매우 불편했기 때문에 주로 리덕스를 사용해 전역 상태 관리를 했다.

단순히 전역 상태 관리만 한다면 Context API를 사용하는 것만으로도 충분하다. 하지만 리덕스를 사용하면 상태를 더욱 체계적으로 관리할 수 있기 때문에 프로젝트의 규모가 클 경우에는 리덕스를 사용하는 편이 좋다. 코드의 유지 보수성도 높여 주고 작업 효율도 극대화해 주기 때문이다. 추가로 아주 편리한 개발자 도구도 지원하며, 미들웨어라는 기능을 제공하여 비동기 작업을 훨씬 효율적으로 관리할 수 있게 해 주기도 한다.

이번 실습은 다음과 같은 흐름으로 진행된다.

> 핵심 키워드 알아보기 → Parcel로 프로젝트 구성하기 → 토글 스위치와 카운터 구현하기

## 16.1 개념 미리 정리하기

먼저 앞으로 리덕스를 사용하면서 접하게 될 키워드의 개념을 간략하게 알아보도록 하자. 

#### 16.1.1 액션

상태에 어떠한 변화가 필요하면 액션(action)이란 것이 발생한다. 이는 하나의 객체로 표현되는데 액션 객체는 다음과 같은 형식으로 이루어져 있다.

```jsx
{
  type: 'TOGGLE_VALUE',
}
```

액션 객체는 type 필드를 반드시 가지고 있어야 한다. 이 값을 액션의 이름이라고 생각하면 된다. 그리고 그 외의 값들은 나중에 상태 업데이트를 할 때 참고해야 할 값이며, 작성자 마음대로 넣을 수 있다. 

```jsx
{
  type: 'ADD_TODO',
  data: {
    id: 1,
    text: '리덕스 배우기',
  }
}
  
{
  type: 'CHANGE_INPUT',
  text: '안녕하세요',
}
```

#### 16.1.2 액션 생성 함수

액션 생성 함수(action creator)는 액션 객체를 만들어 주는 함수다.

```react
function addTodo(data) {
	return {
    type: 'ADD_TODO',
    data
  };
}
// 화살표 함수로도 만들 수 있다.
const changeInput = text => ({
  type: 'CHANGE_INPUT',
  text
});
```

#### 16.1.3 리듀서

리듀서(Reducer)는 변화를 일으키는 함수다. 액션을 만들어서 발생시키면 리듀서가 현재 상태와 전달받은 액션 객체를 파라미터로 받아 온다. 그리고 두 값을 참고하여 **새로운 상태를 만들어서 반환**해 준다. 리듀서 코드는 다음과 같은 형태로 이루어져 있다.

```jsx
const initialState = {
  counter: 1,
}

function reducer(state=initialState, action) {
	switch(action.type) {
    case INCREMENT:
      return {
        counter: state.counter + 1
      };
    default:
      return state;
  }
}
```

#### 16.1.4 스토어

프로젝트에 리덕스를 적용하기 위해 스토어(store)를 만든다. 한 개의 프로젝트는 단 하나의 스토어만 가질 수 있다. 스토어 안에는 현재 애플리케이션 상태와 리듀서가 들어가 있으며, 그 외에도 몇 가지 중요한 내장 함수를 지닌다.

#### 16.1.5 디스패치

디스패치는 스토어의 내장 함수 중 하나다. 디스패치는 **'액션을 발생시키는 것'**이라고 이해하면된다. 이 함수는 `dispatch(action)` 과 같은 형태로 액션 객체를 파라미터로 넣어서 호출한다. 이 함수가 호출되면 스토어는 **리듀서 함수를 실행시켜 새로운 상태를 만들어 준다.**

#### 16.1.6 구독

구독(subscribe)도 스토어의 내장 함수 중 하나다. subscribe 함수 안에 리스너 함수를 파라미터로 넣어서 호출해 주면(**함수 형태의 값을 파라미터로 받음**), 이 리스너 함수가 액션이 디스패치되어 상태가 업데이트될 때마다 호출된다.

```jsx
const listener = () => {
  console.log('상태가 업데이트됨');
}
const unsubscribe = store.subscribe(listener);

unsubscribe(); // 추후 구독을 비활성화할 때 함수를 호출
```

## 16.2 리액트 없이 쓰는 리덕스

리덕스는 리액트에 종속되는 라이브러리가 아니다. 리액트에서 사용하려고 만들어졌지만 실제로 다른 UI 라이브러리/프레임워크와 함께 사용할 수도 있다.

또한 리덧스는 바닐라 자바스크립트와 함께 사용할 수도 있다. 이번에는 바닐라 자바스크립트 환경에서 리덕스를 하용하여 리덕스의 핵심 기능과 작동 원리를 이해해 보자.

#### 16.2.1 Parcel로 프로젝트 만들기

프로젝트를 구성하기 위해 Parcel이라는 도구를 사용해보겠다. 이 도구를 사용하면 아주 쉽고 빠르게 웹 애플리케이션 프로젝트를 구성할 수 있다.

먼저 parcel_bundler를 설치하고

`$ yarn global add parcel-bundler`

> ❗️ yarn global이 잘 설치되지 않으면 `npm install -g parcel-bundler` 를 해보자

프로젝트 디렉터리를 생성한 후 package.json 파일을 생성한다.

` $ mkdir vanila-redux `

`$ cd vanila-redux`

`$ yarn init -y` => package.json 파일 생성

에디터로 해당 디렉터리를 열어서 index.html과 index.js 파일을 만든 다음 아래 명령어를 실행하면 개발용 서버가 실행된다.

`$ parcel index.html`

<img src= "./images/16_02.png" />

개발 서버의 주소를 http://localhost:1234이며, 파일을 저장할 때마다 자동으로 새로고침 된다. 해당 주소로 들어가게 되면 정상적으로 돌아가고 있는 것을 확인할 수 있다.

<img src= "./images/16_01.png" />

이제 yarn을 사용하여 리덕스 모듈을 설치하면 프로젝트 준비가 완료된다.

`$ yarn add redux`

#### 16.2.2 간단한 UI 구성

실습을 위한 간단한 UI를 만들기 위해 css파일을 만들고 index.html을 다음과 같이 수정해줬다.

```jsx
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" type="text/css" href="index.css" />
    <title>Document</title>
  </head>
  <body>
    <div class="toggle"></div>
    <hr />
    <h1>0</h1>
    <button id="increase">+1</button>
    <button id="decrease">-1</button>
    <script src="./index.js"></script>
  </body>
</html>
```

```css
.toggle {
  border: 2px solid black;
  width: 64px;
  height: 64px;
  border-radius: 32px;
  box-sizing: border-box;
}

.toggle.active {
  background: yellow;
}
```

#### 16.2.3 DOM 레퍼런스 만들기

이번 프로젝트에서느 UI를 관리할 때 별도의 라이브러리를 사용하지 않기 때문에 DOM을 직접 수정해주어야 한다. 다음과 같이 자바스크립트 파일 상단에 수정할 DOM 노드를 가리키는 값을 미리 선언해 준다.

```jsx
const divToggle = document.querySelector(".toggle");
const counter = document.querySelector("h1");
const btnIncrease = document.querySelector("#increase");
const btnDncrease = document.querySelector("#Decrease");
```

#### 16.2.4 액션 타입과 액션 생성 함수 정의

프로젝트의 상태의 변화를 일으키는 것을 액션이라고 한다라고 배웠다. 먼저 액션에 이름을 정의해 주겠습니다. 액션 이름은 문자열 형태로, 주로 대문자로 작성하며 액션 이름은 고유해야 한다. 이름이 중복되면 의도하지 않은 결과가 발생할 수 있기 때문이다.

```jsx
const divToggle = document.querySelector(".toggle");
const counter = document.querySelector("h1");
const btnIncrease = document.querySelector("#increase");
const btnDncrease = document.querySelector("#Decrease");

const TOGGLE_SWITCH = "TOGGLE_SWITCH";
const INCREASE = "INCREASE";
const DECREASE = "DECREASE";
```

다음으로 이 액션 이름을 사용하여 액션 객체를 만드는 액션 생성 함수를 작성해 준다. 액션 객체는 type 값을 반드시 갖고 있어야 하며, 그 외에 추후 상태를 업데이트할 때 참고하고 싶은 값은 마음대로 넣을 수 있다.

```jsx
const divToggle = document.querySelector(".toggle");
const counter = document.querySelector("h1");
const btnIncrease = document.querySelector("#increase");
const btnDncrease = document.querySelector("#Decrease");

const TOGGLE_SWITCH = "TOGGLE_SWITCH";
const INCREASE = "INCREASE";
const DECREASE = "DECREASE";

const toggleSwitch = () => ({ type: TOGGLE_SWITCH });
const increase = (difference) => ({ type: INCREASE, difference });
const decrease = () => ({ type: DECREASE });
```

#### 16.2.5 초깃값 설정

초깃값의 형태는 자유다. 숫자일 수도 있고, 문자열일 수도 있고, 객체일 수도 있다.

```jsx
const divToggle = document.querySelector(".toggle");
const counter = document.querySelector("h1");
const btnIncrease = document.querySelector("#increase");
const btnDncrease = document.querySelector("#Decrease");

const TOGGLE_SWITCH = "TOGGLE_SWITCH";
const INCREASE = "INCREASE";
const DECREASE = "DECREASE";

const toggleSwitch = () => ({ type: TOGGLE_SWITCH });
const increase = (difference) => ({ type: INCREASE, difference });
const decrease = () => ({ type: DECREASE });

const initialState = {
  toggle: false,
  counter: 0,
};
```

#### 16.2.6 리듀서 함수 정의

리듀서는 변화를 일으키는 함수다. 함수의 파라미터로는 state와 action 값을 받아온다.

```jsx
const divToggle = document.querySelector(".toggle");
const counter = document.querySelector("h1");
const btnIncrease = document.querySelector("#increase");
const btnDncrease = document.querySelector("#Decrease");

const TOGGLE_SWITCH = "TOGGLE_SWITCH";
const INCREASE = "INCREASE";
const DECREASE = "DECREASE";

const toggleSwitch = () => ({ type: TOGGLE_SWITCH });
const increase = (difference) => ({ type: INCREASE, difference });
const decrease = () => ({ type: DECREASE });

const initialState = {
  toggle: false,
  counter: 0,
};

// state가 undefined일 때는 initialState를 기본값으로 사용
function reducer(state = initialState, action) {
  switch (action.type) {
    case TOGGLE_SWITCH:
      return {
        ...state, // 불변성을 유지해 주어야 한다.
        toggle: !state.toggle,
      };
    case INCREASE:
      return {
        ...state,
        counter: state.counter + action.difference,
      };
    case DECREASE:
      return {
        ...state,
        counter: state.counter - 1,
      };
    default:
      return state;
  }
}
```

리듀서 함수가 맨 처음 호출될 때는 state 값이 undefined이다. 해당 값이 undefined로 주어졌을 때는 initialState를 기본값으로 설정하기 위해 함수의 파라미터 쪽에 기본값이 설정되어 있다. 

리듀서에서는 **상태의 불변성을 유지하면서 데이터에 변화를 일으켜 주어야 한다.** 이 작업을 할 때 spread(...) 연산자를 사용하면 편하다. 단, 객체의 구조가 복잡해지면(ex: object.something.inside.value) spread 연산자로 불변성을 관리하며 업데이트하는 것이 굉장히 번거로울 수 있고 코드의 가독성도 나빠지기 때문에 **리덕스의 상태는 최대한 깊지 않은 구조로 진행하는 것이 좋다**. 

객체의 구조가 복잡해지거나 배열도 함께 다루는 경우 immer 라이브러리를 사용하면 좀 더 쉽게 리듀서를 작성할 수 있다.

#### 16.2.7 스토어 만들기

스토어를 만들 때는 createStore 함수를 사용한다. 이 함수를 사용하려면 코드 상단에 import 구문을 넣어 리덕스에서 해당 함수를 불러와야 하고, 함수의 파라미터에는 리듀서 함수를 넣어 주어야 한다. 

```jsx
const { createStore } = require("redux");

(...)
 
const store = createStore(reducer);
```



#### 16.2.8 render 함수 만들기

render 함수는 상태가 업데이트될 때마다 호출되며, 리액트의 render 함수와는 다르게 이미 html을 사용하여 만들어진 속성을 상태에 따라 변경해 준다.

```jsx
const { createStore } = require("redux");

(...)
 
const store = createStore(reducer);

const render = () => {
  const state = store.getState(); // 현재 상태를 불러온다.
  // 토글 처리
  if (state.toggle) {
    divToggle.classList.add("active");
  } else {
    divToggle.classList.remove("active");
  }
  //카운터 처리
  counter.innerText = state.counter;
};

render();
```

#### 16.2.9 구독하기

스토어의 상태가 바뀔 때마다 방금 만든 render 함수가 호출되도록 해 줄 것이다. 이 작업은 스토어의 내장 함수 subscribe를 사용하여 수행할 수 있다. subscribe 함수의 파라미터로는 함수형태의 값을 전달해 준다. 이렇게 전달된 함수는 추후 액션이 발생하여 상태가 업데이트될 때마다 호출된다.

```jsx
const listener = () => {
  console.log('상태가 업데이트됨');
}
const unsubscribe = store.subscribe(listener);

unsubscribe(); // 추후 구독을 비활성화할 때 함수를 호출
```

이번 프로젝트에서는 subscribe 함수를 직접 사용지만, 추후 리액트 프로젝트에서 리덕스를 사용할 때는 이 함수를 직접 사용하지 않을 것이다. 왜냐하면, 컴포넌트에서 리덕스 상태를 조회하는 과정에서 react-redux라는 라이브러리가 이 작업을 대신 해주기 때문이다. 

이제 상태가 업데이트될 때마다 render 함수를 호출하도록 코드를 작성해 보자.

```jsx
(...)
 
const render = () => {
  const state = store.getState(); // 현재 상태를 불러온다.
  // 토글 처리
  if (state.toggle) {
    divToggle.classList.add("active");
  } else {
    divToggle.classList.remove("active");
  }
  //카운터 처리
  counter.innerText = state.counter;
};

render();
store.subscribe(render);
```

#### 16.2.10 액션 발생시키기

액션을 발생시키는 것을 디스패치라고 한다. 디스패치를 할 때는 스토어의 내장 함수 dispatch를 사용한다. 파라미터는 액션 객체를 넣어 주면 된다.

다음과 같이 각 DOM 요소에 클릭 이벤트를 설정하고 이벤트 함수 내부에서는 dispatch 함수를 사용하여 액션에 스토어를 전달해 주자.

```jsx
(...)

divToggle.onclick = () => {
  store.dispatch(toggleSwitch());
};
btnIncrease.onclick = () => {
  store.dispatch(increase(1));
};
btnDecrease.onclick = () => {
  store.dispatch(decrease());
};
```

저장한 뒤 브라우저의 원과 버튼을 누르면 상태 변화가 잘 일어나는 것을 확인할 수 있다.

<img src= "./images/16_03.png" />

## 16.3 리덕스의 세 가지 규칙

#### 16.3.1 단일 스토어

하나의 애플리케이션 안에는 하나의 스토어가 들어 있다. 사실 여러 개의 스토어를 사용하는 것이 완전히 불가능하지는 않다. 특정 업데이트가 너무 빈번하게 일어나거나 애플리케이션의 특정 부분을 완전히 불리시킬 때 여러 개의 스토어를 만들 수도 있지만, 상태 관리가 복잡해질 수 있으므로 권장하지 않는다.

#### 16.3.2 읽기 전용 상태

리덕스 상태는 읽기 전용이다. 기존에 리액트에서 setState를 사용하여 state를 업데이트할 때도 객체나 배열을 업데이트하는 과정에서 불변성을 지켜 주기 위해 spread 연산자를 사용하거나 immer와 같은 불변성 관리 라이브러리를 사용했다. 리덕스도 마찬가지로 상태를 업데이트할 때 기존의 객체는 건드리지 않고 새로운 객체를 생성해 주어야 한다.

리덕스에서 불변성을 유지해야 하는 이유는 내부적으로 데이터가 변경되는 것을 감지하기 위해 얕은 비교(shallow equality)검사를 하기 때문이다. 객체의 변화를 감지할 때 객체의 깊숙한 안쪽까지 비굑하는 것이 아니라 겉핥기 식으로 비교하여 좋은 성능을 유지할 수 있는 것이다.

#### 16.3.3 리듀서는 순수한 함수

변화를 일으키는 리듀서 함수는 순수한 함수여야 한다. 순수한 함수는 다음 조건을 만족해야 한다

- 리듀서 함수는 이전 상태와 액션 객체를 파라미터로 받는다.
- 파라미터 외의 값에는 의존하면 안된다.
- 이전 상태는 절대로 건드리지 않고, 변화를 준 새로운 상태 객체를 만들어서 반환한다. = 불변성 유지
- 똑같은 파라미터로 호출된 리듀서 함수는 언제나 똑같은 결과 값을 반환해야 한다.

리듀서를 작성할 때는 위 네 가지 사항을 주의해야 한다. 예를 들어 리듀서 함수 내부에서 랜덤 값을 만들거나, Date 함수를 사용하여 현재 시간을 가져오거나, 네트워크 요청을 한다면, 파라미터가 같아도 다른 결과를 만들어 낼 수 있기 때문에 사용하면 안된다. 이러한 작업은 리듀서 함수 바깥에서 처리해 주어야 한다. 액션을 만드는 과정에서 처리해도 되고, 추후 배울 리덕스 미들웨어에서 처리해도 된다. **주로 네트워크 요청과 같은 비동기 작업은 미들웨어를 통해 관리한다.**

## 16.4 정리

다음 장에서는 리액트 프로젝트에서 리덕스를 사용하는 방법을 알아볼 예정이다. 리덕스 코드를 작성하는 흐름은 이번 장에서 했던 것과 매우 유사하다. 먼저 액션 타입과 액션 생성 함수를 작성하고, 이어서 리듀서를 작성하고, 스토어를 만든다. 이번 프로젝트에서는 함수에서 스토어를 구독하는 작업을 직접 해 보았지만, 다음 장에서는 react-redux라는 라이브러리를 사용하여 스토어의 상태가 업데이트될 때마다 컴포넌트를 리렌더링 시켜 주겠다.