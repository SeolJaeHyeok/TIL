## 26.1 함수의 구분

ES6 이전까지 자바스크립트의 함수는 별다른 구분 없이 다양한 목적으로 사용되었다. 자바스크립트의 함수는 일반적인 함수로서 호출할 수도 있고, `new` 연산자와 함께 호출하여 인스턴스를 생성할 수 있는 생성자 함수로서 호출할 수도 있으며, 객체에 바인딩되어 메서드로서 호출할 수도 있다. 이는 언뜻 보면 편리한 것 같지만 실수를 유발시킬 수 있으며 성능 면에서도 손해다.

```javascript
var foo = function () {
  return 1;
};

// 일반적인 함수로서 호출
foo(); // -> 1

// 생성자 함수로서 호출
new foo(); // -> foo {}

// 메서드로서 호출
var obj = { foo: foo };
obj.foo(); // -> 1
```

이처럼 ES6 이전의 함수는 사용 목적에 따라 명확히 구분되지 않는다. 즉, **ES6 이전의 모든 함수는 일반 함수로서 호출할 수 있는 것은 물론 생성자 함수로서 호출할 수 있다.** 다시 말해, ES6 이전의 모든 함수는 `callable` 이면서 `constructor` 다.

```javascript
var foo = function () {};

// ES6 이전의 모든 함수는 callable이면서 constructor다.
foo(); // -> undefined
new foo(); // -> foo {}
```

>❗️
>
>"내부 메서드 `[[Call]]` 과 `[[Construct]]` "에서 살펴보았듯이 호출할 수 있는 함수 객체를 `callable` 이라 하며, 인스턴스를 생성할 수 있는 함수 객체를 `constructor` , 인스턴스를 생성할 수 없는 함수 객체를 `non-constructor` 라고 한다.

주의할 것은 ES6 이전에 일반적으로 메서드라고 부르던 객체에 바인딩된 함수도 `callable` 이며 `constructor` 라는 것이다. 따라서 객체에 바인딩된 함수도 일반 함수로서 호출할 수 있는 것은 물론 생성자 함수로서 호출할 수도 있다.

```javascript
// 프로퍼티 f에 바인딩된 함수는 callable이며 constructor다.
var obj = {
  x: 10,
  f: function () { return this.x; }
};

// 프로퍼티 f에 바인딩된 함수를 메서드로서 호출
console.log(obj.f()); // 10

// 프로퍼티 f에 바인딩된 함수를 일반 함수로서 호출
var bar = obj.f;
console.log(bar()); // undefined

// 프로퍼티 f에 바인딩된 함수를 생성자 함수로서 호출
console.log(new obj.f()); // f {}
```

위 예제아 같이 객체에 바인딩된 함수를 생성자 함수로 호출하는 경우는 흔치 않지만 문법상 가능하다는 것은 문제가 있다. 그리고 이는 성능 면에서도 문제가된다. 객체에 바인딩된 함수가 `constructor` 라는 것은 객체에 바인딩된 함수가 `prototype` 프로퍼티를 가지며, 프로토타입 객체도 생성한다는 것을 의미하기 때문이다.

함수에 전달되어 보조 함수의 역할을 수행하는 콜백 함수도 마찬가지다. 콜백 함수도 `constructor` 이기 때문에 불필요한 프로토타입 객체를 생성한다.

```javascript
// 콜백 함수를 사용하는 고차 함수 map. 콜백 함수도 constructor이며 프로토타입을 생성한다.
[1, 2, 3].map(function (item) {
  return item * 2;
}); // -> [ 2, 4, 6 ]
```

이처럼 ES6 이전의 모든 함수는 사용 목적에 따라 명확한 구분 없이 호출 방식에 특별한 제약이 없고 생성자 함수로 호출되지 않아도 프로토타입 객체를 생성한다. 이는 혼란스러우며 실수를 유발할 가능성이 있고 성능 상에도 문제가 있다.

이러한 문제를 해결하기 위해 ES6에서는 함수를 사용 목적에 따라 세 가지 종류로 명확히 구분했다.

| ES6 함수의 구분 | constructor | prototype | super | arguments |
| --------------- | ----------- | --------- | ----- | --------- |
| 일반 함수       | O           | O         | X     | O         |
| 메서드          | X           | X         | O     | O         |
| 화살표 함수     | X           | X         | X     | X         |

일반 함수는 함수 선언문이나 함수 표현식으로 정의한 함수를 말하며, ES6 이전의 함수와 차이가 없다. 하지만 ES6의 메서드와 화살표 함수는 ES6 이전의 함수와 명확한 차이가 있다.

일반 함수는 `constructor` 이지만 ES6의 메서드와 화살표 함수는 `non-constructor` 다.

## 26.2 메서드

ES6 사양 이전에는 메서드에 대한 명확한 정의가 없었다. 일반적으로 메서드는 객체에 바인딩된 함수를 일컫는 의미로 사용되었다. ES6 사양에서는 메서드에 대한 정의가 명확히 규정되어 있다. **ES6 사양에서 메서드는 메서드 축약 표현으로 정의된 함수만을 말한다.**

```javascript
const obj = {
  x: 1,
  // foo는 메서드이다.
  foo() { return this.x; },
  // bar에 바인딩된 함수는 메서드가 아닌 일반 함수이다.
  bar: function() { return this.x; }
};

console.log(obj.foo()); // 1
console.log(obj.bar()); // 1
```

ES6 사양에서 정의한 메서드는 인스턴스를 생성할 수 없는 `non-constructor`다. 따라서 ES6 메서드는 생성자 함수로 호출할 수 없다.

```javascript
new obj.foo(); // -> TypeError: obj.foo is not a constructor
new obj.bar(); // -> bar {}
```

ES6 메서드는 인스턴스를 생성할 수 없으므로 `prototype` 프로퍼티가 없고 프로토타입도 생성하지 않는다.

```javascript
// obj.foo는 constructor가 아닌 ES6 메서드이므로 prototype 프로퍼티가 없다.
obj.foo.hasOwnProperty('prototype'); // -> false

// obj.bar는 constructor인 일반 함수이므로 prototype 프로퍼티가 있다.
obj.bar.hasOwnProperty('prototype'); // -> true
```

참고로 표준 빌트인 객체가 제공하는 프로토타입 메서드와 정적 메서드는 모두 `non-constructor`다.

```javascript
String.prototype.toUpperCase.prototype; // -> undefined
String.fromCharCode.prototype           // -> undefined

Number.prototype.toFixed.prototype; // -> undefined
Number.isFinite.prototype;          // -> undefined

Array.prototype.map.prototype; // -> undefined
Array.from.prototype;          // -> undefined
```

**ES6 메서드는 자신을 바인딩한 객체를 가리키는 내부 슬롯 `[[HomeObject]]` 를 갖는다.** `super` 참조는 내부 슬롯 `[[HomeObject]]` 를 사용하여 수퍼클래스의 메서드를 참조하므로 내부 슬롯 `[[HomeObject]]` 를 갖는 ES6 메서드는 `super` 키워드를 사용할 수 있다.

```javascript
const base = {
  name: 'Lee',
  sayHi() {
    return `Hi! ${this.name}`;
  }
};

const derived = {
  __proto__: base,
  // sayHi는 ES6 메서드다. ES6 메서드는 [[HomeObject]]를 갖는다.
  // sayHi의 [[HomeObject]]는 sayHi가 바인딩된 객체인 derived를 가리키고
  // super는 sayHi의 [[HomeObject]]의 프로토타입인 base를 가리킨다.
  sayHi() {
    return `${super.sayHi()}. how are you doing?`;
  }
};

console.log(derived.sayHi()); // Hi! Lee. how are you doing?
```

ES6 메서드가 아닌 함수는 `super` 키워드를 사용할 수 없다. ES6 메서드가 아닌 함수는 내부 슬롯 `[[HomeObject]]` 를 갖지 않기 때문이다.

```javascript
const derived = {
  __proto__: base,
  // sayHi는 ES6 메서드가 아니다.
  // 따라서 sayHi는 [[HomeObject]]를 갖지 않으므로 super 키워드를 사용할 수 없다.
  sayHi: function () {
    // SyntaxError: 'super' keyword unexpected here
    return `${super.sayHi()}. how are you doing?`;
  }
};
```

이처럼 ES6 메서드는 본연의 기능(`super`)을 추가하고 의미적으로 맞지 않는 기능(`constructor`)는 제거했다. 따라서 메서드를 정의할 때 프로퍼티 값으로 익명 함수 표현식을 할당하는 ES6 이전의 방식은 사용하지 않는 것이 좋다.

## 26.3 화살표 함수

화살표 함수는 `function` 키워드 대신 화살표(=>, fat arrow)를 사용하여 기존의 함수 정의 방식보다 간략하게 함수를 정의할 수 있다. 화살표 함수는 표현만 간략한 것이 아니라 내부 동작도 기존의 함수보다 간략하다. 특시 화살표 함ㅅ는 콜백 함수 내부에서 `this` 가 전역 객체를 가리키는 문제를 해결하기 위한 대안으로 유용하다.

#### 26.3.1 화살표 함수 정의

**1. 함수 정의**

화살표 함수는 함수 선언문으로 정의할 수 없고 함수 표현식으로 정의해야 한다. 호출 방식은 기존의 방식과 동일하다.

```javascript
const multiply = (x, y) => x * y;
multiply(5, 6);
```

**2. 매개변수 선언**

매개 변수가 여러 개일 경우 소괄호 () 안에 매개변수를 선언한다.

```javascript
const arrow = (x, y) => { ... };
```

매개변수가 한 개일 경우 소괄호를 생략할 수 있다.

```javascript
const arrow = x => { ... };
```

매개변수가 없는 경우 소괄호를 생략할 수 없다.

```javascript
const arrow = () => { ... };
```

**3. 함수 몸체 정의**

함수 몸체가 하나의 문으로 구성된다면 함수 몸체를 감싸는 중괄호 {}를 생략할 수 있다. 이때 함수 몸체 내부의 문이 값으로 평가될 수 있는 표현식이라면 암묵적으로 반환된다.

```javascript
// concise body
const power = x => x ** 2;
power(2); // -> 4

// 위 표현은 다음과 동일하다.
// block body
const power = x => { return x ** 2; };
```

함수 몸체를 감싸는 중괄 {} 를 생략하는 경우 함수 몸체 내부의 문이 표현식이 아닌 문이라면 에러가 발생한다. 표현식이 아닌 문은 반환할 수 없기 때문이다.

```javascript
const arrow = () => const x = 1; // SyntaxError: Unexpected token 'const'

// 위 표현은 다음과 같이 해석된다.
const arrow = () => { return const x = 1; };
```

따라서 함수 몸체가 하나의 문으로 구성된다 해도 함수 몸체의 문이 표현식이 아닌 문이라면 중괄호를 생략할 수 없다.

```javascript
const arrow = () => { const x = 1; };
```

객체 리터럴을 반환하는 경우 객체 리터럴을 소괄호 ()로 감싸 주어야 한다.

```javascript
const create = (id, content) => ({ id, content });
create(1, 'JavaScript'); // -> {id: 1, content: "JavaScript"}

// 위 표현은 다음과 동일하다.
const create = (id, content) => { return { id, content }; };
```

객체 리터럴을 소괄호로 감싸지 않으면 객체 리터럴의 중괄호를 함수 몸체를 감싸는 중괄호로 잘못 해석한다.

```javascript
// { id, content }를 함수 몸체 내의 쉼표 연산자문으로 해석한다.
const create = (id, content) => { id, content };
create(1, 'JavaScript'); // -> undefined
```

함수 몸체가 여러 개의 문으로 구성된다면 함수 몸체를 감싸는 중괄호를 생략할 수 없다. 이때 반환값이 있다면 명시적으로 반환해야 한다.

```javascript
const sum = (a, b) => {
  const result = a + b;
  return result;
};
```

화살표 함수도 즉시 실행 함수로 사용할 수 있다.

```javascript
const person = (name => ({
  sayHi() { return `Hi? My name is ${name}.`; }
}))('Lee');

console.log(person.sayHi()); // Hi? My name is Lee.
```

화살표 함수도 일급 객체이므로 `Array.prototype.map`, `Array.prototype.filter`, `Array.prototype.reduce` 같은 고차 함수에 인수로 전달할 수 있다. 이 경우 일반적인 함수 표현식보다 표현이 간결하고 가독성이 좋다.

```javascript
// ES5
[1, 2, 3].map(function (v) {
  return v * 2;
});

// ES6
[1, 2, 3].map(v => v * 2); // -> [ 2, 4, 6 ]
```

이처럼 화살표 함수는 콜백 함수로서 정의할 때 유용하다. 화살표 함수는 표현만 간략한 것이 아니다. 화살표 함수는 일반 함수의 기능을 간략화했으며 `this` 도 편리하게 설계되었다. 일반 함수와 화살표 함수의 차이를 알아보자.

#### 26.3.2 화살표 함수와 일반 함수의 차이

화살표 함수와 일반 함수의 차이는 다음과 같다.

1. 화살표 함수는 인스턴스를 생성할 수 없는 `non-constructor` 다.

   ```javascript
   const Foo = () => {};
   // 화살표 함수는 생성자 함수로서 호출할 수 없다.
   new Foo(); // TypeError: Foo is not a constructor
   ```

   화살표 함수는 인스턴스를 생성할 수 없으므로 `prototype` 프로퍼티가 없고 프로토타입도 생성하지 않는다.

   ```javascript
   const Foo = () => {};
   // 화살표 함수는 prototype 프로퍼티가 없다.
   Foo.hasOwnProperty('prototype'); // -> false
   ```

2. 중복된 매개변수 이름을 선언할 수 없다.

   ```javascript
   function normal(a, a) { return a + a; }
   console.log(normal(1, 2)); // 4
   ```

   단, strict mode에서 중복된 매개변수 이름을 선언하면 에러가 발생한다.

   ```javascript
   'use strict';
   
   function normal(a, a) { return a + a; }
   // SyntaxError: Duplicate parameter name not allowed in this context
   ```

   화살표 함수에서도 중복된 매개변수 이름을 사용하면 에러가 발생한다.

   ```javascript
   const arrow = (a, a) => a + a;
   // SyntaxError: Duplicate parameter name not allowed in this context
   ```

3. 화살표 함수는 함수 자체의 `this`, `arguments`, `super`, `new.target` 바인딩을 갖지 않는다.

   따라서 화살표 함수 내부에서 `this`, `arguments`, `new.target`, `super` 를 참조하면 스코프 체인을 통해 상위 스코프의 `this`, `arguments`, `new.target` , `super`을 참조한다.

   만약 화살표 함수와 화살표 함수가 중첩되어 있다면 상위 화살표 함수에도 `this`, `arguments,` `new,target`, `super`  바인딩이 없으므로 스코프 체인 상에서 가장 가까운 상위 함수 중에서 화살표 함수가 아닌 함수의 `this`, `arguments,` `new.target` , `super` 를 참조한다.

#### 26.3.3 this

화살표 함수가 일반 함수와 구분되는 가장 큰 특징은 바로 `this` 다. 그리고 화살표 함수는 다른 함수의 인수로 전달되어 콜백 함수로 사용되는 경우가 많다.

화살표 함수의 `this` 는 일반 함수의 `this` 와 다르게 동작한다. 이는 "콜백 함수 내부의 `this` 문제", 즉 콜백 함수 내부의 `this` 가 외부 함수의 `this` 와 다르기 때문에 발생하는 문제를 해결하기 위해 의도적으로 설계된 것이다.

`this` 바인딩은 함수의 호출 방식, 즉 함수가 어떻게 호출되었는지에 따라 동적으로 결정된다. 다시 말해, 함수를 정의할 때 `this` 에 바인딩할 객체가 정적으로 결정되는 것이 아니고, 함수를 호출할 때 함수가 어떻게 호출되었는지에 따라 `this` 에 바인딩할 객체가 동적으로 결정된다.

이때 주의할 것은 일반 함수로서 호출되는 콜백 함수의 경우다. 고차 함수의 인수로 전달되어 고차 함수 내부에서 호출되는 콜백 함수도 중첩 함수라고 할 수 있다. 주어진 배열의 각 요소에 접두어를 추가하는 다음 예제를 살펴보자.

```javascript
class Prefixer {
  constructor(prefix) {
    this.prefix = prefix;
  }

  add(arr) {
    // add 메서드는 인수로 전달된 배열 arr을 순회하며 배열의 모든 요소에 prefix를 추가한다.
    // ①
    return arr.map(function (item) {
      return this.prefix + item; // ②
      // -> TypeError: Cannot read property 'prefix' of undefined
    });
  }
}

const prefixer = new Prefixer('-webkit-');
console.log(prefixer.add(['transition', 'user-select']));
```

위 예제를 실행했을 때 기대하는 결과는 `['-webkit-transition', '-webkit-user-select']` 다. 하지만 실행을 해보면 타입 에러가 발생하는 것을 확인할 수 있다. 왜 그런지 살펴보도록 하자.

프로토타입 메서드 내부의 (1)에서 `this` 는 메서드를 호출한 객체(위 예제의 경우 `prefixer` 객체)를 가리킨다. 그런데 `Array.prototype.map` 의 인수로 전달한 콜백 함수의 내부인 (2)에서 `this` 는 `undefined` 를 가리킨다. 이는 `Array.prototype.map` 메서드가 콜백 함수를 일반 함수로서 호출하기 때문이다.

앞서 살펴보았듯이 일반 함수로서 호출되는 모든 함수 내부의 `this` 는 전역 객체가 바인딩된다. 그런데 클래스 내부의 모든 코드에는 strict mode가 암묵적으로 적용된다. 따라서 `Array.prototype.map` 메서드의 콜백 함수에도 strict mode가 적용된다. strict mode에서 일반 함수로서 호출된 모든 함수 내부의 `this` 에는 전역 객체가 아니라 `undefined` 가 바인딩되므로 일반 함수로서 호출되는 `Array.prototype.map` 메서드의 콜백 함수 내부의 `this` 에는 `undefined` 가 바인딩된다.

이때 발생하는 문제가 바로 "콜백 함수 내부의 `this` 문제"다. 즉, 콜백 함수의 `this`(2)와 외부 함수의 `this`(1) 가 서로 다른 값을 가리키고 있기 때문에 타입 에러가 발생한 것이다. 이와 같은  "콜백 함수 내부의 `this` 문제"를 해결하기 위해 ES6 이전에는 다음과 같은 방법을 사용했다.

1. `add` 메서드를 호출한 `prefixer` 개게를 가리키는 `this` 를 일단 회피시킨 후에 콜백 함수 내부에서 사용한다.

   ```javascript
   ...
   add(arr) {
     // this를 일단 회피시킨다.
     const that = this;
     return arr.map(function (item) {
       // this 대신 that을 참조한다.
       return that.prefix + ' ' + item;
     });
   }
   ...
   ```

2. `Array.prototype.map` 의 두 번째 인수로 `add` 메서드를 호출한 `prefixer` 객체를 가리키는 `this` 를 전달한다. ES5에서 도입된 `Array.prototype.map` 은 "콜백 함수 내부의 `this` 문제"를 해결하기 위해 두 번째 인수로 콜백 함수 내부에서 `this` 로 사용할 객체를 전달할 수 있다.

   ```javascript
   ...
   add(arr) {
     return arr.map(function (item) {
       return this.prefix + ' ' + item;
     }, this); // this에 바인딩된 값이 콜백 함수 내부의 this에 바인딩된다.
   }
   ...
   ```

3. `Function.prototype.bind` 메서드를 사용하여 `add` 메서드를 호출한 `prefixer` 객체를 가리키는 `this` 를 바인딩한다.

   ```javascript
   ...
   add(arr) {
     return arr.map(function (item) {
       return this.prefix + ' ' + item;
     }.bind(this)); // this에 바인딩된 값이 콜백 함수 내부의 this에 바인딩된다.
   }
   ...
   ```

ES6에서는 화살표 함수를 사용하여 "콜백 함수 내부의 `this` 문제"를 해결할 수 있다.

```javascript
class Prefixer {
  constructor(prefix) {
    this.prefix = prefix;
  }

  add(arr) {
    return arr.map(item => this.prefix + item);
  }
}

const prefixer = new Prefixer('-webkit-');
console.log(prefixer.add(['transition', 'user-select']));
// ['-webkit-transition', '-webkit-user-select']

```

**화살표 함수는 함수 자체의 `this` 바인딩을 갖지 않는다. 따라서 화살표 함수 내부에서 `this` 를 참조하면 상위 스코프의 `this` 를 그대로 참조한다. 이를 `lexical this` 라고 한다.** 이는 마치 렉시컬 스코프와 같이 화살표 함수의 `this` 가 함수가 정의된 위치에 의해 결정된다는 것을 의미한다.

화살표 함수를 제외한 모든 함수에는 `this` 바인딩이 반드시 존재한다. 따라서 ES6에서 화살표 함수가 도입되기 이전에는 일반적인 식별자처럼 스코프 체인을 통해 `this` 를 탐색할 필요가 없었다. 하지만 화살표 함수는 함수 자체의 `this` 바인딩이 존재하지 않는다. 따라서 화살표 함수 내부에서 `this` 를 참조하면 일반적인 식별자처럼 스코프 체인을 통해 상위 스코프의 `this` 를 탐색한다. 화살표 함수는 `Function.prototype.bind` 를 사용하여 표현하면 다음과 같다.

```javascript
// 화살표 함수는 상위 스코프의 this를 참조한다.
() => this.x;

// 익명 함수에 상위 스코프의 this를 주입한다. 위 화살표 함수와 동일하게 동작한다.
(function () { return this.x; }).bind(this);
```

만약 화살표 함수와 화살표 함수가 중첩되어 있다면 상위 화살표 함수에도 `this` 바인딩이 없으므로 스코프 체인 상에서 가장 가까운 상위 함수 중에서 화살표 함수가 아닌 함수의 `this` 를 참조한다.

```javascript
// 중첩 함수 foo의 상위 스코프는 즉시 실행 함수다.
// 따라서 화살표 함수 foo의 this는 상위 스코프인 즉시 실행 함수의 this를 가리킨다.
(function () {
  const foo = () => console.log(this);
  foo();
}).call({ a: 1 }); // { a: 1 }

// bar 함수는 화살표 함수를 반환한다.
// bar 함수가 반환한 화살표 함수의 상위 스코프는 화살표 함수 bar다.
// 하지만 화살표 함수는 함수 자체의 this 바인딩을 갖지 않으므로 bar 함수가 반환한
// 화살표 함수 내부에서 참조하는 this는 화살표 함수가 아닌 즉시 실행 함수의 this를 가리킨다.
(function () {
  const bar = () => () => console.log(this);
  bar()();
}).call({ a: 1 }); // { a: 1 }
```

만약 화살표 함수가 전역 함수라면 화살표 함수의 `this` 는 전역 객체를 가리킨다. 전역 함수의 상위 스코프는 전역이고 전역에서 `this` 는 전역 객체를 가리키기 때문이다.

```javascript
// 전역 함수 foo의 상위 스코프는 전역이므로 화살표 함수 foo의 this는 전역 객체를 가리킨다.
const foo = () => console.log(this);
foo(); // window
```

프로퍼티에 할당한 화살표 함수도 스코프 체인 상에서 가장 가까운 상위 함수 중에서 화살표 함수가 아닌 함수의 `this` 를 참조한다.

```javascript
// increase 프로퍼티에 할당한 화살표 함수의 상위 스코프는 전역이다.
// 따라서 increase 프로퍼티에 할당한 화살표 함수의 this는 전역 객체를 가리킨다.
const counter = {
  num: 1,
  increase: () => ++this.num
};

console.log(counter.increase()); // NaN
```

화살표 함수는 함수 자체의 `this` 바인딩을 갖지 않기 때문에 `Function.prototype.call` ,` Function.prototype.apply`, `Function.prototype.bind` 메서드를 사용해도 화살표 함수 내부의 `this` 를 교체할 수 없다.

```javascript
window.x = 1;

const normal = function () { return this.x; };
const arrow = () => this.x;

console.log(normal.call({ x: 10 })); // 10
console.log(arrow.call({ x: 10 }));  // 1
```

화살표 함수가 `Function.prototype.call` ,` Function.prototype.apply`, `Function.prototype.bind` 메서드를 호출할 수 없다는 의미는 아니다. 화살표 함수는 함수 자체의 `this` 바인딩을 갖지 않기 때문에 `this` 를 교체할 수 없고 언제나 상위 스코프의 `this` 바인딩을 참조한다.

```javascript
const add = (a, b) => a + b;

console.log(add.call(null, 1, 2));    // 3
console.log(add.apply(null, [1, 2])); // 3
console.log(add.bind(null, 1, 2)());  // 3
```

메서드를 화살표 함수로 정의하는 것은 피해야 한다. 화살표 함수로 메서드를 정의해 보자. 여기서 말하는 메서드는 ES6 메서드가 아닌 일반적인 의미의 메서드다.

```javascript
// Bad
const person = {
  name: 'Lee',
  sayHi: () => console.log(`Hi ${this.name}`)
};

// sayHi 프로퍼티에 할당된 화살표 함수 내부의 this는 상위 스코프인 전역의 this가 가리키는
// 전역 객체를 가리키므로 이 예제를 브라우저에서 실행하면 this.name은 빈 문자열을 갖는
// window.name과 같다. 전역 객체 window에는 빌트인 프로퍼티 name이 존재한다.
person.sayHi(); // Hi
```

위 예제의 경우 `sayHi` 프로퍼티에 할당한 화살표 함수 내부의 `this` 에는 메서드를 호출한 객체인 `person` 을 가리키지 않고 상위 스코프인 전역의 `this` 가 가리키는 전역 객체를 가리킨다. 따라서 화살표 함수로 메서드를 정의하는 것은 바람직하지 않다. 메서드를 정의할 때는 ES6 메서드 축약 표현으로 정의한 ES6 메서드를 사용하는 것이 좋다.

```javascript
// Good
const person = {
  name: 'Lee',
  sayHi() {
    console.log(`Hi ${this.name}`);
  }
};

person.sayHi(); // Hi Lee
```

프로토타입 객체의 프로퍼티에 화살표 함수를 할당하는 경우도 동일한 문제가 발생한다.

```javascript
// Bad
function Person(name) {
  this.name = name;
}

Person.prototype.sayHi = () => console.log(`Hi ${this.name}`);

const person = new Person('Lee');
// 이 예제를 브라우저에서 실행하면 this.name은 빈 문자열을 갖는 window.name과 같다.
person.sayHi(); // Hi
```

프로퍼티를 동적 추가할 떄는 ES6 메서드 정의를 사용할 수 없으므로 일반 함수를 할당한다.

```javascript
// Good
function Person(name) {
  this.name = name;
}

Person.prototype.sayHi = function () { console.log(`Hi ${this.name}`); };

const person = new Person('Lee');
person.sayHi(); // Hi Lee
```

일반 함수가 아닌 ES6 메서드를 동적 추가하고 싶다면 다음과 같이 객체 리터럴을 바인딩하고 프로토타입의 `constructor` 프로퍼티와 생성자 함수 간의 연결을 재설정한다.

```javascript
function Person(name) {
  this.name = name;
}

Person.prototype = {
  // constructor 프로퍼티와 생성자 함수 간의 연결을 재설정
  constructor: Person,
  sayHi() { console.log(`Hi ${this.name}`); }
};

const person = new Person('Lee');
person.sayHi(); // Hi Lee
```

클래스 필드 정의 제안을 사용하여 클래스 필드에 화살표 함수를 할당할 수도 있다.

```javascript
// Bad
class Person {
  // 클래스 필드 정의 제안
  name = 'Lee';
  sayHi = () => console.log(`Hi ${this.name}`);
}

const person = new Person();
person.sayHi(); // Hi Lee
```

이때 `sayHi` 클래스 필드에 할당한 화살표 함수 내부에서 `this` 를 참조하면 상위 스코프의 `this` 바인딩을 참조한다. 그렇다면 클래스 필드에 할당한 화살표 함수의 상위 스코프는 무엇일까? `sayHi` 클래스 필드는 인스턴스 프로퍼티이므로 다음과 같은 의미다.

```javascript
class Person {
  constructor() {
    this.name = 'Lee';
    // 클래스가 생성한 인스턴스(this)의 sayHi 프로퍼티에 화살표 함수를 할당한다.
    // sayHi 프로퍼티는 인스턴스 프로퍼티이다.
    this.sayHi = () => console.log(`Hi ${this.name}`);
  }
}
```

`sayHi` 클래스 필드에 할당한 화살표 함수의 상위 스코프는 사실 클래스 외부다. 하지만 `this` 는 클래스 외부의 `this` 를 참조하지 않고 클래스가 생성할 인스턴스를 참조한다. 따라서 `sayHi` 클래스 필드에 할당한 화살표 함수 내부에서 참조한 `this` 는 `constructor` 내부의 `this` 바인딩과 같다. `constructor` 내부의 `this` 바인딩은 클래스가 생성한 인스턴스를 가리키므로 `sayHi` 클래스 필드에 할당한 화살표 함수 내부의 `this` 또한 클래스가 생성한 인스턴스를 가리킨다. 하지만 클래스 필드에 할당한 화살표 함수는 프로토타입 메서드가 아니라 인스턴스 메서드가 된다. 따라서 메서드를 정의할 때는 ES6 메서드 축약 표현으로 정의한 ES6 메서드를 사용하는 것이 좋다.

```javascript
// Good
class Person {
  // 클래스 필드 정의
  name = 'Lee';

  sayHi() { console.log(`Hi ${this.name}`); }
}
const person = new Person();
person.sayHi(); // Hi Lee
```

#### 26.3.4 super

화살표 함수는 함수 자체의 `super` 바인딩을 갖지 않는다. 따라서 화살표 함수 내부에서 `super` 를 참조하면 `this` 와 마찬가지로 상위 스코프의 `super` 를 참조한다.

```javascript
class Base {
  constructor(name) {
    this.name = name;
  }

  sayHi() {
    return `Hi! ${this.name}`;
  }
}

class Derived extends Base {
  // 화살표 함수의 super는 상위 스코프인 constructor의 super를 가리킨다.
  sayHi = () => `${super.sayHi()} how are you doing?`;
}

const derived = new Derived('Lee');
console.log(derived.sayHi()); // Hi! Lee how are you doing?
```

`super` 는 내부 슬롯 `[[HomeObject]]` 를 갖는 ES6 메서드 내에서만 사용할 수 있는 키워드다. `sayHi` 클래스 필드에 할당한 화살표 함수는 ES6 메서드는 아니지만 함수 자체의 `super` 바인딩을 갖지 않으므로 `super` 를 참조해도 에러가 발생하지 않고 `this` 와 마찬가지로 클래스 필드에 할당한 화살표 함수 내부에서 `super` 를 참조하면 `constructor` 내부의 `super` 바인딩을 참조한다. 위 예제의 경우 `Derived` 클래스의 `constructor` 는 생략되었지만 암묵적으로 `constructor` 가 생성된다.

#### 26.3.5 arguments

화살표 함수는 함수 자체의 `arguments` 바인딩을 갖지 않는다. 따라서 화살표 함수 내부에서 `arguments` 를 참조하면 `this` 와 마찬가지로 상위 스코프의 `arguments` 를 참조한다.

```javascript
(function () {
  // 화살표 함수 foo의 arguments는 상위 스코프인 즉시 실행 함수의 arguments를 가리킨다.
  const foo = () => console.log(arguments); // [Arguments] { '0': 1, '1': 2 }
  foo(3, 4);
}(1, 2));

// 화살표 함수 foo의 arguments는 상위 스코프인 전역의 arguments를 가리킨다.
// 하지만 전역에는 arguments 객체가 존재하지 않는다. arguments 객체는 함수 내부에서만 유효하다.
const foo = () => console.log(arguments);
foo(1, 2); // ReferenceError: arguments is not defined
```

`arguments` 객체는 함수를 정의할 때 매개변수의 개수를 확정할 수 없는 가변 인자 함수를 구현할 떄 유용하다. 하지만 화살표 함수에서는 `arguments` 객체를 사용할 수 없다. 상위 스코프의 `arguments` 객체를 참조할 수는 있지만 화살표 함수 자신에게 전달된 인수 목록을 확인할 수 없고 상위 함수에게 전달된 인수 목록을 참조하므로 그다지 도움이 되지 않는다.

따라서 화살표 함수로 가변 인자 함수를 구현해야 할 때는 반드시 Rest 파라미터를 사용해야 한다.