# Immutability

데이터를 불변하게 다루면 데이터들간의 간섭으로 인한 버그의 가능성을 획기적으로 낮출 수 있다. 또 데이터가 변경 되었는지 여부를 매우 쉽게 체크할 수 있다. 그 외에 Hot module reloading, time travel과 같은 고급 기법을 구현하는데 기초가 되기도 한다.

#### Test

```jsx
var n1 = 1;
var n2 = 1;
console.log(n1 === n2);
=> true입니다. 당연합니다.

var o1 = {name:'kim'}
var o2 = {name:'kim'}
console.log(o1 === o2);
=> false 입니다. 조금 애매하죠. JavaScript는 값이 바뀌지 않는 원시 데이터 타입과 값이 바뀔 수 있는 객체를 다르게 취급합니다.

var o1 = {name:'kim'}
var o2 = o1;
o2.name = 'lee';
console.log(o1.name);
=> lee 입니다. o1은 영문도 모르고 자신이 가르키고 있는 name의 값이 바뀌어 버렸습니다.

var o1 = {name:'kim'}
var o2 = Object.assign({}, o1); // 빈 객체에 o1을 복사합니다.
o2.name = 'lee';
console.log(o1.name);
=> kim입니다. o2를 변경해도 o1이 영향을 받지 않습니다. o2에 대해서 o1은 불변한 상태를 유지할 수 있게 됩니다.

var o1 = {score:[1,2]}
var o2 = Object.assign({}, o1);
o2.score.push(3);
console.log(o1.score)
=> [1,2,3] 입니다. 영문도 모르고 o1이 또 바뀌었습니다. score는 객체의 일종인 배열이기 때문입니다.

var o1 = {score:[1,2]}
var o2 = Object.assign({}, o1);
o2.score = o2.score.concat(); // 배열을 복사합니다.
o2.score.push(3);
console.log(o1.score)
=> [1,2] 입니다.

다른 방법도 있습니다. 몽땅 다 복사를 하는 것입니다.
var o1 = {score:[1,2]}
var o2 = JSON.parse(JSON.stringify(o1));
o2.score.push(3);
console.log(o1.score)
=> [1,2] 입니다.

원본이 바뀌지 않게 조심하는 것도 좋지만, 원본이 아예 안바뀌게 하는 것도 가능합니다.
var o1 = {name:'kim'}
Object.freeze(o1);
o1.name = 'lee';
console.log(o1.name);
=> 'kim' 입니다.

하지만 객체는 이게 안됩니다.
var o1 = {score:[1,2]}
Object.freeze(o1);
o1.score.push(3);
console.log(o1.score);
// [1,2,3] 입니다.

방어적으로 냉동을 해야 합니다.
var o1 = {score:[1,2]}
Object.freeze(o1);
Object.freeze(o1.score);
o1.score.push(3);
console.log(o1.score);
// 변경이 안됩니다. 심지어 항의성 에러를 발생시켜버립니다.
```

----

변수를 어떻게 불변하게 할 것인가?  const 키워드를 사용

**JS의 데이터 타입**

- Primitive(원시 데이터 타입 == 최소한의 데이터 타입) : Number, String, Boolean, Null, Undefined, Symbol 은 변경 불가능한 값(immutable value)다. 값이 같으면 같은 메모리에 위치한다.

- Object : Object, Array, Function 은 변경이 가능한 값이다. 즉, 객체는 새로운 객체를 만들 필요 없이 직접 변경이 가능하다. 값이 같아도 다른 메모리에 위치하고 있다.

-----

### 불변 데이터 패턴

의도하지 않은 객체의 변경이 발생하는 원인의 대다수는 “레퍼런스를 참조한 다른 객체에서 객체를 변경”하기 때문이다. 이 문제의 해결 방법은 비용은 조금 들지만 객체를 불변객체로 만들어 프로퍼티의 변경을 방지하며 객체의 변경이 필요한 경우에는 참조가 아닌 객체의 방어적 복사(defensive copy)를 통해 새로운 객체를 생성한 후 변경한다.

이를 정리하면 아래와 같다.

- 객체의 방어적 복사(defensive copy)

  Object.assign

- 불변객체화를 통한 객체 변경 방지

  Object.freeze

----

#### 1. Object.assign

Object.assign은 타킷 객체로 소스 객체의 프로퍼티를 복사한다. 이때 소스 객체의 프로퍼티와 동일한 프로퍼티를 가진 타켓 객체의 프로퍼티들은 소스 객체의 프로퍼티로 덮어쓰기된다. 리턴값으로 타킷 객체를 반환한다. ES6에서 추가된 메소드이며 Internet Explorer는 지원하지 않는다.

```javascript
// Syntax
Object.assign(target, ...sources)
```

```javascript
// Copy
const obj = { a: 1 };
const copy = Object.assign({}, obj);
console.log(copy); // { a: 1 }
console.log(obj == copy); // false

// Merge
const o1 = { a: 1 };
const o2 = { b: 2 };
const o3 = { c: 3 };

const merge1 = Object.assign(o1, o2, o3);

console.log(merge1); // { a: 1, b: 2, c: 3 }
console.log(o1);     // { a: 1, b: 2, c: 3 }, 타겟 객체가 변경된다!

// Merge
const o4 = { a: 1 };
const o5 = { b: 2 };
const o6 = { c: 3 };

const merge2 = Object.assign({}, o4, o5, o6);

console.log(merge2); // { a: 1, b: 2, c: 3 }
console.log(o4);     // { a: 1 }
```

Object.assign을 사용하여 기존 객체를 변경하지 않고 객체를 복사하여 사용할 수 있다. Object.assign은 완전한 deep copy를 지원하지 않는다. 객체 내부의 객체(Nested Object)는 Shallow copy된다.

```javascript
const user1 = {
  name: 'Lee',
  address: {
    city: 'Seoul'
  }
};

// 새로운 빈 객체에 user1을 copy한다.
const user2 = Object.assign({}, user1);
// user1과 user2는 참조값이 다르다.
console.log(user1 === user2); // false

user2.name = 'Kim';
console.log(user1.name); // Lee
console.log(user2.name); // Kim

// 객체 내부의 객체(Nested Object)는 Shallow copy된다.
console.log(user1.address === user2.address); // true

user1.address.city = 'Busan';
console.log(user1.address.city); // Busan
console.log(user2.address.city); // Busan
```

Shallow copy(얕은 복사)란 새로운 객체에 원본 객체의 프로퍼티의 값을 정확히 복사한다.

하지만 만약 프로퍼티의 값이 객체 형태라면, 객체의 주소를 복사한다. 

즉, 복사된 객체는 원본 객체와 동일한 프로퍼티와 값들을 새롭게 가지지만, 주소가 복사된 프로퍼티는 새로운 형태가 아닌 같은 것을 공유하게 된다.

얕은 복사의 가장 큰 이슈는 서로 공유하는 객체가 존재한다는 것이다.

이와 같은 이슈들을 정리하면 다음과 같다.

1. Property Descriptors 가 복사되지 않는다.
2. 프로토타입 체인 또는 열거가능하지 않은 프로퍼티는 복사되지 않는다.
3. 기본형 타입은 변경해도 서로 영향을 끼치지 않지만, 참조형 타입인 객체는 공유하고 있기 때문에 영향을 끼치게된다.

출처: https://mygumi.tistory.com/322

-----

#### 2. Object.freeze

```javascript
const user1 = {
  name: 'Lee',
  address: {
    city: 'Seoul'
  }
};

// Object.assign은 완전한 deep copy를 지원하지 않는다.
const user2 = Object.assign({}, user1, {name: 'Kim'});

console.log(user1.name); // Lee
console.log(user2.name); // Kim

Object.freeze(user1);

user1.name = 'Kim'; // 무시된다!

console.log(user1); // { name: 'Lee', address: { city: 'Seoul' } }

console.log(Object.isFrozen(user1)); // true
```

하지만 객체 내부의 객체(Nested Object)는 변경가능하다.

```javascript
const user = {
  name: 'Lee',
  address: {
    city: 'Seoul'
  }
};

Object.freeze(user);

user.address.city = 'Busan'; // 변경된다!
console.log(user); // { name: 'Lee', address: { city: 'Busan' } }
```

객체 내부의 객체까지 변경 불가능하게 만들려면 Deep Freeze를 해야 한다.

```jsx
function deepFreeze(obj) {
  const props = Object.getOwnPropertyNames(obj);

  props.forEach((name) => {
    const prop = obj[name];
    if(typeof prop === 'object' && prop !== null) {
      deepFreeze(prop);
    }
  });
  return Object.freeze(obj);
}

const user = {
  name: 'Lee',
  address: {
    city: 'Seoul'
  }
};

deepFreeze(user);

user.name = 'Kim';           // 무시된다
user.address.city = 'Busan'; // 무시된다

console.log(user); // { name: 'Lee', address: { city: 'Seoul' } }
```

----

#### 3. Immutable.js

Object.assign과 Object.freeze을 사용하여 불변 객체를 만드는 방법은 번거러울 뿐더러 성능상 이슈가 있어서 큰 객체에는 사용하지 않는 것이 좋다.

또 다른 대안으로 Facebook이 제공하는 [Immutable.js](https://facebook.github.io/immutable-js/)를 사용하는 방법이 있다.

Immutable.js는 List, Stack, Map, OrderedMap, Set, OrderedSet, Record와 같은 영구 불변 (Permit Immutable) 데이터 구조를 제공한다.

npm을 사용하여 Immutable.js를 설치한다.

immuatable의 Map 모듈을 import하여 사용한다.

```jsx
const { Map } = require('immutable')
const map1 = Map({ a: 1, b: 2, c: 3 })
const map2 = map1.set('b', 50)
map1.get('b') // 2
map2.get('b') // 50
```

map1.set(‘b’, 50)의 실행에도 불구하고 map1은 불변하였다. map1.set()은 결과를 반영한 새로운 객체를 반환한다.

----

#### 가변 API와 불변 API 비교

```javascript
var score = [1,2,3];
var a = score;
var b = score;
// 1~
score.push(4); // 원본을 바꾸는 방법 (score의 값을 바꿈), immutable하지 않음

var score2 = score.concat(4); // 원본을 복제한 복제본을 바꾼 결과를 리턴, immutable하게 원본 유지 가능
console.log(score, score2, a, b);
```

-----

#### Spread 연산자

