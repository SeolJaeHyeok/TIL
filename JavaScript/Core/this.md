# this

다른 대부분의 객체지향 언어에서 `this` 는 클래스로 생성한 인스턴스 객체를 의미한다. 클래스에서 사용할 수 있기 때문에 혼란의 여지가 많지 없거나 많지 않다. 그러나 자바스크립트에서는 `this`를 어디에서나 사용할 수 있기 때문에 상황에 따라 `this` 가 바라보는 대상이 달라진다. 어떤 이유로 그렇게 되는지를 파악하기 힘든 경우도 있고 예상과 다르게 엉뚱한 대상을 바라보는 경우도 있다.

함수와 객체(메서드)의 구분이 느슨한 자바스크립트에서 `this`는 실질적으로 이 둘을 구분하는 거의 유일한 기능이다. 여기서느 상황별로 `this`가 어떻게 달라지는지, 왜 그렇게 되는지, 예상과 다른 대상을 바라보고 있을 경우 원인을 효과적으로 추적하는 방법 등을 살펴보도록 하자.

### 1. 상황에 따라 달라지는 this

자바스크립트에서 `this` 는 기본적으로 실행 컨텍스가 생성될 때 함께 결정된다. 실행 컨텍스트는 함수를 호출할 때 생성되므로, 바꿔 말하면 `this`는 **함수를 호출할 때 결정된다**고 할 수 있다. 함수를 어떤 방식으로 호출하느냐에 따라 값이 달라지는 것이다. 

#### 1-1 전역 공간에서의 this

전역 공간에서의 `this`는 전역 객체를 가리킨다.  개념상 전역 컨텍스트를 생성하는 주체가 바로 전역 객체이기 때문이다. 전역 객체는 자바스크립트 런타임 환경에 따라 다른 이름과 정보를 가지고 있다. 브라우저 환경에서 전역 객체는 `window` 이고 Node.js 환경에서는 `global`이다.

**3-1** 전역 공간에서의 `this`(브라우저 환경)

```javascript
console.log(this); // { alert: f(), atob: f(), blur: f(), btoa: f(), ... }
console.log(window); // { alert: f(), atob: f(), blur: f(), btoa: f(), ... }
console.log(this === window); // true
```

**3-2** 전역 공간에서의 `this`(Node.js 환경)

```javascript
console.log(this); // { process: { title: 'node', version: 'v10.13.0',... } }
console.log(global); // { process: { title: 'node', version: 'v10.13.0',... } }
console.log(this === global); // true
```

`this`에 대해 살펴보기 앞서 전역 공간에서 발생하는 특이한 성질 하나를 살펴보도록 하자.

전역 변수를 선언하면 자바스크립트 엔진은 이를 전역 객체의 프로퍼티로도 할당한다. 변수이면서 객체의 프로퍼티이기도 한 것이다. 코드로 확인해보자.

**3-3** 전역 변수와 전역 객체(1)

```javascript
var a = 1;
console.log(a); // 1
console.log(window.a); // 1
console.log(this.a); // 1
```

전역공간에서 선언한 변수 a에 1을 할당했을 뿐인데 `window.a`와 `this.a` 모두 1이 출력이 된다. 전역공간에서의 `this`는 전역객체를 의미하므로 두 값이 같은 값을 출력하는 것은 당연하지만, 그 값이 1인 것이 의문이 들 수 있다. 그 이유는 **자바스크립트의 모든 변수는 실은 특정 객체의 프로퍼티**로서 동작하기 때문이다. 사용자가 `var` 연산자를 이용해 변수를 선언하더라도 실제 자바스크립트 엔진은 어떤 특정 객체의 프로퍼티로 인식하는 것이다. 특정 객체란 바로 실행 컨텍스트의 `LexicalEnvirionment` 다. 실행 컨텍스트는 변수를 수집해서 `LexicalEnvirionment` 의 프로퍼티로 저장한다. 이후 어떤 변수를 호출하면 `LexicalEnvirionment` 를 조회해서 일치하는 프로퍼티가 있을 경우 그 값을 반환한다. 전역 컨텍스트의 경우 `LexicalEnvirionment` 는 전역 객체를 그대로 참조한다.

앞에서 '전역변수를 선언하면 자동으로 전역객체의 프로퍼티로도 할당한다'고 했는데, 이제 이 문장은 틀렸다는 것을 이해할 수 있다. 정확히 표현하자면 '**전역변수를 선언하면 자바스크립트 엔진은 이를 전역객체의 프로퍼티로 할당한다**' 가 될 것이다. 

그렇다면 `window.a`나 `this.a`가 1이 나오는 이유가 설명되는데, a를 직접 호출할 때도 1이 나오는 까닭은 무엇일까?  

이는 변수 a에 접근하고자 하면 스코프 체인에서 a를 검색하다가 가장 마지막에 도달하는 전역 스코프의 `LexicalEnvirionment`,  즉 전역객체에서 해당 프로퍼티 a를 발견해서 그 값을 반환하기 때문이다. 원리는 이러하나 단순하게 `window.` 이 생략된 것이라고 여겨도 무방하다.

이렇다 하는 것은 전역 공간에서 `var`로 변수를 선언하는 대신 `window`의 프로퍼티에 직접 할당하더라도 결과적으로 `var`로 선언한 것과 똑같이 동작할 것이라는 예상을 할 수 있다. 그리고 이 예상은 대부분의 경우에는 맞다.

**3-4** 전역변수와 전역객체(2)

```javascript
var a = 1;
window.b = 2;
console.log(a, window.a, this.a); // 1 1 1
console.log(b, window.b, this.b); // 2 2 2

window.a = 3;
b = 4;
console.log(a, window.a, this.a); // 3 3 3
console.log(b, window.b, this.b); // 4 4 4
```

그런데 전역변수 선언과 전역객체의 프로퍼티 할당 사이에 전혀 다른 경우도 있는데 바로 '삭제' 명령에서 그렇다.

**3-5** 전역변수와 전역객체(3)

```javascript
var a = 1;
delete window.a; // false
console.log(a, window.a, this.a); // 1 1 1

var b = 2;
delete b; // false
console.log(b, window.b, this.b); // 2 2 2

window.c = 3;
delete window.c; // true
console.log(c, window.c, this.c); // Uncaught ReferenceError: c is not defined

window.d = 4;
delete d; // true
console.log(d, window.d, this.d); // Uncaught ReferenceError: d is not defined
```

예제를 살펴보면 처음부터 전역객체의 프로퍼티로 할당한 경우에는 삭제가 되는 반면 전역변수로 선언한 경우네느 삭제가 되지 않는 것을 확인할 수 있다. 이는 사용자가 의도치 않게 삭제하는 것을 방지하는 차원에서 마련한 나름의 방어 전략이라고 해석된다. 즉, 전역변수를 선언하면 자바스크립트 엔진이 이를 자동으로 전역객체의 프로퍼티로 할당하면서 추가적으로 해당 프로퍼티의 configurable 속성(변경 및 삭제 가능성)을 false로 정의하는 것이다.

이처럼 `var`로 선언한 전역변수와 전역객체의 프로퍼티는 호이스팅 여부 및 configurable 여부에서 차이를 보인다.

#### 1-2 메서드로서 호출할 때 그 메서드 내부에서의 this

**함수 vs. 메서드**

어떤 함수를 실행하는 방법은 여러 가지가 있는데, 가장 일반적인 방법 두 가지는 함수로서 호출하는 경우와 메서드로서 호출하는 경우다. 프로그래밍 언어에서 함수와 메서드는 미리 정의한 동작을 수행하는 코드 뭉치로, 이 둘을 구분하는 유일한 차이는 **독립성**에 있다. 함수는 그 자체로 독립적인 기능을 수행하는 반면, 메서드는 자신을 호출한 대상 객체에 관한 동작을 수행한다. 자바스크립트는 상황별로 `this` 키워드에 다른 값을 부여하게 함으로써 이를 구현했다.

자바스크립트를 처음 접하는 사람들은 흔히 메서드를 '객체의 프로퍼티에 할당된 함수'로 이해하곤 한다. 어떤 함수를 객체의 프로퍼티에 할당한다고 해서 그 자체로서 무조건 메서드가 되는 것이 아니라 객체의 메서드로서 호출할 경우에만 메서드로 동작하고, 그렇지 않으면 함수로 동작한다.

**3-6** 함수로서 호출, 메서드로서 호출

```javascript
var func = function(x) {
  console.log(this, x);
};
func(1); // Window { ... } 1

var obj = {
  method: func,
};
obj.method(2); // { method: f } 2
```

1번째 줄에서 `func`라는 변수에 익명함수를 할당했다. 4번째 줄에서 `func`를 호출했더니 `this`로 전역객체 Window가 출력된다.  6번째 줄에서 obj라는 변수에 객체를 할당하는데, 그 객체의 method 프로퍼티에 앞에서 만든 `func`함수를 할당했다. 이제 9번째 줄에 obj에서 method 프로퍼티를 호출했더니, 이번에는 `this`가 obj라고 한다. obj의 method 프로퍼티로 할당한 값과 `func` 변수에 할당한 값은 모두 1번째 줄에서 선언한 함수를 참조한다. **즉 원래 익명함수는 그대로인데 이를 변수에 담아 호출한 경우와 obj의 프로퍼티에 할당해서 호출한 경우에 `this`가 달라지는 것이다.**

그렇다면 '함수로서 호출'과 '메서드로서 호출'은 어떻게 구분할까?

함수 앞에 점(.)이 있는지 여부만으로 간단하게 구분할 수 있다. 위 예제의 4번째 줄은 앞에 점이 없으니 함수로서 호출한 것이고, 9번째 줄은 method 앞에 점이 있으니 메서드로서 호출한 것이다. 

**3-7** 메서드로서 호출 - 점 표기법, 대괄호 표기법

```javascript
var obj = {
  method: function(x) {
    console.log(this, x);
  },
};
obj.method(1); // { method: f } 1
obj['method'](2); // { method: f } 2
```

다시 말해 점 표기법이든 대괄호 표기법이든, 어떤 함수를 호출할 때 그 함수 이름(프로퍼티 명) 앞에 객체가 명시돼 있는 경우에는 메서드로 호출한 것이고, 그렇지 않은 모든 경우에는 함수로 호출한 것이다.

**메서드 내부에서의 this**

`this`에는 호출한 주체에 대한 정보가 담긴다. 어떤 함수를 메서드로서 호출하는 경우 호출 주체는 바로 함수명(프로퍼티 명) 앞의 객체다. 점 표기법의 경우 마지막 점 앞에 명시된 객체가 곧 `this`가 되는 것이다.

**3-8** 메서드 내부에서의 this

```javascript
var obj = {
  methodA: function() {
    console.log(this);
  },
  inner: {
    methodB: function() {
      console.log(this);
    },
  },
};
obj.methodA(); // { methodA: f, inner: {...} }    ( === obj)
obj['methodA'](); // { methodA: f, inner: {...} } ( === obj)

obj.inner.methodB(); // { methodB: f }            ( === obj.inner)
obj.inner['methodB'](); // { methodB: f }         ( === obj.inner)
obj['inner'].methodB(); // { methodB: f }         ( === obj.inner)
obj['inner']['methodB'](); // { methodB: f }      ( === obj.inner)
```

