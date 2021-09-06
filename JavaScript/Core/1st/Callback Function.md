# 콜백 함수

### 1. 콜백 함수란?

콜백 함수는 다른 코드의 인자로 넘겨주는 함수를 말한다. 콜백 함수를 넘겨받은 코드는 이 콜백 함수를 필요에 따라 적절한 시점에 실행할 것이다. 이해하기 어려울 수 있으니 일상생활을 예로 설명해보도록 하자.

A와 B는 다음 날 아침 8시에 만나기로 하고 잠을 잔다. 약속 장소에 가려면 늦어소 6시에는 일어나야 하는데 A는 불안한 마음에 수시로 깨어 시계를 확인하고 있다. 계속 잠을 설치다가 결국 5시 즈음 포기하고 일어나고 만다. 한편 B는 알람시계를 세팅한다. 시계가 정한 시각에 울리지 않을 염려는 없고 평소 알람소리에 쉽게 눈을 뜨곤 했던지라 안심하고 꿀잠을 잔다. 6시가 되자 시계의 알람소리가 울리고 B는 상쾌한 기분으로 일어나게 된다.

A는 수시로 시간을 구하는 함수를 직접 호출했다. 반면 B는 시계의 알람을 설정하는 함수를 호출했고, 해당 함수는 호출 당시에는 아무것도 하지 않았다가 B가 정해준 시각이 됐을 때 비로소 '알람을 울리는' 결과를 반환했다. 시간 정보를 제공하는 시계 입장에서 생각해보면 A의 경우 요청할 때마다 수동적으로 시간 정보를 제공하기만 한 반면, B의 경우에는 요청을 받은 뒤 자체적으로 무언가를 실행하다가 적절한 시점(6시)에 적극적으로 통보했다. A의 경우 시계 함수의 제어권은 A에게 있고, 시계는 그저 요청받은 내용을 이행할 뿐이다. 그런데 B는 시계 함수에게 요청을 하면서 알람을 울리는 명령에 대한 제어권을 시계한테 넘겨준 것이다. 이처럼 콜백 함수는 **제어권** 과 관련이 깊다.

callback은 '부르다', '호출하다'를 의미하는 call과 '뒤돌아오다', '되돌다'의 의민인 back이 합쳐진 말로 '되돌아 호출해달라'라는 명령이다. 어떤 함수 X를 호출하면서 '특정 조건일 때 함수 Y를 실행해서 나에게 알려달라'는 요청을 함께 보내는 것이다. 이 요청을 받은 함수 X의 입장에서는 해당 조건이 갖춰졌는지 여부를 스스로 판단하고 Y를 직접 호출한다.

이처럼 콜백 함수는 다른 코드(함수 또는 메서드)에게 인자로 넘겨줌으로써 그 제어권도 함께 위임한 함수다. 콜백 함수를 위임받은 코드는 자체적인 내부 로직에 의해 이 콜백 함수를 적절한 시점에 실행할 것이다.

### 2. 제어권

몇 가지 예제를 통해 구체적으로 살펴보자.

#### 2-1 호출 시점

**4-1** 콜백 함수 예제(1-1) setInterval

```javascript
var count = 0;
var timer = setInterval(function() {
  console.log(count);
  if (++count > 4) clearInterval(timer);
}, 300);
```

1번째 줄에서 `count` 변수를 선언하고 0을 할당했다. 2번째 줄에서는 `timer` 변수를 선언하고 여기에 `setInterval` 을 실행한 결과를 할당했다. `setInterval` 을 호출할 때 두 개의 매개변수를 전달했는데, 첫 번째는 익명 함수이고, 두 번째는 300이라는 숫자를 전달했다. 

`setInterval` 의 구조를 살펴보면 아래와 같다. => [MDN](https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/setInterval)

```javascript
var intervalID = scope.setInterval(func, [delay, arg1, arg2, ...]);
var intervalID = setInterval(func, [delay, arg1, arg2, ...]);
var intervalID = setInterval(function[, delay]);
var intervalID = setInterval(code, [delay]);
```

우선 `scope` 에는 `Window` 객체 또는 `Worker` 의 인스턴스가 들어올 수 있다. 두 객체 모두 `setInterval` 메서드를 제공하기 때문인데, 일반적인 브라우저 환경에서는 `Window` 를 생략해서 함수처럼 사용 가능할 것이다. 매개변수로는 `func`, `delay` 값을 반드시 전달해야 하고, 세 번째 매개변수부터는 선택적이다. `func` 는 함수이고, `delay`는 밀리초(ms) 단위의 숫자이며, 나머지(arg1, arg2 ...)는 `func` 함수를 실행할 때 매개변수로 전달할 인자다. `func` 에 넘겨준 함수는 매 `delay` 마다 실행되며, 그 결과 어떠한 값도 리턴하지 않는다. `setInterval` 를 실행하면 반복적으로 실행되는 내용 자체를 특정할 수 있는 고유한 **ID** 값이 반환된다. 이를 변수에 담는 이유는 반복 실행되는 중간에 종료(`clearInterval`) 할 수 있게 하기 위함이다.

**4-2** 콜백 함수 예제(1-2) setInterval

```javascript
var count = 0;
var cbFunc = function() {
  console.log(count);
  if (++count > 4) clearInterval(timer);
};
var timer = setInterval(cbFunc, 300);

// -- 실행 결과 --
// 0  (0.3초)
// 1  (0.6초)
// 2  (0.9초)
// 3  (1.2초)
// 4  (1.5초)
```

`timer` 변수에는 `setInterval` 의 **ID** 값이 담긴다. `setInterval` 에 전달한 첫 번째 인자인 `cbFunc` 함수(이 함수가 곧 콜백 함수)는 0.3초마다 자동으로 실행될 것이다. 콜백 함수 내부에서는 `count` 값을 출력하고, `count` 를 1만큼 증가시킨 다음, 그 값이 4보다 크면 반복 실행을 종료하라고 한다.

|           code            |  호출 주체  |   제어권    |
| :-----------------------: | :---------: | :---------: |
|         cbFunc();         |   사용자    |   사용자    |
| setInterval(cbFunc, 300); | setInterval | setInterval |

이 코드를 실행하면 콘솔창에는 0.3초에 한 번씩 숫자가 0부터 1씩 증가하며 출력되다가 4가 출력된 이후 종료된다. `setInterval` 이라고 하는 '다른 코드'에 첫번째 인자로서 `cbFunc` 함수를 넘겨주자 제어권을 넘겨받은 `setInterval`이 스스로의 판단에 따라 적절한 시점(0.3초마다) 이 익명 함수를 실행했다. 이처럼 콜백 함수의 제어권을 넘겨받은 코드는 콜백 함수 호출 시점에 대한 제어권을 가진다.

#### 2-2 인자

**4-3** 콜백 함수 예제(2-1) Array.prototype.map() - [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map)

```javascript
var newArr = [10, 20, 30].map(function(currentValue, index) {
  console.log(currentValue, index);
  return currentValue + 5;
});
console.log(newArr);

// -- 실행 결과 --
// 10 0
// 20 1
// 30 2
// [15, 25, 35]
```

1번째 줄에서 `newArr` 변수를 선언하고 우항의 결과를 할당했다. 그리고 5번째 줄에서 그 결과를 확인하고자 한다. 1번째 줄의 우항은 배열 [10, 20, 30]에 `map` 메서드를 호출하고 있다. 이때 첫 번째 매개변수로 익명함수를 전달한다. `map` 메서드는 첫 번째 인자로 `callback` 함수를 받고, 생략 가능한 두 번째 인자로 콜백 함수 내부에서 `this` 로 인식할 대상을 특정할 수 있다. `thisArg` 를 생략할 경우 일반적인 함수와 마찬가지로 전역객체가 바인딩된다. `map` 메서드는 메서드의 대상이 되는 배열의 모든 요소들을 처음부터 끝까지 하나씩 꺼내어 콜백 함수를 반복 호출하고, 콜백 함수의 실행 결과들을 모아 새로운 배열을 만든다. 콜백 함수의 첫 번째 인자에는 배열의 요소 중 현재값이, 두 번째 인자에는 현재값의 인덱스가, 세 번째 인자에는 `map` 메서드의 대상이 되는 배열 자체가 담긴다.

이를 바탕으로 예제를 살펴보면, 배열 [10, 20, 30]의 각 요소를 처음부터 하나씩 꺼내어 콜백 함수를 실행한다. 우선 첫 번째 인덱스에 대한 콜백함수는 `currentValue` 에 10이, `index`에 0이 담긴 채 실행되고, 각 값을 출력한 다음, 15(10 + 5)를 반환할 것이다. 두 번째 인덱스에 대한 콜백 함수는 `currentValue` 에 20이, `index` 에 1이 담긴 채 실행되고, 25를 반환할 것이다. 같은 방식으로 나머지 요소들에 대한 콜백 함수의 실행을 마치면 [15, 25, 35] 라는 새로운 배열이 만들어져서 변수 `newArr` 에 담기고, 이 값이 5번째 줄에서 출력될 것이다.

만약 콜백 함수의 인자들의 순서를 임의대로 바꾸게 되면 어떻게 될까?

**4-4** 콜백 함수 예제(2-1) Array.prototype.map() - 인자의 순서를 임의로 바꾸어 사용한 경우

```javascript
var newArr2 = [10, 20, 30].map(function(index, currentValue) {
  console.log(index, currentValue);
  return currentValue + 5;
});
console.log(newArr2);

// -- 실행 결과 --
// 10 0
// 20 1
// 30 2
// [5, 6, 7]
```

일반적으로 생각하기에 'index', 'currentValue' 등 단어로 접근하기 때문에 순서를 바꾸더라도 각 단어의 의미가 바뀌지 않으니까 문제 없을 것이라고 생각하기 쉽지만, 사실 저 단어들은 사용자가 명명한 것일 뿐이다. 컴퓨터는 그저 첫 번째, 두 번재의 **순서**에 의해서만 각각을 구분하고 인식할 것이다. 그렇기 때문에 우리가 첫 번째 인자의 이름을 'potato'로 명명하든 'tomato'로 하든지에 관계없이 그냥 순회 중인 배열 중 현재 요소의 값을 배정하는 것이다. 따라서 위의 예제를 실행하면 5번째 줄에서 [15, 25, 35]가 아닌 [5, 6, 7]이라는 전혀 다른 결과가 나오게 된다. `currentValue` 라고 명명한 인자의 위치가 두번째라서 컴퓨터가 여기에 인덱스 값을 부여했기 때문이다.

원하는 시각에 알람이 울리는 결과를 얻기 위해서는 시계가 정한 규칙, 즉 '알람용 침이 원하는 시각을 가리키도록 정하고 알람 스위치를 ON으로 설정해야 한다' 라는 규칙을 따라야만 한다. 마찬가지로 `map` 메서드를 호출해서 원하는 배열을 얻으려면 `map` 메서드에 정의된 규칙에 따라 함수를 작성해야 한다. `map` 메서드의 정의된 규칙에는 콜백 함수의 인자로 넘어올 값들 및 그 순서도 포함돼 있다. **콜백 함수를 호출하는 주체가 사용자가 아닌 `map` 메서드이므로 `map` 메서드가 콜백 함수를 호출할 때 인자에 어떤 값들을 어떤 순서로 넘길 것인지가 전적으로 `map` 메서드에게 달린 것이다.** 이처럼 콜백 함수의 제어권을 넘겨 받은 코드는 콜백 함수를 호출할 때 인자에 어떤 값들을 어떤 순서로 넘길 것인지에 대한 제어권을 가진다.

#### 2-3 this

앞서 "콜백 함수도 함수이기 때문에 기본적으로는 `this` 가 전역객체를 참조하지만, 제어권을 넘겨받을 코드에서 콜백 함수에 별도로 `this` 가 될 대상을 지정한 경우에는 그 대상을 참조하게 된다"고 말한 적이 있다. 별도의 `this` 를 지정하는 방식 및 제어권에 대한 이해를 높이기 위해 `map` 메서드를 직접 구현해보자. 예외 처리에 대한 내용은 모두 배제하고 동작 원리를 이해하는 것을 목표로 핵심 내용만 작성했다.

**4-5** 콜백 함수 예제(2-3) Array.prototype.map - 구현

```javascript
Array.prototype.map = function(callback, thisArg) {
  var mappedArr = [];
  for (var i = 0; i < this.length; i++) {
    var mappedValue = callback.call(thisArg || window, this[i], i, this);
    mappedArr[i] = mappedValue;
  }
  return mappedArr;
};
```

메서드 구현의 핵심은 `apply/call` 메서드에 있다. `this` 에는 `thisArg` 값이 있을 경우에는 그 값을, 없을 경우에는 전역객체를 지정하고, 첫 번째 인자에는 메서드의 `this` 가 배열을 가리킬 것이므로 배열의 i번째 요소 값을, 두 번째 인자에는 i 값을, 세 번째 인자에는 배열 자체를 지정해 호출해 준다. 그 결과가 변수 `mappedValue` 에 담겨 `mappedArr` 의 i번째 인자에 할당된다.

이제 `this` 에 다른 값이 담기는 이유를 정확히 알 수 있겠다. 바로 제어권을 넘겨받을 코드에서 `call/apply` 메서드의 첫 번째 인자에 콜백 함수 내부에서의 `this` 가 될 대상을 명시적으로 바인딩하기 때문이다.

**4-6** 콜백 함수 내부에서의 `this`

```javascript
setTimeout(function() {
  console.log(this);
}, 300); // (1) Window { ... }

[1, 2, 3, 4, 5].forEach(function(x) {
  console.log(this); // (2) Window { ... }
});

document.body.innerHTML += '<button id="a">클릭</button>';
document.body.querySelector('#a').addEventListener(
  'click',
  function(e) {
    console.log(this, e); // (3) <button id="a">클릭</button>
  } // MouseEvent { isTrusted: true, ... }
);
```

예제 4-6은 예제 3-11과 동일한 코드다. 각각 콜백 함수 내에서의 `this` 를 살펴보면, 우선 (1)의 `setTimeout` 은 내부에서 콜백 함수를 호출할 때 `call` 메서드의 첫 번째 인자에 전역객체를 넘기기 때문에 콜백 함수 내부에서의 `this` 가 전역객체를 가리킨다. (2)의 `forEach` 는 '별도의 인자로 `this` 를 받는 경우'에 해당하지만 별도의 인자로 `this` 를 넘겨주지 않았기 때문에 전역객체를 가리키게 된다. (3) `addEventListener` 는 내부에서 콜백 함수를 호출할 때 `call` 메서드의 첫 번째 인자의 `addEventListener` 메서드의 `this` 를 그대로 넘기도록 정의돼 있기 때문에 콜백 함수 내부에서의 `this` 가  `addEventListener` 를 호출한 주체인 HTML 엘리먼트를 가리키게 된다.

### 3. 콜백 함수는 함수다.

콜백 함수는 함수라는 말이 당연하게 느껴질 수 있으나 이 말의 의미에 대해 곰곰이 생각해볼 필요가 있다. 콜백 함수로 어떤 객체의 메서드를 전달하더라도 그 메서드는 메서드가 아닌 함수로서 호출이 된다.

**4-7** 메서드를 콜백 함수로 전달한 경우

```javascript
var obj = {
  vals: [1, 2, 3],
  logValues: function(v, i) {
    console.log(this, v, i);
  },
};
obj.logValues(1, 2); // { vals: [1, 2, 3], logValues: f } 1 2
[4, 5, 6].forEach(obj.logValues); // Window { ... } 4 0
// Window { ... } 5 1
// Window { ... } 6 2
```

`obj` 객체의 `logValues` 는 메서드로 정의된다. 7번째 줄에서는 이 메서드의 이름 앞에 점이 있으니 메서드로서 호출한 것이다. 따라서 `this` 는 `obj` 를 가리키고 인자로 넘어온 1,2가 출력된다.

한편 8번째 줄에서는 이 메서드를 `forEach` 함수의 콜백 함수로서 전달했다. `obj` 를 `this` 로 하는 메서드를 그대로 전달한 것이 아니라, `obj.logValues` 가 가리키는 함수만 전달한 것이다. 이 함수는 메서드로서 호출할 때가 아닌 한 `obj` 와의 직접적인 연관이 없어진다. `forEach` 에 의해 콜백이 함수로서 호출되고, 별도로 `this` 를 지정하는 인자를 지정하지 않았으므로 함수 내부에서의 `this` 는 전역 객체를 바라보게 된다.

그러니까 어떤 함수의 인자에 객체의 메서드를 전달하더라도 이는 결국 메서드가 아닌 함수일 뿐이다.

### 4. 콜백 함수 내부의 `this` 에 다른 값 바인딩하기

위에서 객체의 메서드를 콜백 함수로 전달하면 해당 객체를 `this` 로 바라볼 수 없게 된다는 것을 말했다. 그렇다면 콜백 함수 내부에서 `this` 가 객체를 바라보게 하기 위해서는 어떻게 해야 할까? 별도의 인자로 `this` 를 받는 함수의 경우에는 여기에 원하는 값을 넘겨주면 되지만 그렇지 않은 경우에는 `this` 의 제어권도 넘겨주게 되므로 사용자가 임의로 값을 바꿀 수 없다. 그래서 전통적으로는 `this` 를 다른 변수에 담아 콜백 함수로 활용할 함수에서는 `this` 대시 그 변수를 사용하게 하고, 이를 클로저로 만드는 방식이 많이 쓰였다.

**4-8** 콜백 함수 내부의 `this` 에 다른 값을 바인딩하는 방법 (1) - 전통적인 방식

```javascript
var obj1 = {
  name: 'obj1',
  func: function() {
    var self = this;
    return function() {
      console.log(self.name);
    };
  },
};
var callback = obj1.func();
setTimeout(callback, 1000);
```

`obj1.func()` 메서드 내부에서 `self` 변수에 `this` 를 담고, 익명 함수를 선언과 동시에 반환했다. 이제 10번째 줄에서 `obj1.func()` 를 호출하면서 앞서 선언한 내부함수가 반환되어 `callback` 변수에 담기게 된다.11번째 줄에서 이 `callback` 을 `setTimeout` 함수에 인자로 전달하면 1초 뒤 `callback` 이 실행되면서 'obj1' 을 출력하게 될 것이다.

이렇게 하게 되면 메서드를 함수로서 호출할 경우에도 `this` 가 객체를 가리키게 만들 수 있지만 이 방식은 실제로 `this` 를 사용하지도 않을 뿐더러 번거롭다. 

**4-9**  콜백 함수 내부에서의 `this` 를 사용하지 않은 경우

```javascript
var obj1 = {
  name: 'obj1',
  func: function() {
    console.log(obj1.name);
  },
};
setTimeout(obj1.func, 1000);
```

위 예제는 예제 4-8에서 `this` 를 사용하지 않았을 때의 결과다. 훨씬 간결하고 직관적이지만 아쉬운 부분도 있다. 이제는 작성한 함수를 `this` 를 이용해 다양한 상황에 재활용할 수 없게 됐다. 예제 4-8에서 만들었던 함수를 다른 객체에 재활용하는 방법을 살펴보자.

**4-10** 예제 4-8의 func 함수 재활용

```javascript
var obj1 = {
  name: 'obj1',
  func: function() {
    console.log(obj1.name);
  },
};
var obj2 = {
  name: 'obj2',
  func: obj1.func,
};
var callback2 = obj2.func();
setTimeout(callback2, 1500);

var obj3 = { name: 'obj3' };
var callback3 = obj1.func.call(obj3);
setTimeout(callback3, 2000);
```

위 예제의 `callback2` 에는 (obj1의 func를 복사한)`obj2`의 `func`를 실행한 결과를 담아 이를 콜백으로 사용했다. `callback3` 의 경우 `obj1` 의 `func` 를 실행하면서 `this` 를 `obj3` 가 되도록 지정해 이를 콜백으로 사용하였다. 예제를 실행해보면 실행 시점으로부터 1.5초 후에는 'obj2'가, 실행시점으로부터 2초 후에는 'obj3'이 출력된다. 이처럼 예제 4-8의 방법은 번거롭긴 하지만 `this` 를 우회적으로나마 활용함으로써 다양한 상황에서 원하는 객체를 바라보는 콜백 함수를 만들 수 있는 방법이다.

반면 예제 4-9같은 경우는 처음부터 바라볼 객체를 명시적으로 `obj1` 로 지정했기 때문에 어떤 방법으로도 다른 객체를 바라보게끔 할 수가 없다. 이런 문제점 때문에 불편할뿐 아니라 메모리를 낭비하는 측면이 있음에도 예제 4-8과 같은 전통적인 방식이 널리 통용될 수 밖에 없었던 측면도 있다. 물론 다양한 객체에 재활용할 필요성이 없는 경우라면 예제 4-9와 같이 해도 아무런 문제가 없다. 상황에 따라 적절한 방식을 선택해서 쓰면 될 것이다.

그렇지만 이제는 전통적인 방식의 아쉬움을 보완하는 훌륭한 방법이 있다. 바로 ES5에서 추가된 `bind()` 메서드를 이용하는 것이다. 

```javascript
var obj1 = {
  name: 'obj1',
  func: function() {
    console.log(this.name);
  },
};
setTimeout(obj1.func.bind(obj1), 1000);

var obj2 = { name: 'obj2' };
setTimeout(obj1.func.bind(obj2), 1500);
```

### 5. 콜백 지옥과 비동기 제어

콜백 지옥(callback hell)은 콜백 함수를 익명 함수로 전달하는 과정이 반복되어 코드의 들여쓰기 수준이 감당하기 힘들 정도로 깊어지는 현상으로, 자바스크립트에서 흔히 발생하는 문제다. 주로 이벤트 처리나 서버 통신과 같이 비동기적인 작업을 수행하기 위해 이런 형태가 자주 등장하곤 하는데, 가독성이 떨어질 뿐더러 코드를 수정하기도 어렵다.

비동기(asynchronous)와 동기(synchronous)는 정반대의 말이다. 동기적인 코드는 현재 실행 중인 코드가 완료된 후에야 다음 코드를 실행하는 방식이고 비동기적인 코드는 현재 실행 중인 코드의 완료 여부와 상관없이 즉시 다음 코드로 넘어간다. CPU의 계산에 의해 **즉시** 처리가 가능한 대부분의 코드는 동기적인 코드다. 계산식이 복잡해서 CPU가 계산하는데 시간이 많이 필요한 경우라 하더라도 이는 동기적인 코드다. 반면 사용자의 요청에 의해 특정 시간이 경과되기 전까지 어떤 함수의 실행을 보류한다거나, 사용자의 직접적인 개입이 있을 때 비로소 어떤 함수를 실행하도록 대기한다거나, 웹브타우저 자체가 아닌 별도의 대상에 무언가를 요청하고 그에 대한 응답이 왔을 때, 비로소 어떤 함수를 실행하도록 대기하는 등, **별도의 요청, 실행 대기, 보류** 등과 관련된 코드는 비동기적인 코드라고 할 수 있다.

 **4-12** 콜백 지옥 예시(1-1)

```javascript
setTimeout(
  function(name) {
    var coffeeList = name;
    console.log(coffeeList);

    setTimeout(
      function(name) {
        coffeeList += ', ' + name;
        console.log(coffeeList);

        setTimeout(
          function(name) {
            coffeeList += ', ' + name;
            console.log(coffeeList);

            setTimeout(
              function(name) {
                coffeeList += ', ' + name;
                console.log(coffeeList);
              },
              500,
              '카페라떼'
            );
          },
          500,
          '카페모카'
        );
      },
      500,
      '아메리카노'
    );
  },
  500,
  '에스프레소'
);
```

위 예제는 0.5초마다 커피 목록을 출력하고 수집하는 코드다. 각 콜백은 커피 이름을 전달하고 목록에 이름을 추가한다. 목적 달성에는 지장이 없지만 들여쓰기 수준이 과도하게 깊어졌을뿐더러 값이 전달되는 순서가 '아래에서 위로' 향하고 있어 어색하게 느껴지기도 한다. 

가독성과 어색함의 문제를 해결할 수 있는 가장 간단한 방법은 익명의 콜백 함수를 모두 기명함수로 전환하는 것이다.

**4-13** 콜백 지옥 해결 - 기명함수로 변환	

```javascript
var coffeeList = '';

var addEspresso = function(name) {
  coffeeList = name;
  console.log(coffeeList);
  setTimeout(addAmericano, 500, '아메리카노');
};
var addAmericano = function(name) {
  coffeeList += ', ' + name;
  console.log(coffeeList);
  setTimeout(addMocha, 500, '카페모카');
};
var addMocha = function(name) {
  coffeeList += ', ' + name;
  console.log(coffeeList);
  setTimeout(addLatte, 500, '카페라떼');
};
var addLatte = function(name) {
  coffeeList += ', ' + name;
  console.log(coffeeList);
};

setTimeout(addEspresso, 500, '에스프레소');
```

이 방식은 코드의 가독성을 높일뿐 아니라 함수 선언과 함수 호출만 구분할 수 있다면 위에서부터 아래로 순서대로 읽어내려가는 데 어려움이 없다. 또한 변수를 최상단으로 끌어올림으로써 외부에 노출되게 됐지만 전체를 즉시 실행 함수 등으로 감싸면 간단히 해결될 문제다.

그렇지만 일회성 함수를 전부 변수에 할당하는 것이 코드명을 일일이 따라다녀야 하므로 헷갈릴 소지가 있기도 하고 불편하다고 느낄 수도 있다. 이러한 비동기적인 작업을 동기적으로 처리해주는 장치를 마련하고자한 노력의 결과로 ES6에서는 `Promise` , `Generator` 등이 도입됐고, ES2017에서는 `async/await` 가 도입됐다. 

**4-14** 비동기 작업의 동기적 표현(1) - Promise(1)

```javascript
new Promise(function(resolve) {
  setTimeout(function() {
    var name = '에스프레소';
    console.log(name);
    resolve(name);
  }, 500);
})
  .then(function(prevName) {
    return new Promise(function(resolve) {
      setTimeout(function() {
        var name = prevName + ', 아메리카노';
        console.log(name);
        resolve(name);
      }, 500);
    });
  })
  .then(function(prevName) {
    return new Promise(function(resolve) {
      setTimeout(function() {
        var name = prevName + ', 카페모카';
        console.log(name);
        resolve(name);
      }, 500);
    });
  })
  .then(function(prevName) {
    return new Promise(function(resolve) {
      setTimeout(function() {
        var name = prevName + ', 카페라떼';
        console.log(name);
        resolve(name);
      }, 500);
    });
  });
```

첫 번째로 ES6의 `Promise` 를 이용한 방식이다. `new` 연산자와 함께 호출한 `Promise` 의 인자로 넘겨주는 콜백 함수는 호출할 때 바로 실행되지만 그 내부의  `resolve` 또는  `reject` 함수를 호출하는 구문이 있을 경우 둘 중 하나가 실행되기 전까지는 다음( `then`) 또는 오류 구문( `catch`) 로 넘어가지 않는다. 따라서 비동기 작업이 완료될 때 비로소  `resolve` 또는  `reject` 를 호출하는 방법으로 비동기 작업의 동기적 표현이 가능하다.

**4-15** 비동기 작업의 동기적 표현(2) - Promise(2)

```javascript
var addCoffee = function(name) {
  return function(prevName) {
    return new Promise(function(resolve) {
      setTimeout(function() {
        var newName = prevName ? prevName + ', ' + name : name;
        console.log(newName);
        resolve(newName);
      }, 500);
    });
  };
};
addCoffee('에스프레소')()
  .then(addCoffee('아메리카노'))
  .then(addCoffee('카페모카'))
  .then(addCoffee('카페라떼'));
```

위 예제는 예제 4-14의 반복적인 내용을 함수화해서 더욱 짧게 표현한 것이다. 2번째 및 3번째 줄에서 클로저가 등장했는데, 클로저에 대해서는 추후에 자세히 알아보도록하자.

**4-16** 비동기 작업의 동기적 표현(3) - Generator

```javascript
var addCoffee = function(prevName, name) {
  setTimeout(function() {
    coffeeMaker.next(prevName ? prevName + ', ' + name : name);
  }, 500);
};
var coffeeGenerator = function*() {
  var espresso = yield addCoffee('', '에스프레소');
  console.log(espresso);
  var americano = yield addCoffee(espresso, '아메리카노');
  console.log(americano);
  var mocha = yield addCoffee(americano, '카페모카');
  console.log(mocha);
  var latte = yield addCoffee(mocha, '카페라떼');
  console.log(latte);
};
var coffeeMaker = coffeeGenerator();
coffeeMaker.next();
```

위 예제는 ES6의 `Generator` 를 이용해서 비동기 코드를 작성한 것이다. 6번째 줄에서 '*'이 붙은 함수가 바로 `Generator` 함수다. `Generator` 함수를 실행하면 `Iterator` 가 반환되는데, `Iterator` 는 `next` 라는 메서드를 가지고 있다. 이 `next` 메서드를 호출함ㄴ `Generator` 함수 내부에서 가장 먼저 등장하는 `yield` 에서 함수의 실행을 멈춘다. 이후 다시 `next` 메서드를 호출하면 앞서 멈췄던 부분부터 시작해서 그다음에 등장하는 `yield` 에서 함수의 실행을 멈춘다. 그러니까 비동기 작업이 완료되는 시점마다 `next` 메서드를 호출해준다면 `Generator` 함수 내부의 소스가 위에서부터 아래로 순차적을 ㅗ진행되는 것이다.

**4-17** 비동기 작업의 동기적 표현(4) - Async/await

```javascript
var addCoffee = function(name) {
  return new Promise(function(resolve) {
    setTimeout(function() {
      resolve(name);
    }, 500);
  });
};
var coffeeMaker = async function() {
  var coffeeList = '';
  var _addCoffee = async function(name) {
    coffeeList += (coffeeList ? ',' : '') + (await addCoffee(name));
  };
  await _addCoffee('에스프레소');
  console.log(coffeeList);
  await _addCoffee('아메리카노');
  console.log(coffeeList);
  await _addCoffee('카페모카');
  console.log(coffeeList);
  await _addCoffee('카페라떼');
  console.log(coffeeList);
};
coffeeMaker();
```

ES2017에서는 가독성이 뛰어나면서 작성법도 간단한 새로운 기능이 추가됐는데, 바로 `async/await` 기능이다. 비동기 작업을 수행하고자 하는 함수 앞에 `async` 를 표기하고, 함수 내부에서 실질적인 비동기 작업이 필요한 위치마다 `await` 를 표기하는 것만으로 뒤의 내용을 `Promise` 로 자동 전환하고, 해당 내용이 `resolve` 된 이후에야 다음으로 진행한다. 즉, `Promise` 의 `then` 과 흡사한 효과를 얻을 수 있다.

### 6. 정리

- 콜백 함수는 다른 코드로 인자를 넘겨줌으로써 그 제어권도 함께 위임한 함수다.

- 제어권을 넘겨받은 코드는 다음과 같은 제어권을 가진다.

  1) 콜백 함수를 호출하는 시점을 스스로 판단해서 실행한다.

  2) 콜백 함수를 호출할 때 인자로 넘겨줄 값들 및 그 순서가 정해져 있다. 이 순서를 따르지 않고 코드를 작성하면 엉뚱한 결과를 얻게 된다.

  3) 콜백 함수의 `this` 가 무엇을 바라보도록 할지가 정해져 있는 경우도 있다. 정하지 않은 경우에는 전역객체를 바라본다. 사용자 임의로 `this` 를 바꾸고 싶을 경우 `bind` 메서드를 활용하면 된다.

- 어떤 함수에 인자로 메서드를 전달하더라도 이는 결국 함수로서 실행된다.

- 비동기 제어를 위해 콜백 함수를 사용하다 보면 콜백 지옥에 빠지기 쉽다. 그렇기 때문에 `Promise`, `Generator`, `Async/await` 등 콜백 지옥에서 벗어날 수 있는 방법들을 이용하는게 편하다.
