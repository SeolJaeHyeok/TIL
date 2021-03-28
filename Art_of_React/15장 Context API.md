# Context API

Context API는 리액트 프로젝트에서 전역적으로 사용할 데이터가 있을 때 유용한 기능이다. 이를테면 사용자 로그인 정보, 애플리케이션 환경 설정, 테마 등 여러 종류가 있을 수 있다. 이 기능은 리액트 관련 라이브러리에서도 많이 사용되고 있다. 예를 들어 리덕스, 리액트 라우터, styled-components 등의 라이브러리는 Context API를 기반으로 구현되어 있다.

이번 실습은 다음과 같은 흐름으로 진행된다.

> Context API를 사용한 전역 상태 관리 흐름 이해하기 → 기본적인 사용법 익히기 → 동적 Context 사용하기 → Consumer 대신 Hook 또는 static contextType 사용하기

## 15.1 Context API를 사용한 전역 상태 관리 흐름 이해하기

프로젝트 내에서 환경 설정, 사용자 정보와 같은 전역적으로 필요한 상태를 관리해야 할 때는 어떻게 해야 할까?

리액트 애플리케이션은 컴포넌트 간에 **데이터를 props로 전달**하기 때문에 컴포넌트 여기저기서 필요한 데이터가 있을 때는 **주로 최상위 컴포넌트인 App의 state에 넣어서 관리**한다. 

![](https://thebook.io/img/080203/392_2.jpg)

G 컴포넌트는 전역 상태를 업데이트 시키고, F와 J 컴포넌트는 업데이트 된 상태를 렌더링 한다고 가정해보자. 그렇다면 App 컴포넌트에서는 다음과 같이 상태와 업데이트 함수를 정의해야 한다.

```react
const [value, setValue] = useState('Hello');
const onSetValue = useCallback(value => setValue(value), []);
```

그리고 App이 지니고 있는 value 값을 F 컴포넌트와 J 컴포넌트에 전달하려면 여러 컴포넌트를 거쳐야 한다. F의 경우 App -> A -> B -> F의 흐름이고, J의 경우 App -> H -> J의 흐름이다. 추가로 G 컴포넌트에 상태 업데이트 함수를 전달할 때도 App -> A -> B -> E -> G와 같이 복잡하게 여러 번 거쳐서 전달해야 한다.

실제로 리액트 프로젝트에서는 더 많은 컴포넌트를 거쳐야 할 때도 있고 다루어야 하는 데이터가 훨씬 많아질 수도 있으므로, 이런 방식을 사용하면 유지 보수성이 낮아질 가능성이 높다. 그렇기 때문에 **리덕스나 MobX같은 상태 관리 라이브러리를 사용하여 전역 상태 관리 작업을 더 편하게 처리**하기도 한다. 리액트 v16.3 업데이트 이후에는 Context API가 많이 개선되었기 떄문에 별도의 라이브러리를 사용하지 않아도 전역 상태 관리를 손쉽게 할 수 있다.

아래 그림과 같이 기존에는 최상위 컴포넌트에서 여러 컴포넌트를 거쳐 props로 원하는 상태와 함수를 전달했지만, **Context API를 사용하면 Context를 만들어 단 한번에 원하는 값을 받아 와서 사용할 수 있다.**

![](https://media.vlpt.us/images/choidy180/post/0ec72aab-06a7-4ff8-9f05-a414a70a9cb6/image.png)

## 15.2 Context API 사용법 익히기

먼저 Context API를 연습할 리액트 프로젝트를 생성해 준다.

`$ yarn create react-app context-tutorial`

#### 15.2.1 새 Context 만들기

프로젝트를 생성한 후, 새로운 Context를 만들어보자. src 디렉터리에 contexts 디렉터리를 만든 뒤 그 안에 color.js라는 파일을 만든다. Context를 만들 때 반드기 contexts 디렉터리를 만들 필요는 없지만 다른 파일과 구분하기 위해 따로 디렉터리를 만들었다.

파일을 만들고 아래와 같이 입력한다.

```react
import { createContext } from "react";

const colorContext = createContext({ color: "black" });

export default colorContext;
```

새 Context를 만들 때는 createContext 함수를 사용한다. 파라미터에는 해당 Context의 기본 상태를 지정한다.

#### 15.2.2 Consumer 사용하기

이번에는 ColorBox라는 컴포넌트를 만들어서 ColorContext 안에 들어 있는 색상을 보여주도록 해보자. 이때 생상을 props로 받아 오는 것이 아니라 ColorContext 안에 들어 있는 Consumer라는 컴포넌트를 통해 색상을 조회할 예정이다.

Src 디렉터리에 components 디렉터리를 만들고, 그 안에 ColorBox.js 파일을 생성하여 아래와 같이 입력해준다.

```react
import React from "react";
import ColorContext from "../contexts/color";

const ColorBox = () => {
  return (
    <ColorContext.Consumer>
      {(value) => (
        <div
          style={{ width: "64px", height: "64px", backgroud: value.color }}
        />
      )}
    </ColorContext.Consumer>
  );
};

export default ColorBox;
```

Consumer 사이에 중괄호를 열어서 그 안에 함수를 넣어 주었다. 이러한 패턴을 Function as a child, 혹은 Render Props 라고 부른다. 컴포넌트의 children이 있어야 할 자리에 일반 JSX 혹은 문자열이 아닌 함수를 전달하는 것이다.

> 💬
>
> Render Props 예제
>
> ```react
> import React from "react";
> 
> const RenderPropsSample = ({children}) => {
>   return <div>결과: {children(5)}</div>;
> }
> 
> export default RenderPropsSample;
> ```
>
> 만약 위와 같은 컴포넌트가 있다면 추후 사용할 때 다음과 같이 사용할 수 있다.
>
> ```react
> <RenderPropsSample>{value => 2 * value}</RenderPropsSample>;
> ```
>
> RenderPropsSample에게 children props로 파라미터에 2를 곱해서 반환하는 함수를 전달하면 해당 컴포넌트에서는 이 함수에 5를 인자로 넣어서 "결과 : 10"을 렌더링 한다.

컴포넌트를 다 만든 다음 App 컴포넌트에 렌더링 하고 브라우저를 확인해보면 아래와 같은 검정색 정사각형이 나타난 것을 확인할 수 있다.

<img src="./images/15_01.png" />

#### 15.3 Provider

Provider를 사용하면 Context의 value를 변경할 수 있다. App 컴포넌트를 다음과 같이 수정해보자

```react
import React from "react";
import ColorBox from "./components/ColorBox";
import ColorContext from "./contexts/color";

function App() {
  return (
    <ColorContext.Provider value={{ color: "red" }}>
      <div>
        <ColorBox />
      </div>
    </ColorContext.Provider>
  );
}

export default App;
```

저장한 후 브라우저를 확인하면 빨간색 박스로 바뀐 것을 확인할 수 있다.

<img src="./images/15_02.png" />

기존에 createContext 함수를 사용할 때는 파라미터로 Context의 기본값(여기서는 'black')을 넣어 줬다. 이 기본값은 Provider를 사용하지 않았을 때만 사용된다. 만약 Provider를 사용했는데 value를 명시하지 않았다면, 이 기본값을 사용하지 않기 때문에 오류가 발생한다. 

다음은 오류가 발생하는 코드다.

```react
import React from "react";
import ColorBox from "./components/ColorBox";
import ColorContext from "./contexts/color";

function App() {
  return (
    <ColorContext.Provider>
      <div>
        <ColorBox />
      </div>
    </ColorContext.Provider>
  );
}

export default App;
```

Provider를 사용하고 value를 명시하지 않으면 아래와 같이 오류가 발생한다. 따라서 Provider를 사용한다면 value를 꼭 명시해 주어야 제대로 작동한다는 것을 명심해야 한다.

<img src="./images/15_03.png" />

## 15.3 동적 Context 사용하기

