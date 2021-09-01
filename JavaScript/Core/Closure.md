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

클로저는 어떤 함수에서 선언한 변수를 참조하는 내부함수에서만 발생하는 현상이라고 말했다. 예제 5-1과 5-2에서는 일반적인 함수의 경우와 마찬가지로 `outer` 의 `LexicalEnvironment` 에 속하는 변수가 모두 가비지 컬렉팅 대상에 포함된 반면, 예제 5-3의 경우 변수 `a` 가 대상에서 제외됐다. **이처럼 함수의 실행 컨텍스트가 종료된 후에도 `LexicalEnvironment` 가 가비지 컬렉터의 수집 대상에서 제외되는 경우는 5-3과 같이 지역 변수를 참조하는 내부함수가 외부로 전달된 경우가 유일하다.** 그러니까 "어떤 함수에서 선언한 변수를 참조하는 내부함수에서만 발생하는 현상" 이란 "외부 함수의 `LexicalEnvironment` 가 가비지 컬렉팅되지 않는 현상"을 말하는 것이다.

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

### 3. 클로저의 활용 사례

#### 5-3-1 콜백 함수 내부에서 외부 데이터를 사용하고자 할 때

다음은 대표적인 콜백 함수 중 하나인 이벤트 리스너에 관한 예시다. 클로저의 '외부 데이터'에 주목하면서 흐름을 따라가 보자.

**5-6** 콜백 함수와 클로저(1)

```javascript
var fruits = ['apple', 'banana', 'peach'];
var $ul = document.createElement('ul'); // (공통 코드)

fruits.forEach(function(fruit) {
  // (A)
  var $li = document.createElement('li');
  $li.innerText = fruit;
  $li.addEventListener('click', function() {
    // (B)
    alert('your choice is ' + fruit);
  });
  $ul.appendChild($li);
});
document.body.appendChild($ul);
```

위 예제에서는 `fruits` 변수를 순회하면 `li` 를 생성하고, 각 `li` 를 클릭하면 해당 리스너에 기억된 콜백 함수를 실행하게 했다. 4번째 줄의 `forEach` 메서드에 넘겨준 익명의 콜백 함수(A)는 그 내부에서 외부 변수를 사용하고 있지 않으므로 클로저가 없지만, 7번째 줄의 `addEventListener` 에 넘겨준 콜백 함수(B)에는 `fruits` 라는 외부 변수를 참조하고 있으므로 클로저가 있다. (A)는 `fruits` 의 개수만큼 실행되며, 그때마다 새로운 실행 컨텍스트가 활성화될 것이다. A의 실행 종료 여부와 무관하게 클릭 이벤트에 의해 각 컨텍스트의 (B)가 실행될 때는 (B)의 `outerEnvironmentReference` 가 (A)의 `LexicalEnvironment` 를 참조하게 될 것이다. 따라서 최소한 (B) 함수가 참조할 예정인 변수 `fruit` 에 대해서는 (A)가 종료된 이후에도 GC의 수집 대상에서 제외되어 계속 참조가 가능할 것이다.

그런데 (B) 함수의 쓰임새가 콜백 함수에 국한되지 않는 경우라면 반복을 줄이기 위해 (B)를 외부로 분리하는 편이 나을 수 있을 것이다. 즉 `fruit` 을 인자로 받아 출력하는 형태로 바꾸는 것이다.

**5-7** 콜백 함수와 클로저(2)

```javascript
var fruits = ['apple', 'banana', 'peach'];
var $ul = document.createElement('ul');

var alertFruit = function(fruit) {
  alert('your choice is ' + fruit);
};
fruits.forEach(function(fruit) {
  var $li = document.createElement('li');
  $li.innerText = fruit;
  $li.addEventListener('click', alertFruit);
  $ul.appendChild($li);
});
document.body.appendChild($ul);
alertFruit(fruits[1]);
```

위 예제에서는 공통 함수로 쓰고자 콜백 함수를 외부로 꺼내서 `alertFruit` 라는 변수에 담았다. 이제 `alertFruit` 를 직접 실행 할 수 있다. 또한 14번째 줄에서는 정상적으로 `banana` 에 대한 `alert` 이 실행된다. 그런데 각 `li` 를 클릭하면 클릭한 대상의 과일명이 아닌 `[object MouseEvent]` 라는 값이 출력되는데 이는 콜백 함수의 인자에 대한 제어권을 `addEventListener` 가 가진 상태이며, `addEventListener` 는 콜백 함수를 호출할 때 첫 번째 인자에 '이벤트 객체'를 주입하기 때문이다. 이 문제는 `bind` 메서드를 활용하면 손쉽게 해결할 수 있다.

**5-8** 콜백 함수와 클로저(3)

```javascript
var fruits = ['apple', 'banana', 'peach'];
var $ul = document.createElement('ul');

var alertFruit = function(fruit) {
  alert('your choice is ' + fruit);
};
fruits.forEach(function(fruit) {
  var $li = document.createElement('li');
  $li.innerText = fruit;
  $li.addEventListener('click', alertFruit.bind(null, fruit));
  $ul.appendChild($li);
});
document.body.appendChild($ul);
```

다만 이렇게 하면 이벤트 객체가 인자로 넘어오는 순서가 바뀌는 점 및 함수 내부에서의 `this` 가 원래의 그것과 달라지는 점은 감안해야 한다 (`bind` 메서드의 첫 번째 인자가 바로 새로 바인딩할 `this` 인데 이 값을 생략할 수 없기 때문에 일반적으로 원래의 `this` 를 유지하도록 할 수 없는 경우가 많다. 또한 예제에서는 두 번째 인자에 이벤트 객체가 넘어올 것이다).

이런 변경사항이 발생하지 않게끔 하면서 이슈를 해결하기 위해서는 `bind` 메서드가 아닌 다른 방식으로 풀어내야만하는데 고차함수를 활용하는 것으로 해결할 수 있다.

**5-9** 콜백 함수와 클로저(4)

```javascript
var fruits = ['apple', 'banana', 'peach'];
var $ul = document.createElement('ul');

var alertFruitBuilder = function(fruit) {
  return function() {
    alert('your choice is ' + fruit);
  };
};
fruits.forEach(function(fruit) {
  var $li = document.createElement('li');
  $li.innerText = fruit;
  $li.addEventListener('click', alertFruitBuilder(fruit));
  $ul.appendChild($li);
});
document.body.appendChild($ul);
```

4번째 줄에서 `alertFruit` 함수 대신 `alertFruitBuilder` 라는 이름의 함수를 작성해줬다. 이 함수 내부에서는 다시 익명함수를 반환하는데, 이 익명함수가 바로 기존의 `alertFruit` 함수다. 12번째 줄에서는 `alertFruitBuilder` 함수를 실행하면서 `fruit` 값을 인자로 전달했다. 그러면 이 함수의 실행 결과가 다시 함수가 되며, 이렇게 반환된 함수를 리스너에 콜백 함수로써 전달한 것이다. 이후 언젠가 클릭 이벤트가 발생하면 비로소 이 함수의 실행 컨텍스트가 열리면서 `alertFruitBuilder` 의 인자로 넘어온 `fruilt` 를 `outerEnvironmentReference` 에 의해 참조할 수 있을 것이다. 즉 `alertFruitBuilder` 의 실행 결과로 반환된 함수에는 클로저가 존재한다.

정리하면 예제 5-6은 콜백 함수를 내부함수로 선언해서 외부변수를 직접 참조하는 방법으로, 클로저를 사용한 방법이었다. 예제 5-8은 `bind` 를 활용했는데, `bind` 메서드로 값을 직접 넘겨준 덕분에 클로저는 발생하지 않게 된 반면 여러 가지 제약사항이 따르게 됐다. 예제 5-9는 콜백 함수를 고차함수로 바꿔서 클로저를 적극적으로 활용한 방안이었다. 세 가지 방법 모두 각기 다른 장단점이 존재하는 방법들이기 때문에 어떤 방식을 도입하는 것이 좋을지는 고민을 해봐야 할 것이다.

#### 5-3-2 접근 권한 제어(정보 은닉)

정보 은닉(information hiding)은 어떤 모듀의 내부 로직에 대해 외부로의 노출을 최소화해서 모듈간의 결합도를 낮추고 유연성을 높이고자 하는 현대 프로그래밍 언어의 중요한 개념 중 하나다. 흔히 접근 권한에는 `public`, `private`, `protected` 의 세 종류가 있다. 각 단어는 의미 그대로, `public` 외부에서 접근 가능한 것이고, `private` 내부에서만 사용하며 외부에 노출되지 않는 것을 의미한다.

자바스크립트는 기본적으로 변수 자체에 이런한 접근 권한을 직접 부여하도록 설계돼 있지 않다. 그렇다고 접근 권한 제어가 불가능한 것은 아니다. 클로저를 이용하면 함수 차원에서 `public` 한 값과 `private` 한 값을 구분하는 것이 가능하다. 

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

예제 5-3을 다시 보면 `outer` 함수를 종료할 때 `inner` 함수를 반환함으로써 `outer` 함수의 지역변수인 `a` 의 값을 외부에서도 읽을수 있게 됐다. 이처럼 클로저를 활용하면 외부 스코프에서 함수 내부의 변수들 중 선택적으로 일부의 변수에 대한 접근 권한을 부여할 수 있는데 이는   `return` 을 활용하면 된다.

closure라는 영어 단어는 사전적으로 '닫혀있음, 폐쇄성, 완결성' 정도의 의미를 가진다. 이 폐쇄성에 주목하면 위 예제를 조금 다르게 받아들일 수 있다.  `outer` 함수는 외부(전역 스코프)로부터 철저하게 격리된 공간이다. 외부에서는 외부 공간에 노출돼 있는 `outer` 라는 변수를 통해 `outer` 함수를 실행할 수 있지만, `outer` 함수 내부에는 어떠한 개입도 할 수 없다. 외부에서는 오직 `outer` 함수가 `return` 한 정보에만 접근할 수 있는 것이다. 즉, `return` 값이 외부에 정보를 제공하는 유일한 수단인 것이다.

그러니까 외부에 제공하고자 하는 정보들을 모아서 `return` 하고 내부에서만 사용할 정보들은 `return` 하지 않는 것으로 접근 권한 제어가 가능한 것이다. `return` 한 변수들은 공개 멤버(public member)가 되고, 그렇지 않은 변수들은 비공개 멤버(private member)가 되는 것이다.

접근 권한 제어에 대해 알아보기 위해 간단한 게임을 만들어서 적용해보도록 하자.

> - 각 턴마다 주사위를 굴려 나온 숫자(km)만큼 이동
> - 차량별로 연료량(fuel)과 연비(power)는 무작위로 생성
> - 남은 연료가 이동할 거리에 필요한 연료보다 부족하면 이동하지 못함
> - 모든 유저가 이동할 수 없는 턴에 게임이 종료
> - 게임 종료 시점에 가장 멀리 이동해 있는 사람이 승리

위 규칙에 따라 간단한 자동차 객체를 만들어 준다.

```javascript
var car = {
  fuel: Math.ceil(Math.random() * 10 + 10), // 연료(L)
  power: Math.ceil(Math.random() * 3 + 2), // 연비(km/L)
  moved: 0, // 총 이동거리
  run: function() {
    var km = Math.ceil(Math.random() * 6);
    var wasteFuel = km / this.power;
    if (this.fuel < wasteFuel) {
      console.log('이동불가');
      return;
    }
    this.fuel -= wasteFuel;
    this.moved += km;
    console.log(km + 'km 이동 (총 ' + this.moved + 'km)');
  },
};
```

`car` 변수에 직접 객체를 할당하였고 `fuel` 과 `power` 는 무작위로 생성하며,  `moved` 라는 프로퍼티에 총 이동거리를 부여했으며, `run` 메서드를 실행할 때마다 `car` 객체의 `fuel`, `moved` 값이 변하게 했다. 이런 `car` 객체를 사람 수만큼 생성해서 각자의 턴에 `run` 을 실행하면 게임을 즐길 수 있다.

모두가 `run` 메서드만 호출한다는 가정하에는 이 정도만으로도 충분하다. 그러나 무작위로 정해지는 연료, 연비, 이동거리 등을 마음대로 바꾼다면 일방적인 게임이 되고 말 것이다. 그렇다면 이렇게 값을 바꾸지 못하도록 방어할 필요가 있을 것이다. 바로 이때 클로저를 활용하면 된다. 즉, 객체가 아닌 함수로 만들고, 필요한 멤버만을 `return` 하는 것이다.

**5-11** 클로저 변수로 보호한 자동차 객체(1)

```javascript
var createCar = function() {
  var fuel = Math.ceil(Math.random() * 10 + 10); // 연료(L)
  var power = Math.ceil(Math.random() * 3 + 2); // 연비(km / L)
  var moved = 0; // 총 이동거리
  return {
    get moved() {
      return moved;
    },
    run: function() {
      var km = Math.ceil(Math.random() * 6);
      var wasteFuel = km / power;
      if (fuel < wasteFuel) {
        console.log('이동불가');
        return;
      }
      fuel -= wasteFuel;
      moved += km;
      console.log(km + 'km 이동 (총 ' + moved + 'km). 남은 연료: ' + fuel);
    },
  };
};
var car = createCar();
```

이번에는 `createCar` 라는 함수를 실행함으로써 객체를 생성하게 했다. `fuel`, `power` 변수는 비공개 멤버로 지정해서 외부에서의 접근을 제한했고, `moved` 변수는 getter만을 부여함으로써 읽기 전용 속성을 부여했다. 이제 외부에서는 오직 `run` 메서드를 실행하는 것과 현재의 `moved` 값을 확인하는 두 가지 동작만 할 수 있다. 그러므로 다음과 같이 값을 변경하고자 하는 시도는 대부분 실패하게 된다.

```javascript
car.run(); // 3km 이동(총 3km). 남은 연료: 17.4
console.log(car.moved); // 3 
console.log(car.fuel); // undefined
console.log(car.power); // undefined

car.fuel = 1000;
console.log(car.fuel); // 1000
car.run(); 							// 1km 이동(총 4km). 남은 연료: 17.2

car.power = 100;
console.log(car.power); // 100
car.run(); 							// 4km 이동(총 8km). 남은 연료: 16.4

car.moved = 1000;
console.log(car.moved); // 8
car.run(); 							// 2km 이동(총 10km). 남은 연료: 16
```

비록 `run` 메서드를 다른 내용으로 덮어씌우는 어뷰징은 여전히 가능한 상태이긴 하지만 앞서의 코드보다는 훨씬 안전한 코드가 됐다. 이런 어뷰징까지 막기 위해서는 객체를 `return` 하기 전에 미리 변경할 수 없게끔 조치를 취해야 한다.

**5-12** 클로저 변수로 보호한 자동차 객체(2)

```javascript
var createCar = function() {
  var fuel = Math.ceil(Math.random() * 10 + 10); // 연료(L)
  var power = Math.ceil(Math.random() * 3 + 2); // 연비(km / L)
  var moved = 0; // 총 이동거리
  var publicMembers = {
    get moved() {
      return moved;
    },
    run: function() {
      var km = Math.ceil(Math.random() * 6);
      var wasteFuel = km / power;
      if (fuel < wasteFuel) {
        console.log('이동불가');
        return;
      }
      fuel -= wasteFuel;
      moved += km;
      console.log(km + 'km 이동 (총 ' + moved + 'km). 남은 연료: ' + fuel);
    },
  };
  Object.freeze(publicMembers); // 객체 동결
  return publicMembers;
};
var car = createCar();
```

정리하면 클로저를 활용해 접근권한을 제어하는 방법은 다음과 같다.

> 1. 함수에서 지역변수 및 내부함수 등을 생성한다.
>
> 2. 외부에 접근권한을 주고자 하는 대상들로 구성된 참조형 데이터(대상이 여럿일 때는 객체 또는 배열, 하나일 때는 함수)를 return 한다.
>
>    -> return한 변수들은 공배 멤버가 되고, 그렇지 않은 변수들은 비공개 멤버가 된다.

#### 5-3-3 부분 적용 함수

부분 적용 함수(partially applied function)란 n개의 인자를 받는 함수에 미리 m개의 인자만 넘겨 기억시켰다가, 나중에 (n-m)개의 인자를 넘기면 비로소 원래 함수의 실행 결과를 얻을 수 있게끔 하는 함수다. `this` 를 바인딩해야 하는 점을 제외하면 앞서 살펴본 `bind` 메서드의 실행결과가 바로 부분 적용 함수다.

**5-13** `bind`  메서드를 활용한 부분 적용 함수

```javascript
var add = function() {
  var result = 0;
  for (var i = 0; i < arguments.length; i++) {
    result += arguments[i];
  }
  return result;
};
var addPartial = add.bind(null, 1, 2, 3, 4, 5);
console.log(addPartial(6, 7, 8, 9, 10)); // 55
```

위 예제의 `addPartial` 함수는 인자 5개를 미리 적용하고, 추후 추가적으로 인자들을 전달하면 모든 인자를 모아 원래의 함수가 실행되는 부분 적용 함수다. `add` 함수는 `this` 를 사용하지 않으므로 `bind` 메서드만으로도 문제 없이 구현됐다. 그러나 `this` 의 값을 변경할 수 밖에 없기 떄문에 메서드에서는 사용할 수 없다. `this` 에 관여하지 않는 별도의 부분 적용 함수가 있다면 범용성 측면에서 더욱 좋을 것이다.

**5-14** 부분 적용 함수 구현(1)

```javascript
var partial = function() {
  var originalPartialArgs = arguments;
  var func = originalPartialArgs[0];
  if (typeof func !== 'function') {
    throw new Error('첫 번째 인자가 함수가 아닙니다.');
  }
  return function() {
    var partialArgs = Array.prototype.slice.call(originalPartialArgs, 1);
    var restArgs = Array.prototype.slice.call(arguments);
    return func.apply(this, partialArgs.concat(restArgs));
  };
};

var add = function() {
  var result = 0;
  for (var i = 0; i < arguments.length; i++) {
    result += arguments[i];
  }
  return result;
};
var addPartial = partial(add, 1, 2, 3, 4, 5);
console.log(addPartial(6, 7, 8, 9, 10)); // 55

var dog = {
  name: '강아지',
  greet: partial(function(prefix, suffix) {
    return prefix + this.name + suffix;
  }, '왈왈, '),
};
dog.greet('입니다!'); // 왈왈, 강아지입니다.
```

위 예제에서 첫 번째 인자에는 원본 함수를, 두 번째 인자 이후부터는 미리 적용할 인자들을 전달하고, 반환할 함수(부분 적용 함수) 에서는 다시 나머지 인자들을 받아 이들을 모아(concat) 원본 함수를 호출(apply) 한다. 또한 실행 시점의 `this` 를 그대로 반영함으로써 `this` 에는 아무런 영향을 주지 않게 됐다.

보통의 경우 부분 적용 함수는 이 정도로 충분하다 원하는 만큼의 인자를 미리 넘겨놓고, 나중에 추가할 인자를 전달해서 실행하는 목적에 정확하게 부합하기 때문이다. 다만 부분 적용 함수에 넘길 인자를 반드시 앞에서부터 차례로 전달할 수밖에 없다는 점이 아쉽다. 인자들을 원하는 위치에 미리 넣어놓고 나중에는 빈자리에 인자를 채워넣어 실행할 수 있다면 더 좋을 것 같다.

**5-15** 부분 적용 함수 구현(1)

```javascript
Object.defineProperty(window, '_', {
  value: 'EMPTY_SPACE',
  writable: false,
  configurable: false,
  enumerable: false,
});

var partial2 = function() {
  var originalPartialArgs = arguments;
  var func = originalPartialArgs[0];
  if (typeof func !== 'function') {
    throw new Error('첫 번째 인자가 함수가 아닙니다.');
  }
  return function() {
    var partialArgs = Array.prototype.slice.call(originalPartialArgs, 1);
    var restArgs = Array.prototype.slice.call(arguments);
    for (var i = 0; i < partialArgs.length; i++) {
      if (partialArgs[i] === _) {
        partialArgs[i] = restArgs.shift();
      }
    }
    return func.apply(this, partialArgs.concat(restArgs));
  };
};

var add = function() {
  var result = 0;
  for (var i = 0; i < arguments.length; i++) {
    result += arguments[i];
  }
  return result;
};
var addPartial = partial2(add, 1, 2, _, 4, 5, _, _, 8, 9);
console.log(addPartial(3, 6, 7, 10)); // 55

var dog = {
  name: '강아지',
  greet: partial2(function(prefix, suffix) {
    return prefix + this.name + suffix;
  }, '왈왈, '),
};
dog.greet(' 배고파요!'); // 왈왈, 강아지 배고파요!
```

이번에는 '비워놓음'을 표시하기 위해 미리 전역객체에 _라는 프로퍼티를 준비하면서 삭제 변경 등의 접근에 대한 방어 차원에서 여러 가지 프로퍼티 속성을 설정했다. 예제 5-14와의 실질적인 변화는 17번째부터 21번째까지에 있다. 처음에 넘겨준 인자들 중 _로 비워놓은 공간마다 나중에 넘어온 인자들이 차례대로 끼워넣도록 구현했다. 이렇게 구현하는 것은 부분 적용 함수를 만들 때 미리부터 실행할 함수의 모든 인자 개수를 맞춰 빈 공간을 확보하지 않아도 된다. 실행할 함수 내부 로직에만 문제가 없다면 최종 실행 시 인자 개수가 많든 적든 잘 실행될 것이다.

예제 5-14, 5-15 의 부분 적용 함수들은 모두 클로저를 핵심 기법으로 사용했다. 미리 일부 인자를 넘겨두어 기억하게끔 하고 추후 필요한 시점에 기억했던 인자들까지 함께 실행하게 한다는 개념 자체가 클로저의 정의에 정확히 부합한다.

실무에서 부분 함수를 사용하기에 적합한 예로 디바운스(debounce)가 있다. 디바운스는 짧은 시간 동안 동일한 이벤트가 많이 발생할 경우 이를 전부 처리하지 않고 처음 또는 마지막에 발생한 이벤트에 대해 한 번만 처리하는 것으로, 프런트엔드 성능 최적화에 큰 도움을 주는 기능 중 하나다. `scroll`, `wheel`, `mousemove`, `resize` 등에 적용하기 좋다. Lodash 등의 라이브러리에서는 디바운스를 꽤 복잡하게 구현해 놓았지만, 최소한의 기능(마지막에 발생한 이벤트만 처리해도 괜찮고, 어느 정도의 시간 지연이 크게 문제되지 않은 경우)에 대한 구현은 생각보다 간단하다.

**5-16** 부분 적용 함수 - 디바운스

```javascript
var debounce = function(eventName, func, wait) {
  var timeoutId = null;
  return function(event) {
    var self = this;
    console.log(eventName, 'event 발생');
    clearTimeout(timeoutId);
    timeoutId = setTimeout(func.bind(self, event), wait);
  };
};

var moveHandler = function(e) {
  console.log('move event 처리');
};
var wheelHandler = function(e) {
  console.log('wheel event 처리');
};
document.body.addEventListener('mousemove', debounce('move', moveHandler, 500));
document.body.addEventListener(
  'mousewheel',
  debounce('wheel', wheelHandler, 700)
);
```

위에서 구현한 디바운스 함수는 출력 용도로 지정한 `eventName` 과 실행할 함수(func), 마지막으로 발생한 이벤트인지 여부를 판단하기 위한 대기시간(wait(ms))를 받는다. 내부에서는 `timeoutId` 변수를 생성하고, 클로저로 `EventListener` 에 의해 호출될 함수를 반환한다. 반환될 함수 내부에서는, 5번째 줄에서 `setTimeout` 을 사용하기 위해 `this` 를 별도의 변수에 담고, 6번째 줄에서는 무조건 대기큐를 초기화하게 했다. 마지막으로 7번째 줄에서 `setTimeout` 으로 `wait` 시간만큼 지연시킨 다음, 원래의 `func` 를 호출하는 형태다.

이제 최초 `event` 가 발생하면 7번째 줄에 의해 `timeout` 의 대기열에 ' `wait` 시간 뒤에 `func` 를 실행할 것'이라는 내용이 담긴다. 그런데 `wait` 시간이 경과하기 이전에 다시 동일한 `event` 가 발생하면 이번에는 6번째 줄에 의해 앞서 저장했던 대기열을 초기화 하고, 다시 7번째 줄에서 새로운 대기열을 등록한다. 결국 각 이벤트가 바로 이전 이벤트로부터 `wait` 시간 이내에 발생하는 한 마지막에 발생한 이벤트만이 초기화되지 않고 무사히 실행될 것이다. 참고로 예제 5-16의 디바운스 함수에서 클로저로 처리되는 변수에는 `eventName`, `func`, `wait`, `timeoutId` 가 있다.