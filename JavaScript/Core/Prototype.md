# 프로토타입

자바스크립트는 프로토타입(prototype)기반 언어다. 클래스 기반 언어에서는 '상속'을 사용하지만 프로토타입 기반 언어에서는 어떤 객체를 원형(prototype)으로 삼고 이를 복제(참조)함으로써 상속과 비슷한 효과를 얻는다. 유명 프로그래밍 언어의 상당수가 클래스 기반인 것에 비교하면 프로토타입은 꽤나 독특한 개념이라고 할 수 있다.

클래스에 익숙한 많은 개발자들이 자바스크립트를 배척하는 이유로 프로토타입이 어렵고 복잡하다는 점을 들지만, 오히려 자바스크립트는 프로토타입 개념을 제대로 이해하는 것만으로도 이미 숙련자 레벨에 도달할 수 있는 시야를 확보하게 되는 셈이다.

### 1. 프로토타입의 개념 이해

#### 6-1-1 constructor, prototype, instance

먼저 그림부터 보고 시작하자. 이 그림은 7장 클래스까지 반복적으로 등장할 그림이다.

**그림 6-1** 프로토타입 도식(1)

<img src="./images/6-1.png" width=400/>

위 그림만 이해하면 프로토타입은 끝이다. 즉, 이 그림으로부터 전체 구조를 파악할 수 있고, 반대로 전체 구조로부터 이 그림을 도출해낼 수 있으면 된다. 위 그림은 사실 아래 코드의 내용을 추상화한 것이다.

```javascript
var instance = new Constructor();
```

위 그림의 윗변(실선)의 왼쪽 꼭지점에는 `Constructor(생성자 함수)` 를, 오른쪽 꼭짓점에는 `Constructor.prototype` 이라는 프로퍼티를 위치시켰다. 왼쪽 꼭짓점으로부터 아래를 향한 화살표 중간에 `new` 가 있고, 화살표의 종점에는 `instance` 가 있다. 오른쪽 꼭짓점으로부터 대각선 아래로 향하는 화살표의 종점에는 `instance.__prototype__` 이라는 프로퍼티를 위치시켰다. 위 코드와 그림을 따라서 흐름을 살펴보면

> - 어떤 생성자 함수(Constructor)를 new 연산자와 함께 호출하면
> - `Constructor` 에서 정의된 내용을 바탕으로 새로운 인스턴스(instance)가 생성된다.
> - 이떄 `instance` 에는 `__proto__` 라는 프로퍼티가 자동으로 부여되는데,
> - 이 프로퍼티는 `Constructor` 의 `prototype` 이라는 프로퍼티를 참조한다.

`prototype` 이라는 프로퍼티와 `__proto__` 라는 프로퍼티가 새로 등장했는데, 이 둘의 관계가 프로토타입 개념의 핵심이다. `prototype` 은 객체다. 이를 참조하는 `__proto__` 역시 당연히 객체다. `prototype` 객체 내부에는 인스턴스가 사용할 메서드를 저장한다. 그러면 인스턴스에서도 숨겨진 프로퍼티인 `__proto__` 를 통해 이 메서드들에 접근할 수 있게 된다.

> ❗️
>
> ES5.1 명세에는 `__proto__` 가 아니라 `[[prototype]]` 이라는 명칭으로 정의돼 있다. `__proto__` 라는 프로퍼티는 사실 부라우저들이 `[[prototype]]` 을 구현한 대상에 지나지 않았다. 명세에는 또 `instance.__proto__` 와 같은 방식으로 직접 접근하는 것은 허용하지 않고 오직 `Object.getPrototypeOf(instance) / Refelect.getPrototypeOf(instance)` 를 통해서만 접근할 수 있도록 정의했었다. 하지만 이런 명세에도 불구하고 대부분의 브라우저들이 `__proto__` 에 직접 접근하는 방식을 포기하지 않았고, 결국 ES6에서 이를 브라우저에서 동작하는 레거시 코드에 대한 호환성 유지 차원에서 정식으로 인정하기에 이르렀다. 다만 어디까지나 브라우저에서의 호환성을 고려한 지원일 뿐 권장되는 방식은 아니며, 브라우저가 아닌 다른 환경에서는 얼마든지 이 방식이 지원되지 않을 가능성이 있다.
>
>  가급적  `__proto__` 를 사용하는 대신 `Object.getPrototypeOf() / Object.create()` 등을 이용하는 것이 권장된다.

예를 들어, `Person` 이라는 생성자 함수의 `prototype`에 `getName` 이라는 메서드를 지정했다고 하자.

**6-1** Person.prototype

```javascript
var Person = function(name) {
  this._name = name;
};
Person.prototype.getName = function() {
  return this._name;
};
```

이제 `Person` 의 인스턴스는 `__proto__` 프로퍼티를 통해 `getName` 을 호출할 수 있다.

```javascript
var carina = new Person('Carina');
carina.__proto__.getName(); // undefined
```

왜냐하면 `instance` 의 `__proto__` 가 `Constructor` 의 `prototype` 을 참조하므로 결국 둘은 같은 객체를 바라보기 때문이다.

```javascript
Person.prototype === carina.__proto__ // true
```

메서드 호출의 결과로 `undefined` 가 나온 점에 주목해보자. 'Carina' 라는 값이 나오지 않은것보다는 '에러가 발생하지 않았다는 점'이 우선이다. **어떤 변수를 실행해 `undefined` 가 나온다는 것은 이 변수가 '호출할 수 있는 함수'에 해당한다는 것을 의미한다.** 만약 실행할 수 없는, 즉 함수가 아닌 다른 데이터 타입이었다면 `TypeError` 가 발생했을 것이다.그런데 값이 에러가 아닌 다른 값이 다왔으니까 `getName`이 실제로 실행됐음을 알 수 있고, 이로부터 `getName` 이 함수라는 것이 입증됐다.

다음으로 함수 내부에서 어떤 값을 반환하는지를 살펴볼 차례다. 위 함수에서는  `this.name` 값을 리턴하는 것으로 보여진다. 그렇다면 `this` 에 원래의 의도와는 다른 값이 할당된 것이 아닐까, 라는 의심을 할 수있다. 이런 의문을 가지로 로그를 출력해보거나 `debugger` 를 지정하는 등으로 의심되는 사항을 하나하나 추적하다 보면 원인을 파악할 수 있을 것이다. 하지만 앞서 상황별로 어떤 값이 `this` 에 할당되는지를 살펴본 바 있다. 이 지식을 바탕으로 디버깅 과정을 거치지 않고도 문제를 파악할 수 있다. 결론부터 말하자면, **문제는 바로 `this` 에 바인딩된 대상이 잘못 지정됐다는 것이다.**

어떤 함수를 '메서드로서' 호출할 때는 메서드명 바로 앞의 객체가 곧 `this` 가 된다고 언급했었다. 그러니까 `thomas.__proto__.getName()` 에서 `getName` 함수 내부에서의 `this` 는 `thomas` 가 아니라 `thomas.__proto__` 라는 객체가 되는 것이다. 이 객체 내부에는 `name` 프로퍼티가 없으므로 '찾고자 하는 식별자가 정의돼 있지 않을 때는 `Error` 대신 `undefined` 를 반환한다' 라는 자바스크립트 규약에 의해 `undefined` 가 반환된 것이다.

그럼 만약 `__proto__` 객체에 `name` 프로퍼티가 있다면 어떨까?

```javascript
var carina = new Person("Carina");
carina.__proto__._name = "Carina__proto__";
carina.__proto__.getName(); // Carina__proto__
```

<img src="./images/6-2.png" width=600 height=400 />

예상대로 "Carina\__proto__" 가 잘 출력되는 것을 확인할 수 있다. 그러니까 관건은 `this` 다. `this` 를 인스턴스로 할 수 있다면 좋을 것이다. 그 방법은 `__proto__` 없이 인스턴스에서 곧바로 메서드를 쓰는 것이다.

```javascript
var carina = new Person("Carina", 22);
carina.getName(); // Carina
var iu = new Person("Jieun", 29);
iu.getName(); // Jieun
```

`__proto__` 을 빼면 `this` 는 `instance` 가 되는 것은 맞지만, 이대로 메서드가 호출되고 심지어 원하는 값이 나오는 건 조금 이상하다고 느낄 수 있다. 이상하지만 의외로 정상인데 그 이유는 바로 `__proto__` 가 **생략 가능한** 프로퍼티이기 때문이다. 원래부터 생략 가능하도록 정의돼 있다. 그리고 이 정의를 바탕으로 자바스크립트 전체 구조가 구성됐다고 해도 과언이 아니다. 그러니까 '생략 가능한 프로퍼티' 라는 개념은 언어를 창시하고 전체 구조를 설계한 브랜든 아이크의 머리에서 나온 아이디러로, 이해의 영역이 아니므로 '그냥 그런가보다' 하는 수 밖에 없다. 이유야 어찌됐든 중요한 것은 **`__proto__` 은 생략이 가능하다** 는 점만 기억하면 된다.

```javascript
carina.__proto__.getName
-> carina.(__proto__).getName
-> carina.getName
```

`__proto__` 를 생략하지 않으면 `this` 는 `carina.__proto__` 를 가리키지만, 이를 생략하면 `carina` 를 가리킨다. `carina.__proto__` 에 있는 메서드인 `getName` 을 실행하지만 `this` 는 `carina` 를 바라보게 할 수 있게 된 것이다. 도식으로 보면 다음과 같다.

<img src="./images/6-3.png" height=600 />

다시 한번 프로토타입에 대해 정의하면 아래와 같이 정의할 수 있다.

**new 연산자로 `Constructor` 를 호출하면 `instance` 가 만들어 지는데, 이 `instance`의 생략 가능한 프로퍼티인 `__proto__` 는 `Constructor` 의 `prototype`을 참조한다.** 

프로토타입의 개념을 좀 더 상세히 설명하면 자바스크립트는 함수에 자동으로 객체인 `prototype` 프로퍼티를 생성해 놓는데, 해당 함수를 생성자 함수로서 사용할 경우, 즉 `new` 연산자와 함께 호출할 경우, 그로부터 생성된 인스턴스에는 숨겨진 프로퍼티인 `__proto__` 가 자동으로 생성되며, 이 프로퍼티는 생성자 함수의 `prototype` 프로퍼티를 참조한다.`__proto__` 프로퍼티는 생략 가능하도록 구현돼 있기 때문에 **생성자 함수의 `prototype`에 어떤 메서드나 프로퍼티가 있다면 인스턴스에서도 마친 자신의 것처럼 해당 메서드나 프로퍼티에 접근할 수 있게 된다.**

**6-2** prototype과 \__proto__

```javascript
var Constructor = function(name) {
  this.name = name;
};
Constructor.prototype.method1 = function() {};
Constructor.prototype.property1 = 'Constructor Prototype Property';

var instance = new Constructor('Instance');
console.dir(Constructor);
console.dir(instance);
```

<img src="./images/6-4.png" height=600 />

실행 결과를 보면 예제 6-2의 8번째 줄에서 `Constructor` 의 디렉터리 구조를 출력하라고 했다. 출력 결과의 첫 줄에는 함수라는 의미의 `f` 와 함수 이름인 `Constructor` , 인자 `name` 이 보인다. 그 내부에는 옅은 색의 `arguments, caller, length, name, prototype, [[Prototype]], [[Scopes]]` 등의 프로퍼티들이 보인다. `prototype` 을 열어보면 예제 6-2의 4,5번째 중에서 추가한 `method1`, `property1` 등의 값이 짙은 색으로 보이고 `Constructor` , `[[Prototype]]` 등이 옅은 색으로 보인다.

> ❗️
>
> 이런 색상의 차이는 `{ enumerable: false }` 속성이 부여된 프로퍼티인지 여부에 따른다. 짙은색은 enumerable, 즉 열거 가능한 프로퍼티임을 의미하고, 옅은색은 innumerable, 즉 열거할 수 없는 프로퍼티임을 의미한다. `for`, `in` 등으로 객체의 프로퍼티 전체에 접근하고자 할 때 접근 가능 여부를 색상으로 구분지어 표기하는 것이다.

9번째 줄에서는 `instance` 의 디렉터리 구조를 출력하는 문장이 있다. 그런데 출력 결과를 보면 `Constructor` 가 나오고 있는 것을 확인할 수 있다. 어떤 생성자 함수의 인스턴스는 해당 생성자 함수의 이름을 표기함으로써 해당 함수의 인스턴스임을 표기하고 있다. `Constructor` 를 열어보면 `name` 프로퍼티가 짙은 색으로 보이고, `[[Prototype]] == __proto__` 프로퍼티가 옅은 색으로 보인다. 다시 `[[Prototype]]` 을 열어보니 `method1`, `property1` , `constructor`, `__proto__` 등이 보이는 것으로 봐엇 `Constructor` 의 `prototype` 과 동일한 내용으로 구성돼 있음이 확인된다.

이번에는 대표적인 내장 생성자 함수인 `Array` 를 바탕으로 살펴보도록 하자.

```javascript
var arr = [1, 2];
console.dir(arr);
console.dir(Array);
```

<img src="./images/6-5.png" height=600 />

왼쪽은 `arr` 변수를 출력한 결과고, 오른쪽은 생성자 함수인 `Array` 를 출력한 결과다. 왼쪽부터 보면 첫 줄에는 Array(2)라고 표기되고 있다. `Array` 라는 생성자 함수를 원형으로 삼아 생성됐고, `length` 가 2임을 알 수 있다. 인덱스인 0, 1이 짙은 색상으로, `length` 와 `[[Prototype]] == __proto__` 가 옅은 색상으로 표기된다(책에서는 옅은 색상으로 표기되는데 직접 콘솔에서 확인할 때는 짙은 색상으로 확인된다.. 뭐지 ). `[[Prototype]]` 을 열어보니 옅은 색상의 다양한 배열 메서드들이 길게 펼쳐지는 것을 확인할 수 있다.

이제 오른쪽을 보게되면, 첫 줄에는 함수라는 의미의 `f` 가 표시돼 있고, 둘째 줄부터는 함수의 기본적인 프로퍼티들인 `arguments`, `caller`, `length`, `name` 등이 옅은 색으로 보인다.  또한 `Array` 함수의 정적 메서드인 `from`, `isArray`, `of` 등도 보인다. `prototype` 을 열어보니 왼쪽의 `[[Prototype]] == __proto__` 과 완전히 동일한 내용으로 구성돼 있다. 위 출력 결과를 바탕으로 위 그림의 도식을 더욱 구체화하면 다음과 같다.

<img src="./images/6-6.png" height=600 />

이제 생성자 함수와 `prototype` , 인스턴스 사이의 관계가 명확히 보이는 것 같다. `Array` 를 `new` 연산자와 함께 호출해서 인스턴스를 생성하든, 그냥 배열 리터럴을 생성하든, 어쨌든 `instance` 인 [1, 2]가 만들어진다. 이 인스턴스의 `__proto__` 은 `Array.prototype` 을 참조하는데, `__proto__` 가 생략 가능하도록 설계돼 있기 때문에 인스턴스가 `push`, `pop`, `forEach` 등의 메서드를 마친 자신의 것처럼 호출할 수 있다. 한편 `Array` 의 `prototype` 프로퍼티 내부에 있지 않은 `from`, `isArray`, `of` 등의 메서드들은 인스턴스가 직접 호출할 수 없는 것들이다. 이들은 `Array` 생성자 함수에서 직접 접근해야 실행이 가능하다.

```javascript
var arr = [1, 2];
arr.forEach(function(){}); 	// (0)
Array.isArray(arr);					// (0) true
arr.isArray();							// (x) TypeError: arr.isArray is not a function
```

#### 6-1-2 constructor 프로퍼티

생성자 함수의 프로퍼티인 `prototype` 객체 내부에는 `constructor` 라는 프로퍼티가 있다. 이는 물론 인스턴스의 `__proto__` 객체 내부에도 마찬가지다. 미 프로퍼티는 단어 그대로 원래의 생성자 함수(자기 자신)을 참조한다. 자신을 참조하는 프로퍼티를 굳이 뭐하러 가지고 있을까 싶지만, 이 역시 인스턴스와의 관계에 있어서 필요한 정보다. 인스턴스로부터 그 원형이 무엇인지를 알 수 있는 수단이기 때문이다.

**6-3** constructor 프로퍼티

```javascript
var arr = [1, 2];
Array.prototype.constructor === Array; // true
arr.__proto__.constructor === Array; // true
arr.constructor === Array; // true

var arr2 = new arr.constructor(3, 4);
console.log(arr2); // [3, 4]
```

인스턴스의 `__proto__` 가 생성자 함수의 `prototype` 를 참조하며 `__proto__` 가 생략 가능하기 때문에 인스턴스에서 직접 `constructor` 에 접근할 수 있는 수단이 생긴 것이다. 그러기에 6번째 줄과 같은 명령도 오류 없이 동작하게 된다.

한편 `constructor` 는 읽기 전용 속성이 부여된 예외적인 경우(기본형 리터럴 변수 - `number`, `boolean`, `string` )를 제외하고는 값을 바꿀 수 없다.

**6-4** constructor 변경

```javascript
var NewConstructor = function() {
  console.log('this is new constuctor!');
};
var dataTypes = [
  1, 							// Number & false
  'test', 				// String & false
  true, 					// Boolean & false
  {}, 						// NewConstructor & false
  [], 						// NewConstructor & false
  function() {}, 	// NewConstructor & false
  /test/, 				// NewConstructor & false
  new Number(), 	// NewConstructor & false
  new String(), 	// NewConstructor & false
  new Boolean(), 	// NewConstructor & false
  new Object(), 	// NewConstructor & false
  new Array(), 		// NewConstructor & false
  new Function(), // NewConstructor & false
  new RegExp(), 	// NewConstructor & false
  new Date(), 		// NewConstructor & false
  new Error(), 		// NewConstructor & false
];

dataTypes.forEach(function(d) {
  d.constructor = NewConstructor;
  console.log(d.constructor.name, '&', d instanceof NewConstructor);
});
```

모든 데이터가 `d instanceof NewConstructor` 명령에 대해 `false` 를 반환한다. 이로부터 `constructor` 를 변경하더라도 참조하는 대상이 변경될 뿐 이미 만들어진 인스턴스의 원형이 바뀐다거나 데이터 타입이 변하는 것은 아님을 알 수 있다. 어떤 인스턴스의 생성자 정보를 알아내기 위해 `constructor` 프로퍼티에 의존하는 게 항상 안전하지는 않은 것이다.

비록 어떤 인스턴스로부터 생성자 정보를 알아내느 유일한 수단인 `constructor` 가 항상 안전하지는 않지만 오히려 그렇기 떄문에 클래스 상속을 흉내 내는 등이 가능해진 측면도 있다. 이 내용은 추후에 '클래스' 에서 자세히 다뤄보도록 하자.

정리하는 차원에서 다른 예제도 살펴보도록 하자.

**6-5** 다양한 constructor 접근 방법

```javascript
var Person = function(name) {
  this.name = name;
};
var p1 = new Person('사람1'); 											// Person { name: "사람1" } true
var p1Proto = Object.getPrototypeOf(p1);
var p2 = new Person.prototype.constructor('사람2'); // Person { name: "사람2" } true
var p3 = new p1Proto.constructor('사람3'); 					// Person { name: "사람3" } true
var p4 = new p1.__proto__.constructor('사람4'); 		// Person { name: "사람4" } true
var p5 = new p1.constructor('사람5'); 							// Person { name: "사람5" } true

[p1, p2, p3, p4, p5].forEach(function(p) {
  console.log(p, p instanceof Person);
});
```

`p1` 부터 `p5` 까지 모두 `Person` 의 인스턴스다. 따라서 다음 두 공식이 성립한다.

첫째, 다음 각 줄은 모두 동일한 대상을 가리킨다.

```java
[Constructor]
[instance].__proto__.constructor
[instance].constructor
Object.getPrototypeOf([instance]).construcor
[Constructor].prototype.constructor
```

둘째, 다음 각 줄은 모두 동일한 객체(prototype) 에 접근할 수 있다.

```javascript
[Constructor].prototype
[instance].__proto__
[instance]
Object.getPrototypeOf([instance])
```

