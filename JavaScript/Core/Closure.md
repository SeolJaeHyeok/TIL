# Closure

### 1. 클로저의 의미 및 원리

클로저(Closure)는 여러 함수형 프로그래밍 언어에서 등장하는 보편적인 특성이다. 자바스크립트 고유의 개념이 아니라서 ECMAScript 명세에서도 클로저의 정의를 다루지 않고, 여러 다양한 문헌에서도 제각각 클로저를 다르게 정의 또는 설명하고 있다. 더구나 클로저를 설명하는 문장 자체도 이해하기 어려운 단어가 등장하는 경우가 많다. 다양한 서적에서 언급하는 클로저를 요약하는 부분을 보게 되면 아래와 같다.

- 자신을 내포하는 함수의 컨텍스트에 접근할 수 있는 함수 - 더글라스 크록포드, <자바스크립트 핵심 가이드>
- 함수가 특정 스코프에 접근할 수 있도록 의도적으로 그 스코프에서 정의하는 것 - 에단 브라운, <러닝 자바스크립트>
- 함수를 선언할 때 만들어지는 유효범위가 사라진 후에도 호출할 수 있는 함수 - 존 레식, <자바스크립트 닌자 비급>
- 이미 생명 주기상 끝난 외부 함수의 변수를 참조하는 함수 - 송현주, 고현주, <인사이드 자바스크립트>
- 자유변수가 있는 함수와 자유변수를 알 수 있는 환경의 결합 - 에릭 프리먼, <**Head First Javascript Programming**>
- 로컬 변수를 참조하고 있는 함수 내의 함수 - 야마다 요시히로, <자바스크립트 마스터북>
- 자신이 생성될 때의 스코프에서 알 수 있었던 변수들 중 언젠가 자신이 실행될 때 사용할 변수들만을 기억하여 유지시키는 함수 - 유인동, <함수형 자바스크립트 프로그래밍>

그 밖에도 매우 많은 책에서 대부분 위와 같은 정의와 함께 자세한 설명을 이어나가고는 있지만, 문장만 놓고 이해할 수 있는 사례보다는 그렇지 않은 사례가 더 많다. 이번 장에서는 클로저의 일반적인 정의로부터 그 의미를 파악하고 다양한 사례를 통해 성질을 살펴본 후, 마지막에 다시 재조합해서 이해하기 쉬운 문장으로 바꿔보는 방식으로 진행해보자.

[MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures#closure)에서는 클로저에 대해 "A *closure* is the combination of a function and the lexical environment within which that function was declared." 라고 소개한다. 해석해보면, "클로저는 함수와 그 함수가 선언될 당시의 lexical environment의 상호관계에 따른 현상" 정도로 해석할 수 있다.

"선언될 당시의 lexical environment"는 2장에서 소개한 실행 컨텍스트의 구성 요소 중 하나인 `outerEnvironmentReference` 에 해당한다.  `LexicalEnvironment`의  `environmentRecord` 와  `outerEnvironmentReference` 에 의해 변수의 유효범위인 스코프가 결정되고 스코프 체인이 가능해진다고 했었다. 어떤 컨텍스트 A에서 선언한 내부함수 B의 실행 컨텍스트가 활성화된 시점에는 B의  `outerEnvironmentReference` 가 참조하는 대상인 A의  `LexicalEnvironment` 에도 접근이 가능하다. 다시 말해, A는 B에서 선언한 변수에 접근할 수 없지만 B에서는 A에서 선언한 변수에 접근이 가능하다.

여기서 'combination'의 의미를 파악할 수 있다. 내부함수 B가 A의  `LexicalEnvironment` 를 언제나 사용하는 것은 아니다. 내부함수에서 외부 변수를 참조하지 않는 경우라면 combination이라고 할 수 없다. 내부함수에서 외부 변수를 참조하는 경우에 한해서만 combination, 즉 '선언될 당시의  `LexicalEnvironment` 와의 상호관계'가 의미가 있을 것이다.

지금까지 파악한 내용에 따르면 클로저란 '어떤 함수에서 선언한 변수를 참조한느 내부함수에서만 발생하는 현상'이라고 볼 수 있다. 예제를 통해 명확하게 만들어보자. 우선 외부함수에서 변수를 선언하고 내부함수에서 해당 변수를 참조하는 형태의 간단한 코드를 작성한다.

**5-1** 외부 함수의 변수를 참조하는 내부 함수(1)

```javascript
var outer = function() {
  var a = 1;
  var inner = function() {
    console.log(++a);
  };
  inner();
};
outer();
```

위 예제에서는 `outer` 함수에서 변수 `a`를 선언했고, `outer`의 내부 함수인 `inner` 함수에서 `a` 의 값을 1만큼 증가시킨 다음 출력한다. `inner` 함수 내부에서는 `a` 를 선언하지 않았기 때문에 `environmentRecord` 에서 값을 찾지 못하므로 `outerEnvironmentReference` 에 지정된 상위 컨텍스트인 `outer` 의 `LexicalEnvironment` 에 접근해서 다시 `a` 를 찾는다. 그런 다음 `outer` 함수 내에 선언된 `a` 를 발견하고 4번째 줄에서 2를 출력한다. `outer` 함수의 실행 컨텍스트가 종료되면 `LexicalEnvironment` 에 저장된 식별자들(`a`, `inner`)에 대한 참조를 지운다. 그러면 각 주소에 저장돼 있던 값들은 자신을 참조하는 변수가 하나도 없게 되므로 가비지 컬렉터의 수집 대상이 될 것이다.

**5-2** 외부 함수의 변수를 참조하는 내부 함수(2)

```javascript
var outer = function() {
  var a = 1;
  var inner = function() {
    return ++a;
  };
  return inner();
};
var outer2 = outer();
console.log(outer2); // 2
```

이번에도 `inner` 함수 내부에서 외부변수인 `a` 를 사용했다. 그런데 6번째 줄에서는 `inner` 함수를 실행한 결과를 리턴하고 있으므로 결과적으로 `outer` 함수의 실행 컨텍스트가 종료된 시점에는 `a` 변수를 참조하는 대상이 없어진다. 예제 5-1과 마찬가지로 `a`, `inner` 변수의 값들은 언젠가 가비지 컬렉터에 의해 소멸할 것이다. 이 역시 일반적인 함수 및 내부함수에서의 동작과 차이가 없다.

예제 5-1과 5-2는 `outer` 함수의 실행 컨텍스트가 종료되기 이전에 `inner` 함수의 실행 컨텍스트가 종료돼 있으며, 이후 별도로 `inner` 함수를 호출할 수 없다는 공통점이 있다. 그렇다면 `outer` 의 실행 컨텍스트가 종료된 이후에도 `inner` 함수를 호출할 수 있게 만들면 어떨까?

**5-3** 외부 함수의 변수를 참조하는 내부 함수(3)

```javascript
var outer = function() {
  var a = 1;
  var inner = function() {
    return ++a;
  };
  return inner;
};
var outer2 = outer();
console.log(outer2()); // 2
console.log(outer2()); // 3
```

이번에는 6번째 줄에서 `inner` 함수의 실행 결과가 아닌 `inner` 함수 자체를 반환했다. 그러면 `outer` 함수의 실행 컨텍스트가 종료될 때(8번째 줄) `outer2` 변수는 `outer` 의 실행 결과인 `inner` 함수를 참조하게 될 것이다. 이후 9번째 줄에서 `outer2` 를 호출하면 앞서 반환된 함수인 `inner` 가 실행된다.

`inner` 함수의 실행 컨텍스트의 `environmentRecord` 에는 수집할 정보가 없다. `outerEnvironmentReference` 에는 `inner` 함수가 선언된 위치의 `LexicalEnvironment` 가 참조복사 된다. `inner` 함수는 `outer` 함수 내부에서 선언됐으므로, `outer` 함수의 `LexicalEnvironment` 가 담길 것이다. 이제 스코프 체이닝에 따라 `outer` 에서 선언한 변수 `a` 에 접근해서 1만큼 증가시킨 후 그 값이 2를 반환하고, `inner` 함수의 실행 컨텍스트가 종료된다. 10번째 중에서 다시 `outer2` 를 호출하면 같은 방식으로 `a` 의 값을 2에서 3으로 1 증가시킨 후 3을 반환한다.

여기서 의문점이 있다. `inner` 함수의 실행 시점에는 이미 `outer` 함수는 실행이 종료된 상태인데 `outer` 함수의 `LexicalEnvironment` 에는 어떻게 접근할 수 있는걸까? 이는 가비지 컬렉터의 동작 방식 때문이다. **가비지 컬렉터는 어떤 값을 참조하는 변수가 하나라도 있다면 그 값은 수집 대상에서 제외시킨다.** 위 예제의 `outer` 함수는 실행 종료시점에 `inner` 함수를 반환한다. 외부함수인 `outer` 의 실행이 종료되더라도 내부함수인 `inner` 는 언젠가 `outer2` 를 실행함으로써 호출될 가능성이 생긴 것이고 언젠가 `inner` 함수의 실행 컨텍스트가 활성화되면 `outerEnvironmentReference` 가 `outer` 함수의 `LexicalEnvironment` 를 필요로 할 것이므로 수집 대상에서 제외된다. 그 덕에 `inner` 함수가 이 변수에 접근할 수 있는 것이다.

정리하자면 **어떤 함수의 lexicalEnvironment가 이를 '참조할' 예정인 다른 실행 컨텍스트가 있는 한 실행 종료 이후에도 GC되지 않는다는 것이다.**

클로저는 어떤 함수에서 선언한 변수를 참조하는 내부함수에서만 발생하는 현상이라고 말했다. 예제 5-1과 5-2에서는 일반적인 함수의 경우와 마찬가지로 `outer` 의 `LexicalEnvironment` 에 속하는 변수가 모두 가비지 컬렉팅 대상에 포함된 반면, 예제 5-2의 경우 변수 `a` 가 대상에서 제외됐다. 이처럼 함수의 실행 컨텍스트가 종료된 후에도 `LexicalEnvironment` 가 가비지 컬렉터의 수집 대상에서 제외되는 경우는 5-3과 같이 지역 변수를 참조하는 내부함수가 외부로 전달된 경우가 유일하다. 그러니까 "어떤 함수에서 선언한 변수를 참조하는 내부함수에서만 발생하는 현상" 이란 "외부 함수의 `LexicalEnvironment` 가 가비지 컬렉팅되지 않는 현상"을 말하는 것이다.

이를 바탕으로 위에서 정의했던 클로저의 정의를 고쳐보면 다음과 같다.

**클로저란 어떤 함수 A에서 선언한 변수 `a`를 참조하는 내부함수 B를 외부로 전달할 경우 A의 실행 컨텍스트가 종료된 이후에도 변수 `a`가 사라지지 않는 현상**을 말한다. 앞서 살펴본 여러 서적에서 다룬 클로저의 정의 중 이와 가장 근접한 것을 보면

- 함수를 선언할 때 만들어지는 유효범위가 사라진 후에도 호출할 수 있는 함수 - 존 레식, <자바스크립트 닌자 비급>
- 이미 생명 주기상 끝난 외부 함수의 변수를 참조하는 함수 - 송현주, 고현주, <인사이드 자바스크립트>
- 자신이 생성될 때의 스코프에서 알 수 있었던 변수들 중 언젠가 자신이 실행될 때 사용할 변수들만을 기억하여 유지시키는 함수 - 유인동, <함수형 자바스크립트 프로그래밍>

위 세 가지의 정의가 클로저의 정의와 근접하다고 볼 수 있다.

> 🖍 저자의 생각
>
> 통상적으로 위 정의처럼 클로저 현상이 발생하는 함수 자체를 클로저라고 칭하더라도 의미를 통하므로 문제가 되지는 않는다. 하지만 개념상의 클로저와 의미론적으로 일치하는 실제적인 클로저가 무엇인지에 대해 생각해볼 필요가 있다.
>
> 개념적으로 클로저는 어떤 상황에서만 발생하는 특수한 '현상'을 의미한다. 함수는 이 현상이 나타나기 위한 '조건'에 해당하지만, 그 현상을 구체화한 '대상'으로 볼 수 없다. 따라서 실제적인 클로저는 '클로저 현상에 의해 메모리에 남겨진 변수들의 집합'을 지칭하는 것으로 이해하는 것이 좀 더 정확할 것이다.

여기서 한가지 주의할 점이 있다. 바로 '외부로 전달'이 곧 `return` 만을 의미하는 것은 아니라는 점이다.

**5-4** return 없이도 클로저가 발생하는 다양한 경우

```javascript
// (1) setInterval/setTimeout
(function() {
  var a = 0;
  var intervalId = null;
  var inner = function() {
    if (++a >= 10) {
      clearInterval(intervalId);
    }
    console.log(a);
  };
  intervalId = setInterval(inner, 1000);
})();
```

```javascript
// (2) eventListener
(function() {
  var count = 0;
  var button = document.createElement('button');
  button.innerText = 'click';
  button.addEventListener('click', function() {
    console.log(++count, 'times clicked');
  });
  document.body.appendChild(button);
})();
```

(1) 은 별도의 외부객체인 `window` 의 메서드(`setTimeout` 또는 `setInterval` )에 전달할 콜백 함수 내부에서 지역변수를 참조한다. (2)는 별도의 외부객체인 DOM의 메서드(`addEventListener`) 에 등록할 `handler` 함수 내부에서 지역변수를 참조한다. 두 상황 모두 지역변수를 참조하는 내부함수를 외부에 전달했기 때문에 클로저다.

### 2. 클로저와 메모리 관리

클로저는 객체지향과 함수형 모두를 아우르는 매우 중요한 개념이다. 메모리 누수의 위험을 이유로 클로저 사용을 조심해야 한다거나 심지어 지양해야 한다고 주장하는 사람들도 있지만 메모리 소모는 클로저의 본질적인 특성일 뿐이다. 오히려 이러한 특성을 정확히 이해하고 잘 활용할도록 노력해야 한다. '메모리 누수'라는 표현은 개발자의 의도와 달리 어떤 값의 참조 카운트가 0이 되지 않아 GC의 수거 대상이 되지 않게 설계한 경우는 '누수'라고 할 수 없을 것이다.

과거에는 의도치 않게 누수가 발생하는 여러 가지 상황들(순환 참조, 익스플로러의 이벤트 핸들러 등)이 있었지만 그중 대부분은 최근의 자바스크립트 엔진에서는 발생하지 않거나 거의 발견하기 힘들어졌으므로 이제는 의도대로 설계한 '메모리 소모'에 대한 관리법만 잘 파악해서 적용하는 것으로 충분하다.

관리 방법은 정말 간단하다. 클로저는 어떤 필요에 의해 의도적으로 함수의 지역변수를 메모리를 소모하도록 함으로써 발생한다. 그렇다면 그 필요성이 사라진 시점에는 더는 메모리를 소모하지 않게 해주면 된다. 참조 카운트를 0으로 만들면 언젠가 GC가 수거해갈 것이고, 이때 소모됐던 메모리가 회수될 것이다. 

그렇다면 참조 카운트를 0으로 만드는 방법은 무엇일까? 이는 식별자에 참조형이 아닌 기본형 데이터(보통 `null` 이나 `undefined`)를 할당하면 된다. 다음은 예제 5-3과 5-4에 메모리 해제 코드를 추가한 예제다.

**5-5** 클로저의 메모리 관리

```javascript
// (1) return에 의한 클로저의 메모리 해제
var outer = (function() {
  var a = 1;
  var inner = function() {
    return ++a;
  };
  return inner;
})();
console.log(outer());
console.log(outer());
outer = null; // outer 식별자의 inner 함수 참조를 끊음
```

```javascript
// (2) setInterval에 의한 클로저의 메모리 해제
(function() {
  var a = 0;
  var intervalId = null;
  var inner = function() {
    if (++a >= 10) {
      clearInterval(intervalId);
      inner = null; // inner 식별자의 함수 참조를 끊음
    }
    console.log(a);
  };
  intervalId = setInterval(inner, 1000);
})();
```

```javascript
// (3) eventListener에 의한 클로저의 메모리 해제
(function() {
  var count = 0;
  var button = document.createElement('button');
  button.innerText = 'click';

  var clickHandler = function() {
    console.log(++count, 'times clicked');
    if (count >= 10) {
      button.removeEventListener('click', clickHandler);
      clickHandler = null; // clickHandler 식별자의 함수 참조를 끊음
    }
  };
  button.addEventListener('click', clickHandler);
  document.body.appendChild(button);
})();
```

