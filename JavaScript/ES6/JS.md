# Arrow Function

일반적으로 함수는 아래와 같은 형태를 지니고 있다.

```javascript
function sayHello(name) {
  return "Hello" + name;
}
```

위와 같은 형태의 함수는 return을 해주지 않으면 **undefined**가 발생하게 된다. 

하지만 Arrow Function은 return을 한다는 게 함축이 되어 있으므로 return을 명시하지 않고도 return이 가능하다.

```javascript
const sayHello = name => "Hello" + name; 
const milkboy = sayHello("milkboy"); 

console.log(milkboy); // Hello milkboy
```

위의 Arrow Function에서 {}를 사용하게 되면 undefined가 발생하게 된다.

```javascript
const sayHello = name => {"Hello" + name}; 
const milkboy = sayHello("milkboy"); 

console.log(milkboy); // undefined
```

왜냐하면 중괄호를 한다는 건 중괄호 안의 어딘가에서 return을 한다는 것을 의미하기 때문이다. 반대로 중괄호를 쓰지 않고 Arrow Function을 사용한다면 return을 한다는 것을 함축하고 있기 때문에 **undefined**가 출력되지 않는다.

또한 Function을 사용할 때 parameter가 있음에도 parameter가 들어오지 않았을 때를 대비하여 default 값을 설정해 줄 수도 있다.

```javascript
function sayHello(name="Stranger") {
  return "Hello" + name;
}

const milkboy = sayHello(); 
console.log(milkboy); // Hello Stranger;
```

```javascript
const sayHello = (name="Stranger") => "Hello" + name; 
const milkboy = sayHello(); 

console.log(milkboy); // Hello Stranger
```

Arrow Function은 이벤트를 추가하거나 Function을 Anonymous Function으로 만들 때 유용하게 사용할 수 있다. [Example](https://codesandbox.io/s/happy-sky-h0btf?file=/src/index.js) 

추가로 Arrow Function은 argument가 두 개 이상일 때 꼭 괄호를 해줘야 한다는 규칙이 있다. 

Arrow Function은 일반적인 함수의 형태보다 깔끔하고 직관적인 코드를 작성할 수 있다는 장점이 있다.

# Object Destructuring

Object Destructuring은 배열이나 객체의 속성을 해체하여 그 값을 개별 변수에 담을 수 있게 하는 JavaScript 표현식이다.

```javascript
const Human = {
  name: "JaeHyeok",
  sex: "Man",
  nationality: "Korea",
  married: false
}

const name = Human.name;
const nationality: Human.nationality;

console.log(`${name}was born in ${nationality}`); 
```

일반적으로 객체의 property에 접근하려면 위와 같이 Object.property와 같이 접근해야 한다. 하지만 이 방법은 효율적인 방식이 아니고 변수명이 겹치게 된다는 단점 또한 존재한다.

이와 같은 문제를 해결할 때 사용할 수 있는게 바로 Object Destructuring(객체 분해 할당)이다. 다시 말해,  Object를 Deconstruct하고 해당 Object에 기반해 새로운 Variable을 만드는 것을 말한다. 

```javascript
const Human = {
  name: "JaeHyeok",
  sex: "Man",
  nationality: "Korea",
  married: false
};

const { name, nationality } = Human;

console.log(`${name} was born in ${nationality}`);
```

Const 이후에 나오는 중괄호는 Object 안에 있는 property(여기서는 name, nationality)들을 가져오는 것을 의미한다. 그런 다음 어떤 Object(여기서는 Human)에서 가져오는지 알려줘야 한다.

여기서 중요한 것은 새로운 variable들은 Object에 기반하여 만들어진다는 것이다. 다시 말해, Human이라는 Object로 가서 name의 값을 name이라는 새로운 변수에 할당하는 것을 말한다. 

만약 Object 내의 존재하는 property와 같은 변수명을 사용하고 싶지 않다면 두 가지의 방법이 있다.

1. 중괄호를 사용하지 않는 방법

```javascript
const Human = {
  name: "JaeHyeok",
  sex: "Man",
  nationality: "Korea",
  married: false
};

const difName = Human.sex; 
const { name, nationality } = Human;

console.log(`${name} was born in ${nationality}. And ${name} is a ${sex}.`);
```

2. 중괄호 내에서 설정하는 방법

```javascript
const Human = {
  name: "JaeHyeok",
  sex: "Man",
  nationality: "Korea",
  married: false
};

const { name, nationality, sex:difName } = Human;

console.log(`${name} was born in ${nationality}. And ${name} is a ${sex}.`);
```

두 번째 방법은 Object로 가서 해당하는 property를 vatiable로 가져온 뒤 그 variable 값을 내가 설정한 variable(여기서는 difName)으로 할당한다는 뜻이다.

위와 같이 한 번만 탐색하는 것이 아니라 더욱 깊게 탐색할 수도 있는데 

```javascript
const Human = {
  name: "JaeHyeok",
  sex: "Man",
  nationality: "Korea",
  favFood: {
    breakfast: "Noodle",
    lunch: "Pizza",
    dinner: "Hamburger"
  }
};

const { name, nationality, favFood: {breakfast, lunch, dinner}} = Human;

console.log(name, nationality, breakfast, lunch, dinner); // output: JaeHyeok Korea Noodle Pizza Hamburger
```

Object안에 Object가 있다면 해당 Object의 property name을 variable로 받아와서 다시 한 번 중괄호를 통해 해당 Object 안으로 들어갈 수 있다. 

[Example](https://codesandbox.io/s/happy-sky-h0btf?file=/src/OD.js)

# Spread Operator

Spread Operator는 특정 객체 또는 배열의 값을 다른 객체, 배열로 복제하거나 옮길 때 사용하고 연산자의 모양은 `...` 이렇게 생겼다.

```javascript
const days = ["Mon", "Tue", "Wed"];
const otherDays = ["Thu", "Fri", "Sat"];

const allDays = days + otherDays;

console.log(allDays); // output: Mon,Tue,WedThu,Fri,Sat
```

위와 같이 배열끼리 더하게 되면 새로운 배열이 만들어지는 것이 아니라 배열 안의 요소를 가진 문자열(string)으로 나타나게 된다. 이렇게 되면 더이상 배열이 아니기 때문에 `array[0]`과 같이 배열 안의 요소에 접근을 할 수 없게 된다.

Spread Operator는 배열들을 Unpack할 때 유용하게 사용할 수 있다. 예를 들어, days 배열과 otherDays 배열이 필요로 한게 아니라 배열 안의 요소들만 필요로 하다면 Spread Operator는 아주 좋은 선택지가 될 것이다. 왜냐하면 내가 원하는 것은 배열을 없애고 배열 안에 들어 있는 요소들만 사용하기를 원하기 때문이다.

Spread Operator는 배열 안의 요소들을 가져와서 Unpack해 준다. 그렇기 때문에 배열 안의 요소들을 전달할 뿐 배열을 전달하지 않는다.

```jsx
const days = ["Mon", "Tue", "Wed"];
const otherDays = ["Thu", "Fri", "Sat"];

const allDays = [...days, ...otherDays];

console.log(allDays); // output: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
```

위와 같이 Spread Operator를 사용하게 되면 두 배열이 가진 요소들을 하나의 배열이 가지게 된다. 또한 Spread Operator는 객체에서도 동작한다.

```javascript
const ob = {
  first: "hi",
  second: "hello"
};

const ab = {
  third: "bye bye"
};

const two = { ...ob, ...ab };

console.log(two); // output: {first: "hi", second: "hello", third: "bye bye"}
```

이렇게 Object에서도 배열에서와 마찬가지로 객체 내의 요소들만 Unpack하여 사용할 수 있게 해 준다.

Spread Operator는 Function와 Argument에서도 동작한다. 

```javascript
const fn = (something, args) => console.log(...args);
```

위와 같이 사용하게 되면 누군가가 제공한 모든 argument에 대하여 `console.log` 를 할 수 있게 된다.

정리하면 Spread Operator는 두 개의 객체나 배열을 병합하거나, 복사본을 만들거나, 어떤 대상의 콘텐츠를 다른 대상으로 넣을 때 유용하게 쓸 수 있는 문법이다.