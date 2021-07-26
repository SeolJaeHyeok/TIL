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

#### 1-3 함수로서 호출할 때 그 함수 내부에서의 this

**함수 내부에서의 this**

어떤 함수를 함수로서 호출할 경우에는 `this`가 지정되지 않는다. `this`에는 호출한 주체에 대한 정보가 담긴다고 언급했었다. 그런데 함수로서 호출하는 것은 호출 주체(객체지향언어에서의 객체)를 명시하지 않고 개발자가 코드에 직접 관여해서 실행한 것이기 떄문에 호출 주체의 정보를 알 수 없는 것이다.

2장에서 실행 컨텍스트를 활성화할 당시에 `this`가 지정되지 않은 경우 `this`는 전역객체를 바라본다고 했다. 따라서 함수에서의 `this`는 전역객체를 가리킨다. 자바스크립트 개발에 참여한 더글라스 크락포드(Douglas Crockford)는 이를 명백한 설계 오류라고 지적하는데 그 이유를 알아보자.

**메서드의 내부 함수에서의 this**

메서드 내부에서 정의하고 실행한 함수에서의 `this`는 자바스크립트 초심자들이 `this`에 관해 가장 자주 혼란을 느끼는 지점이다. 앞서 말한 '설계상의 오류'로 인해 실제 동작과 다르게 예측하곤 한다. `this`라는 단어 자체가 주는 느낌적 느낌 그대로 코드를 바라보면 다른 결과가 나온다. 그러나 앞에서 말했듯 이미 어떤 함수를 메서드로서 호출할 때 함수로서 호출할 때 `this`가 무엇을 가리키는지를 알고 있다. 내부함수 역시 이를 함수로서 호출했는지 메서드로서 호출했는지만 파악하면 `this`의 값을 정확히 맞출 수 있다. 

**3-9** 내부함수에서의 this

```javascript
var obj1 = {
  outer: function() {
    console.log(this); // (1)
    var innerFunc = function() {
      console.log(this); // (2) (3)
    };
    innerFunc();

    var obj2 = {
      innerMethod: innerFunc,
    };
    obj2.innerMethod();
  },
};
obj1.outer();
```

Console.log의 결과는 (1) obj1, (2) 전역객체(Window), (3) obj2이다. 코드 흐름에 따라 분석해보자.

- 1번째 줄: 객체를 생성하는데, 이때 객체 내부에는 outer라는 프로퍼티가 있으며, 여기에는 익명함수가 연결된다. 이렇게 생성한 객체를 변수 obj1에 할당한다.
- 15번째 줄: obj1.outer를 호출한다.
- 2번째 줄: obj1.outer 함수의 실행 컨텍스트가 생성되면서 호이스팅하고, 스코프 체인 정보를 수집하고, `this`를 바인딩한다. 이 함수를 호출할 때 함수명인 outer 앞에 점(.)이 있으므로 메서드로서호출한 것이고 따라서 `this`에는 마지막 점 앞의 객체인 obj1이 바인딩된다.
- 3번째 줄: obj1 객체 정보가 출력된다.
- 4번째 줄: 호이스팅된 변수 innerFunc는 outer 스코프 내에서만 접근할 수 있는 지역변수다. 이 지역변수에 익명 함수를 할당한다. 
- 7번째 줄: innerFunc를 호출한다.
- 4번째 줄: innerFunc 함수의 실행 컨텍스트가 생성되면서 호이스팅, 스코프 체인 수집, `this` 바인딩 등을 수행한다. 이 함수를 호출할 때 함수명 앞에 점(.)이 없다. 즉 함수로서 호출한 것이므로 `this`가 지정되지 않았고, 따라서 자동으로 스코프 체인상의 최상위 객체인 전역객체(Window)가 바인딩 된다.
- 5번째 줄: Window 객체 정보가 출력된다.
- 9번째 줄: 호이스팅된 변수 obj2 역시 outer 스코프 내에서만 접근할 수 있는 지역변수다. 여기에는 다시 객체를 할당하는데, 그 객체에는 innerMethod라는 프로퍼티가 있으며, 여기에는 앞서 정의된 변수 innerFunc와 연결된 익명 함수가 연결된다.
- 12번째 줄: obj2.innerMethod를 호출한다.
- 9번째 줄: obj2.innerMethod 함수의 실행 컨텍스트가 생성된다. 이 함수는 호출할 때 함수명인 innerMethod 앞에 점(.)이 있었으므로 메서드로서 호출한 것이다. 따라서 `this`는 마지막 점 앞의 obj2가 바인딩 된다.
- 10번째 줄: obj2 객체 정보가 출력된다.

7번째 줄에서는 outer 메서드 내부에 있는 함수(innerFunc)를 함수로서 호출했다. 반면 12번째 줄에서는 같은 함수(innerFunc)를 메서드로서 호출했다. 같은 함수임에도 7번째 줄에 의해 바인딩되는 `this`와 12번째 줄에 의해 바인딩되는 `this` 의 대상이 서로 달라진 것이다.

그러니까 `this` 바인딩에 관해서는 함수를 실행하는 당시의 주변 환경(메서드 내부인지, 함수 내부인지 등) 중요하지 않고, 오직 해당 함수를 호출하는 구문 앞에 점 또는 대괄호 표기가 있는지 없는지 관건이다.

**메서드의 내부 함수에서의 this를 우회하는 방법**

이렇게 하면 `this`에 대한 구분은 명확히 할 수 있지만, 그 결과 `this` 라는 단어가 주는 인상과는 사뭇 달라져 버렸다. 호출 주체가 없을 때는 자동으로 전역객체를 바인딩하지 않고 호출 당시 주변 환경의 `this`를 그대로 상속받아 사용할 수 있다면 좋을 것 같다. 그게 훨씬 자연스러울뿐더러 자바스크립트 설계상 이렇게 동작하는 편이 스코프 체인과의 일관성을 지키는 설득력이 있는 방식이었다. 변수를 검색하면 우선 가장 가까운 스코프의 `LexicalEnvironment`를 찾고없으면 상위 스코프를 탐색하듯이, `this` 역시 현재 컨텍스트에 바인딩된 대상이 없으면 직전 컨텍스트의 `this`를 바라보도록 하는 것이다.

그러나 사용자 입장에서는 어색하더라도 그 자체를 언어가 가지고 있는 고유한 특성으로 받아들이고 주어진 환경에 적응할 수 밖에 없다. ES5까지는 자체적으로 내부함수에 `this`를 상속할 방법이 없지만 이를 우회할 수 있는 방법은 있는데 대표적으로 변수를 활용하는 것이다.

**3-10** 내부 함수에서의 `this`를 우회하는 방법

```javascript
var obj = {
  outer: function() {
    console.log(this); // (1) { outer: f }
    var innerFunc1 = function() {
      console.log(this); // (2) Window { ... }
    };
    innerFunc1();

    var self = this;
    var innerFunc2 = function() {
      console.log(self); // (3) { outer: f }
    };
    innerFunc2();
  },
};
obj.outer();
```

위 예제의 innerFunc1 내부에서 `this`는 전역객체를 가리킨다. 한편 outer 스코프에서 self라는 변수에 `this`를 저장한 상태에서 호출한 innerFunc2의 경우 self에는 객체 obj가 출력된다. 허무한 방법이지만 생각했던대로 동작하기는 한다. 사람마다 서로 다른 변수명을 사용하는데, self가 가장 많이 쓰이고 있다. 그저 상위 스코프의 `this`를 저장해서 내부함수에서 활용하려는 수단일뿐이므로 의미만 통한다면 변수명을 무엇으로 정해도 무관하다.

**`this`를 바인딩하지 않는 함수**

ES6에서는 함수 내부에서 `this`가 전역객체를 바라보는 문제를 보완하고자, `this`를 바인딩하지 않는 화살표 함수(Arrow Function)을 도입했다. 화살표 함수는 실행 컨텍스트를 생성할 때 `this` 바인딩 과정 자체가 빠지게 되어, 상위 스코프의 `this`를 그대로 활용할 수 있다. 내부 함수를 화살표 함수로 바꾸면 앞서 말한 '우회법'이 필요가 없어진다.

**3-11** `this`를 바인딩하지 않는 함수(화살표 함수)

```javascript
var obj = {
  outer: function() {
    console.log(this); // (1) { outer: f }
    var innerFunc = () => {
      console.log(this); // (2) { outer: f }
    };
    innerFunc();
  },
};
obj.outer();
```

그 밖에도 `call`, `apply` 등의 메서드를 활용해 함수를 호출할 때 명시적으로 `this`를 지정하는 방법도 있다.

#### 1-4 콜백 함수 호출 시 그 함수 내부에서의 this

콜백 함수의 정의와 동작 원리에 대해서는 다음 장에서 자세히 다루도록 하고 여기서는 `this`가 어떤 값을 참조하는지만 알아보도록 하자.

함수 A의 제어권을 다른 함수(또는 메서드) B에게 넘겨주는 경우 함수 A를 콜백함수라고 한다. 이때 함수 A는 함수 B의 내부 로직에 따라 실행되며, `this` 역시 함수 B 내부 로직에서 정한 규칙에 따라 값이 결정된다. 콜백 함수도 함수이기 때문에 기본적으로 1-3절과 마찬가지로 `this`가 전역객체를 참조하지만, 제어권을 받은 함수에서 콜백 함수에 별도록 `this`가 될 대상을 지정한 경우에는 그 대상을 참조하게 된다.

**3-12** 콜백 함수 내부에서의 `this`

```javascript
setTimeout(function() {																													// (1)
  console.log(this);
}, 300);

[1, 2, 3, 4, 5].forEach(function(x) {																						// (2)
  console.log(this, x);
});

document.body.innerHTML += '<button id="a">클릭</button>';
document.body.querySelector('#a').addEventListener('click', function(e) {				// (3)
  console.log(this, e);
});
```

위 예제는 대표적인 콜백 함수다. 순서대로 살펴보면 

(1): setTimeout 함수는 300ms 만큼 지연을 한 뒤 콜백함수를 실행하라는 명령이다. 0.3초 뒤에 전역객체가 출력된다.

(2): `forEach` 메서드는 배열의 각 요소를 앞에서부터 차례로 하나씩 꺼내어 그 값을 콜백 함수의 첫 번째 인자로 삼아 함수를 실행하라는 명령이다. 전역객체와 배열의 각 요소가 5회 출력된다.

(3): `addEventListener` 는 지정한 HTML 엘리먼트에 'click' 이벤트가 발생할 때마다 그 이벤트 정보를 콜백 함수의 첫 번째 인자로 삼아 함수를 실행하라는 명령이다. 버튼을 클릭하면 앞서 지정한 엘리먼트와 클릭 이벤트에 관한 정보가 담긴 객체가 출력된다.

(1)의 setTimeout 함수와 `forEach`메서드는 그 내부에서 콜백 함수를 호출할 때 대상이 될 `this` 를 지정하지 않았다. 따라서 콜백 함수 내부에서의 `this` 는 전역객체를 참조한다. 한편 (3)의 `addEventListener` 메서드는 콜백 함수를 호출할 때 자신의 `this` 를 상속하도록 정의돼 있다. 그러니까 메서드명의 점(.) 앞부분이 곧 `this` 가 되는 것이다.

이처럼 콜백 함수에서의 `this` 는 '무조건 이것이다.'라고 정의할 수는 없다. 콜백 함수의 제어권을 가지는 함수나 메서드가 콜백 함수에서의 `this` 를 무엇으로 할지를 결정하며, 특별히 정의하지 않은 경우에는 기본적으로 함수와 마찬가지로 전역객체를 바라본다.

#### 1-5 생성자 함수 내부에서의 this

생성자 함수는 어떤 공통된 성질을 지니는 객체들을 생성하는 데 사용하는 함수다. 객체지향 언어에서는 생성자를 클래스, 클래스를 통해 만든 객체를 인스턴스라고 한다. 

현실세계로 비유하자면 '인간'의 공통 특성, 이를테면 직립 보행, 언어 구사, 도구 사용 등을 모아 인간 집합을 정의한 것이 바로 클래스이며, 각 사람들은 인간 클래스에 속하는 인스턴스가 된다. 각 인스턴스들은 위의 인간의 공통 특성을 가지고 있을뿐더러 저마다의 개성도 존재한다. 프로그래밍적으로 '생성자'는 **구체적인 인스턴스를 만들기 위한 일종의 틀**이다. 이 틀에는 해당 클래스의 공통 속성들이 미리 준비돼 있고, 여기에 구체적인 인스턴스의 개성을 더해 개별 인스턴스를 만들 수 있는 것이다.

자바스크립트는 함수에 생성자로서의 역할을 함께 부여했다. `new` 명령어와 함께 함수를 호출하면 해당 함수가 생성자로서 동작하게 된다. 그리고 어떤 함수가 생성자 함수로서 호출된 경우 내부에서의 `this` 는 곧 새로 만들 구체적인 인스턴스 자산이 된다. 생성자 함수를 호출(`new` 명령어와 함께 호출)하면 우선 생성자의 `prototype` 프로퍼티를 참조하는 `__proto__` 라는 프로퍼티가 있는 객체(인스턴스)를 만들고, 미리 준비된 공통 속성 및 개성을 해당 객체(this)에 부여한다. 이렇게 해서 구체적인 인스턴스가 만들어지는 것이다.

**3-13** 생성자 함수

```javascript
var Cat = function(name, age) {
  this.bark = '야옹';
  this.name = name;
  this.age = age;
};
var choco = new Cat('초코', 7);
var nabi = new Cat('나비', 5);
console.log(choco, nabi);

/* 결과
Cat { bark: '야옹', name: '초코', age: 7 }
Cat { bark: '야옹', name: '나비', age: 5 }
*/
```

Cat이라는 변수에 익명함수를 할당했다. 이 함수 내부에서는 `this` 에 접근해서 `bark`, `name`, `age` 프로퍼티에 각각 값을 대입한다. 6번째 줄과 7번째 줄에서는 `new` 명령어와 함께 Cat 함수를 호출해서 변수 `choco`, `nabi` 에 각각 할당했다. 8번째 줄에서 `choco`, `nabi` 를 출력해보면 각각 Cat 클래스의 인스턴스 객체가 출력이 된다. 7번째 줄에서 실행한 생성자 함수 내부에서의 `this` 는 `nabi` 인스턴스를 가리킴을 알 수 있다.

### 2. 명시적으로 this를 바인딩하는 방법

앞 절에서는 상황별로 `this` 에 어떤 값이 바인딩되는지를 살펴봤지만 이러한 규칙을 깨고 `this` 에 별도의 대상을 바인딩하는 방법도 있다. 앞에서 얘기했던 규칙에 부합하지 않으면 다음 방법 중 하나를 사용했을 것이라고 추측할 수 있다.

#### 2-1 call 메서드

[MDN](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Function/call)

`call` 메서드는 메서드의 호출 주체인 함수를 즉시 실행하도록 하는 명령이다. 이때 `call` 메서드의 첫 번째 인자를 `this`로 바인딩하고, 이후 인자들을 호출할 함수의 매개변수로 한다. 함수를 그냥 실행하면 `this` 는 전역객체를 참조하지만 `call` 메서드를 이용하면 임의의 객체를 `this`로 지정할 수 있다.

**3-14**  `call` 메서드

```javascript
var func = function(a, b, c) {
  console.log(this, a, b, c);
};

func(1, 2, 3); // Window{ ... } 1 2 3
func.call({ x: 1 }, 4, 5, 6); // { x: 1 } 4 5 6
```

메서드에 대해서도 마찬가지로 객체의 메서드를 그냥 호출하면 `this` 는 객체를 참조하지만 `call` 메서드를 이용하면 임의의 객체를 `this`로 지정할 수 ㅣ있다.

**3-15**  `call` 메서드(2)

```javascript
var obj = {
  a: 1,
  method: function(x, y) {
    console.log(this.a, x, y);
  },
};

obj.method(2, 3); // 1 2 3
obj.method.call({ a: 4 }, 5, 6); // 4 5 6
```

#### 2-2 apply 메서드

`apply` 메서드는 기능적으로 `call` 메서드와 완전히 동일하다. `call` 메서드는 첫 번째 인자를 제외한 나머지 모든 인자들을 호출할 함수의 매개변수로 지정하는 반면, `apply` 메서드는 **두 번째 인자를 배열**로 받아 그 배열의 요소들을 호출할 함수의 매개변수로 지정한다는 점에서만 차이가 있다.

**3-16**  `apply` 메서드

```javascript
var func = function(a, b, c) {
  console.log(this, a, b, c);
};
func.apply({ x: 1 }, [4, 5, 6]); // { x: 1 } 4 5 6

var obj = {
  a: 1,
  method: function(x, y) {
    console.log(this.a, x, y);
  },
};
obj.method.apply({ a: 4 }, [5, 6]); // 4 5 6
```

#### 2-3 call/apply 메서드의 활용

`call` 이나 `apply` 메서드를 잘 활용하면 자바스크립트를 더욱 다채롭게 사용할 수 있다. 아래의 몇 가지 예시를 통해 알아보자.

**유사배열객체(array-like object)에 배열 메서드를 적용**

**3-17** call/apply 메서드의 활용1-1) 유사배열객체(array-like object)에 배열 메서드를 적용 

```javascript
var obj = {
  0: 'a',
  1: 'b',
  2: 'c',
  length: 3,
};
Array.prototype.push.call(obj, 'd');
console.log(obj); // { 0: 'a', 1: 'b', 2: 'c', 3: 'd', length: 4 }

var arr = Array.prototype.slice.call(obj);
console.log(arr); // [ 'a', 'b', 'c', 'd' ]
```

먼저 객체에는 배열메서드를 직접 적용할 수 없다. 그러나 **키가 0 또는 양의 정수인 프로퍼티가 존재하고** `length` **프로퍼티의 값이 0 또는 양의 정수** 인 객체, 즉 배열의 구조와 유사한 객체의 경우(유사배열객체) `call` 또는 `apply` 메서드를 이용해 배열 메서드를 차용할 수 있다. 7번째 줄에서는 배열 메서드인 `push` 를 객체 obj에 적용해 프로퍼티 3에 'd'를 추가했다. 9번째 줄에서는 `slice` 메서드를 적용해 객체를 배열로 전환했다. `slice` 메서드는 원래 시작 인덱스값과 마지막 인덱스값을 받아 시작값부터 마지막값의 앞부분까지의 배열 요소를 추출하는 메서드인데, 매개변수를 아무것도 넘기지 않을 경우에는 그냥 **원본 배열의 얕은 복사본을 반환한다.** 그러니까 `call` 메서드를 이용해 원본인 유사배열객체의 얕은 복사를 수행한 것인데, `slice` 메서드가 배열 메서드이기 때문에 복사본은 배열로 반환하게 된 것이다. 함수 내부에서 접근할 수 있는 arguments 객체도 유사배열객체이므로 위의 방법으로 배열로 전환해서 활용할 수 있다. `querySelectorAll` , `getElementsByClassname` 등의 `Node` 선택자로 선택한 결과인 `NodeList` 도 마찬가지다.

**3-18** call/apply 메서드의 활용1-2) arguments, NodeList에 배열 메서드를 적용

```javascript
function a() {
  var argv = Array.prototype.slice.call(arguments);
  argv.forEach(function(arg) {
    console.log(arg);
  });
}
a(1, 2, 3);

document.body.innerHTML = '<div>a</div><div>b</div><div>c</div>';
var nodeList = document.querySelectorAll('div');
var nodeArr = Array.prototype.slice.call(nodeList);
nodeArr.forEach(function(node) {
  console.log(node);
});
```

그 밖에도 유사배열객체에는 `call/apply` 메서드를 이용해 모든 배열 메서드를 적용할 수 있다. 배열처럼 인덱스와 `length` 프로퍼티를 지니는 문자열에 대해서도 마찬가지다. 단, 문자열의 경우 `length` 프로퍼티가 읽기 전용이기 때문에 원본 문자열에 변경을 가하는 메서드(`push`, `pop`, `shift`, `unshift`, `splice` 등)는 에러를 던지며, `concat` 처럼 대상이 반드시 배열이어야 하는 경우에는 에러는 나지 않지만 제대로된 결과를 얻을 수 없다.

**3-19** call/apply 메서드의 활용1-3) 문자열에 배열 메서드 적용 예시 

```javascript
var str = 'abc def';

Array.prototype.push.call(str, ', pushed string');
// Error: Cannot assign to read only property 'length' of object [object String]

Array.prototype.concat.call(str, 'string'); // [String {"abc def"}, "string"]

Array.prototype.every.call(str, function(char) {
  return char !== ' ';
}); // false

Array.prototype.some.call(str, function(char) {
  return char === ' ';
}); // true

var newArr = Array.prototype.map.call(str, function(char) {
  return char + '!';
});
console.log(newArr); // ['a!', 'b!', 'c!', ' !', 'd!', 'e!', 'f!']

var newStr = Array.prototype.reduce.apply(str, [
  function(string, char, i) {
    return string + char + i;
  },
  '',
]);
console.log(newStr); // "a0b1c2 3d4e5f6"
```

이렇게 `call/apply` 를 이용해 형변환하는 것은 '`this`를 원하는 값으로 지정해서 호출한다.' 라는 본래의 메서드의 의도와는 다소 동떨어진 활용법이라고 할 수 있다. `slice` 메서드는 오직 배열 형태로 '복사'하기 위해 차용됐을 뿐이니, 이러한 경험을 해본 사람이 아니고서는 의도를 파악하기 어려울 수 있다. 이에 ES6에서는 유사배열객체 또는 순회 가능한 모든 종류의 데이터 타입을 배열로 전환하는 [Array.from](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/from) 메서드를 새로 도입했다.

**3-20** call/apply 메서드의 활용1-3) ES6의 Array.from 메서드 

```javascript
var obj = {
  0: 'a',
  1: 'b',
  2: 'c',
  length: 3,
};
var arr = Array.from(obj);
console.log(arr); // ['a', 'b', 'c']
```

**생성자 내부에서 다른 생성자를 호출**

생성자 내부에 다른 생성자와 공통된 내용이 있을 경우 `call` 또는 `apply` 를 이용해 다른 생성자를 호출하면 간단하게 반복을 줄일 수 있다. 다음 예제를 살펴보자.

**3-21** call/apply 메서드의 활용 2) 생성자 내부에서 다른 생성자를 호출

```javascript
function Person(name, gender) {
  this.name = name;
  this.gender = gender;
}
function Student(name, gender, school) {
  Person.call(this, name, gender);
  this.school = school;
}
function Employee(name, gender, company) {
  Person.apply(this, [name, gender]);
  this.company = company;
}
var by = new Student('보영', 'female', '단국대');
var jn = new Employee('재난', 'male', '구골');
```

**여러 인수를 묶어 하나의 배열로 전달하고 싶을때 - apply 활용**

여러 개의 인수를 받는 메서드에게 하나의 배열로 인수들을 전달하고 싶을 때 `apply` 메서드를 사용하면 좋다. 예를 들어, 배열에서 최대/최솟값을 구해야 할 경우 `apply` 메서드를 사용하지 않는다면 아래와 같은 방식으로 구현할 수밖에 없을 것이다.

**3-22** call/apply 메서드의 활용 3-1) 최대/최솟값을 구하는 코드를 직접 구현

```javascript
var numbers = [10, 20, 3, 16, 45];
var max = (min = numbers[0]);
numbers.forEach(function(number) {
  if (number > max) {
    max = number;
  }
  if (number < min) {
    min = number;
  }
});
console.log(max, min); // 45 3
```

코드가 길고 가독성 또한 떨어진다. 이보다는 `Math.max/Math.min` 메서드에 `apply` 를 적용하면 훨씬 간단해진다.

**3-23** call/apply 메서드의 활용 3-2) 여러 인수를 받는 메서드(Math.max/Math.min)에 apply 적용

```javascript
var numbers = [10, 20, 3, 16, 45];
var max = Math.max.apply(null, numbers);
var min = Math.min.apply(null, numbers);
console.log(max, min); // 45 3
```

ES6에서는 펼치기 연산자(spread operator)를 사용하면 훨씬 간편하게 작성할 수 있다.

**3-24** call/apply 메서드의 활용 3-3) ES6의 펼치기 연산자 활용

```javascript
const numbers = [10, 20, 3, 16, 45];
const max = Math.max(...numbers);
const min = Math.min(...numbers);
console.log(max, min); // 45 3
```

`call/apply` 메서드는 명시적으로 별도의 `this` 를 바인딩하면서 함수 또는 메서드를 실행하는 훌륭한 방법이지만 오히려 이로 인해 `this` 를 예측하기 어렵게 만들어 코드 해석을 방해한다는 단점이 있다. 하지만 ES5 이하의 환경에서는 마땅한 대안이 없기때문에 실무에서 광범위하게 사용되고 있다고 한다.