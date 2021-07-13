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

