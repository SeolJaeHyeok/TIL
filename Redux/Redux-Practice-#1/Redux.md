# Redux

![](https://s3-ap-northeast-2.amazonaws.com/opentutorials-user-file/module/4078/11034.png)

- Redux의 핵심은 store(은행)

- Store : 정보가 저장되는 곳
  - `Redux.createStore(reducer)`

- State : 실제 정보, 절대로 직접 접근 불가능. 

  - getState를 통해 값을 가져오고 
  - Dispatch를 통해 값을 변경시키고 
  - Subscribe를 이용해서 값이 변경됐을 때 구동될 함수들을 등록
  - 리듀서 안에서만 State를 변경시키는 로직 작성

- Reducer : 유일하게 state에 접근할 수 있는 함수. store를 생성할 때 reducer를 인자로 넘겨줘야 한다.

  - ```jsx
    function reducer(oldState, action) {
    	// ...
    }
    ```

- Render: 현재 State 값을 참조해서 UI를 만들어주는 역할을 하는 코드

- subscribe : store의 state 값이 바뀔 때 마다 render 함수를 호출하여 UI를 갱신시켜주는 역할

  - `store.subscribe(render)`

- Dispatch : reducer를 호출해서 state 값을 바꾸는 역할. 그런 다음 subscribe를 이용해 render 함수를 호출하면 화면이 갱신이 된다.

  - Dispatch가 reducer를 호출할 때 두 개의 인자를 전달
  - dispatch를 통해 reducer 함수를 호출하고 action의 type에 해당하는 로직을 실행한 후 새로운 State의 값을 return한다.
  - **이 때 state는 immutability(불변성)을 유지해줘야 한다.**
  - 즉, reducer는 state 값을 인자로 받고 action을 참조해서 새로운 state 값을 만들어 리턴해 주는 함수를 말한다.





 