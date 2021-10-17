## 27.1 배열이란

배열은 여러 개의 값을 순차적으로 나열한 자료구조다. 배열은 사용 빈도가 매우 높은 가장 기본적인 자료구조다. 자바스크립트는 배열을 다루기 위한 유용한 메서드를 다수 제공한다. 아래 코드는 배열 리터럴을 통해 생성한 배열이다. 

```javascript
const arr = ['apple', 'banana', 'orange'];
```

배열이 가지고 있는 값을 **요소<sup>element</sup>** 라고 부른다. 자바스크립트의 모든 값은 배열의 요소가 될 수 있다. 즉, 원시값은 물론 객체, 함수, 배열 등 자바스크립트에서 값으로 인정하는 모든 것은 배열의 요소가 될 수 있따.

배열의 요소는 배열에서 자신의 위치를 나타내는 0 이상의 정수인 인덱스를 갖는다. 인덱스는 배열의 요소에 접근할 때 사용하는데 대부분의 언어에서 인덱스는 0부터 시작한다.

요소에 접근하려고 할 때는 대괄호 표기법을 사용한다. 대괄호 내에는 접근하고 싶은 요소의 인덱스를 지정한다.

```javascript
arr[0] // -> 'apple'
arr[1] // -> 'banana'
arr[2] // -> 'orange'
```

배열은 요소의 개수, 즉 배열의 길이를 나타내는 `length` 프로퍼티를 갖는다.

```javascript
arr.length // -> 3
```

배열은 인덱스와 `length` 프로퍼티를 갖기 때문에 `for` 문을 통해 순차적으로 요소에 접근할 수 있다.

```javascript
// 배열의 순회
for (let i = 0; i < arr.length; i++) {
  console.log(arr[i]); // 'apple' 'banana' 'orange'
}
```

자바스크립트에 배열이라는 타입은 존재하지 않는다. 배열은 객체 타입이다.

```javascript
typeof arr // -> object
```

배열은 배열 리터럴, `Array` 생성자 함수, `Array.of`, `Array.from` 메서드로 생성할 수 있다. 배열의 생성자 함수는 `Array` 이며, 배열의 프로토타입 객체는 `Array.prototype` 이다. `Array.prototype` 은 배열을 위한 빌트인 메서드를 제공한다.

```javascript
const arr = [1, 2, 3];

arr.constructor === Array // -> true
Object.getPrototypeOf(arr) === Array.prototype // -> true
```

배열은 객체지만 일반 객체와는 구별되는 독특한 특징이 있다.

|      구분       |           객체            |     배열      |
| :-------------: | :-----------------------: | :-----------: |
|      구조       | 프로퍼티 키와 프로퍼티 값 | 인덱스와 요소 |
|    값의 참조    |        프로퍼티 키        |    인덱스     |
|    값의 순서    |             X             |       O       |
| length 프로퍼티 |             X             |       O       |

일반 객체와 배열을 구분하는 가장 큰 특징은 값의 순서와 `length` 프로퍼티다. 인덱스로 표현되는 값의 순서와 `length` 프로퍼티를 갖는 배열은 반복문을 통해 순차적으로 값에 접근하기 위해 적합한 자료구조다.

```javascript
const arr = [1, 2, 3];

// 반복문으로 자료 구조를 순서대로 순회하기 위해서는 자료 구조의 요소에 순서대로
// 접근할 수 있어야 하며 자료 구조의 길이를 알 수 있어야 한다.
for (let i = 0; i < arr.length; i++) {
  console.log(arr[i]); // 1 2 3
}
```

배열의 장점은 처음부터 순차적으로 요소에 접근할 수도 있고, 마지막부터 역순으로 요소에 접근할 수도 있으며, 특정 위치부터 순차적으로 요소에 접근할 수도 있다. 이는 배열이 인덱스, 즉 값의 순서와 `length` 프로퍼티를 갖기 때문에 가능한 것이다.

## 27.2 자바스크립트 배열은 배열이 아니다

자료구조에서 말하는 배열은 동일한 크기의 메모리 공간이 빈틈없이 연속적으로 나열된 자료구조를 말한다. 즉, 배열의 요소는 하나의 데이터 타입으로 통일되어 있으며 서로 연속적으로 인접해 있다. 이러한 배열을 밀집 배열이라 한다.

이처럼 일반적인 의미의 배열은 각 요소가 동일한 데이터 크기를 가지며, 빈틈없이 연속적으로 이어져 있으므로 다음과 같이 인덱스를 통해 단 한 번의 연산으로 임의의 요소에 접근할 수 있다. 이는 매우 효율적이며, 고속으로 동작한다. 

**검색 대상 요소의 메모리 주소 = 배열의 시작 메모리 주소 + 인덱스 * 요소의 바이트 수**

예를 들어, 메모리 주소 1000에서 시작하고 각 요소가 8바이트인 배열을 생각해 보자.

- 인덱스가 0인 요소의 메모리 주소: 1000 + 0 * 8 = 1000
- 인덱스가 1인 요소의 메모리 주소: 1000 + 1 * 8 = 1008
- 인덱스가 2인 요소의 메모리 주소: 1000 + 2 * 8 = 1016

이처럼 배열은 인덱스를 통해 효율적으로 요소에 접근할 수 있다는 장점이 있다. 하지만 정렬되지 않은 배열에서 특정한 요소를 검색하는 경우 배열의 모든 요소를 처음부터 특정 요소를 발견할 때까지 차례대로 검색(선형 탐색, O(n))해야 한다.

```javascript
// 선형 검색을 통해 배열(array)에 특정 요소(target)가 존재하는지 확인한다.
// 배열에 특정 요소가 존재하면 특정 요소의 인덱스를 반환하고, 존재하지 않으면 -1을 반환한다.
function linearSearch(array, target) {
  const length = array.length;

  for (let i = 0; i < length; i++) {
    if (array[i] === target) return i;
  }

  return -1;
}

console.log(linearSearch([1, 2, 3, 4, 5, 6], 3)); // 2
console.log(linearSearch([1, 2, 3, 4, 5, 6], 0)); // -1
```

또한 배열에 요소를 삽입하거나 삭제하는 경우 요소를 연속적으로 유지하기 위해 요소를 이동시켜야 하는 단점도 있다.

자바스크립트의 배열은 지금까지 살펴본 자료구조에서 말하는 일반적인 의미의 배열과 다르다. 즉, 배열의 요소를 위한 각각의 메모리 공간은 동일한 크기를 갖지 않아도 되며, 연속적으로 이어져 있지 않을 수도 있다. 배열의 요소가 연속적으로 이어져 있지 않는 배열을 **희소 배열**이라 한다.

이처럼 자바스크립트의 배열은 엄밀히 말해 일반적인 의미의 배열은 아니다. **자바스크립트의 배열은 일반적인 배열의 동작을 흉내 낸 특수한 객체다.**

```javascript
// "16.2. 프로퍼티 어트리뷰트와 프로퍼티 디스크립터 객체" 참고
console.log(Object.getOwnPropertyDescriptors([1, 2, 3]));
/*
{
  '0': {value: 1, writable: true, enumerable: true, configurable: true}
  '1': {value: 2, writable: true, enumerable: true, configurable: true}
  '2': {value: 3, writable: true, enumerable: true, configurable: true}
  length: {value: 3, writable: true, enumerable: false, configurable: false}
}
*/
```

이처럼 자바스크립트 배열은 인덱스를 나타내는 문자열을 프로퍼티 키로 가지며, `length` 프로퍼티를 갖는 특수한 객체다. 자바스크립트 배열의 요소는 사실 프로퍼티 값이다. 자바스크립트에서 사용할 수 있는 모든 값은 객체의 프로퍼티 값이 될 수 있으므로 어떤 타입의 값이라도 배열의 요소가 될 수 있다.

```javascript
const arr = [
  'string',
  10,
  true,
  null,
  undefined,
  NaN,
  Infinity,
  [ ],
  { },
  function () {}
];
```

일반적인 배열과 자바스크립트의 배열의 장단점을 정리해보면 다음과 같다.

- 일반적인 배열은 인덱스로 요소에 빠르게 접근할 수 있다. 하지만 특정 요소를 검색하거나 요소를 삽입 또는 삭제하는 경우에는 효율적이지 않다.
- 자바스크립트 배열은 해시 테이블로 구현된 객체이므로 인덱스로 요소에 접근하는 경우는 일반적인 배열보다 성능적인 면에서 느릴수 밖에 없는 구조적인 단점이 있다. 하지만 특정 요소를 검색하거나 삽입 또는 삭제하는 경우에는 일반적인 배열보다 빠른 성능을 기대할 수 있다.

즉, 자바스크립트 배열은 인덱스로 배열 요소에 접근하는 경우에는 일반적인 배열보다 느리지만 특정 요소를 검색하거나 요소를 삽입 또는 삭제하는 경우에는 일반적인 배열보다 빠르다. 자바스크립트 배열은 인덱스로 접근하는 경우의 성능 대신 특정 요소를 탐색하거나 배열 요소를 삽입 또는 삭제하는 경우의 성능을 선택한 것이다.

인덱스로 배열 요소에 접근할 때 일반적인 배열보다 느릴 수밖에 없는 구조적인 단점을 보완하기 위해 대부분의 모던 자바스크립트 엔진은 배열을 일반 객체와 구별하여 좀 더 배열처럼 동작하도록 최적화하여 구현했다. 

```javascript
const arr = [];

console.time('Array Performance Test');

for (let i = 0; i < 10000000; i++) {
  arr[i] = i;
}
console.timeEnd('Array Performance Test');
// 약 340ms

const obj = {};

console.time('Object Performance Test');

for (let i = 0; i < 10000000; i++) {
  obj[i] = i;
}

console.timeEnd('Object Performance Test');
// 약 600ms
```

## 27.3 length 프로퍼티와 희소 배열

`length` 프로퍼티는 요소의 개수, 즉 배열의 길이를 나타내는 0 이상의 정수를 값으로 갖는다. `length` 프로퍼티의 값은 빈 배열일 경우 0이며, 빈 배열이 아닐 경우 가장 큰 인덱스에 1을 더한 것과 같다.

```javascript
[].length        // -> 0
[1, 2, 3].length // -> 3
```

`length` 프로퍼티의 값은 0부터 2<sup>32</sup> - 1미만의 양의 정수다. 즉, 배열은 요소를 최대 2<sup>32</sup> - 1개 가질 수 있다. 따라서 배열에서 사용할 수 있는 가장 작은 인덱스는 0이며, 가장 큰 인덱스는 2<sup>32</sup> - 2다.

`length` 프로퍼티의 값은 배열에 요소를 추가하거나 삭제하면 자동 갱신된다.

```javascript
const arr = [1, 2, 3];
console.log(arr.length); // 3

// 요소 추가
arr.push(4);
// 요소를 추가하면 length 프로퍼티의 값이 자동 갱신된다.
console.log(arr.length); // 4

// 요소 삭제
arr.pop();
// 요소를 삭제하면 length 프로퍼티의 값이 자동 갱신된다.
console.log(arr.length); // 3
```

`length` 프로퍼티 값은 요소의 개수, 즉 배열의 길이를 바탕으로 결정되지만 임의의 숫자 값을 명시적으로 할당할 수도 있다.

현재 `length` 프로퍼티 값보다 작은 숫자 값을 할당하면 배열의 길이가 줄어든다.

```javascript
const arr = [1, 2, 3, 4, 5];

// 현재 length 프로퍼티 값인 5보다 작은 숫자 값 3을 length 프로퍼티에 할당
arr.length = 3;

// 배열의 길이가 5에서 3으로 줄어든다.
console.log(arr); // [1, 2, 3]
```

주의할 것은 현재 `length` 프로퍼티 값보다 큰 숫자 값을 할당하는 경우다. 이때 `length` 프로퍼티 값은 변경되지만 실제로 배열의 길이가 늘어나지는 않는다.

```javascript
const arr = [1];

// 현재 length 프로퍼티 값인 1보다 큰 숫자 값 3을 length 프로퍼티에 할당
arr.length = 3;

// length 프로퍼티 값은 변경되지만 실제로 배열의 길이가 늘어나지는 않는다.
console.log(arr.length); // 3
console.log(arr); // [1, empty × 2]
```

위 예제의 출력결과 상의 `empty x 2` 는 실제로 추가된 배열의 요소가 아니다. 즉 `arr[1]` 과 `arr[2]` 에는 값이 존재하지 않는다.

이처럼 `length` 프로퍼티 값보다 큰 숫자 값을 `length` 프로퍼티에 할당하는 경우 `length` 프로퍼티 값은 성공적으로 변경되지만 실제 배열에는 아무런 변함이 없다. 값 없이 비어 있는 요소를 위해 메모리 공간을 확보하지 않으면 빈 요소를 생성하지도 않는다.

```javascript
console.log(Object.getOwnPropertyDescriptors(arr));
/*
{
  '0': {value: 1, writable: true, enumerable: true, configurable: true},
  length: {value: 3, writable: true, enumerable: false, configurable: false}
}
*/
```

이처럼 배열의 요소가 연속적으로 위치하지 않고 일부가 비어 있는 배열을 희소 배열이라 한다. 자바스크립트는 희소 배열을 문법적으로 허용한다. 위 예제는 배열의 뒷부분만 비어 있어서 요소가 연속적으로 위치하는 것처럼 보일 수 있으나 중간이나 앞부분이 비어 있을 수도 있다.

```javascript
// 희소 배열
const sparse = [, 2, , 4];

// 희소 배열의 length 프로퍼티 값은 요소의 개수와 일치하지 않는다.
console.log(sparse.length); // 4
console.log(sparse); // [empty, 2, empty, 4]

// 배열 sparse에는 인덱스가 0, 2인 요소가 존재하지 않는다.
console.log(Object.getOwnPropertyDescriptors(sparse));
/*
{
  '1': { value: 2, writable: true, enumerable: true, configurable: true },
  '3': { value: 4, writable: true, enumerable: true, configurable: true },
  length: { value: 4, writable: true, enumerable: false, configurable: false }
}
*/
```

일반적인 배열의 `length` 는 배열 요소의 개수, 즉 배열의 길이와 언제나 일치한다. 하지만 **희소 배열은 `length` 와 배열 요소의 개수가 일치하지 않는다. 희소 배열의 `length` 는 희소 배열의 실제 요소 개수보다 언제나 크다.**

자바스크립트는 문법적으로 희소 배열을 허용하지만 희소 배열은 사용하지 않는 것이 좋다. 의도적으로 희소 배열을 만들어야 하는 상황은 발생하지 ㅇ낳는다. 희소 배열은 연속적인 값의 집합이라는 배열의 기본적인 개념과 맞지 않으며, 성능에도 좋지 않은 영향을 준다. 최적화가 잘 되어 있는 모던 자바스크립트 엔진은 요소의 타입이 일치하는 배열을 생성할 때 일반적인 의미의 배열처럼 연속된 메모리 공간을 확보하는 것으로 알려져 있다.

배열을 생성할 경우에는 희소 배열을 생성하지 않도록 주의하자. **배열에는 같은 타입의 요소를 연속적으로 위치시키는 것이 최선이다.**

## 27.4 배열 생성

#### 27.4.1 배열 리터럴

객체와 마찬가지로 배열에도 다양한 생성 방식이 있다. 가장 일반적이고 간편한 배열 생성 방식은 배열 리터럴을 사용하는 것이다.

배열 리터럴은 0개 이상의 요소를 쉼표로 구분하여 대괄호로 묶는다. 배열 리터럴은 객체 리터럴과 달리 프로퍼티 키가 없고 값만 존재한다.

```javascript
const arr = [1, 2, 3];
console.log(arr.length); // 3
```

배열 리터럴에 요소를 하나도 추가하지 않으면 배열의 길이, 즉 `length` 프로퍼티 값이 0인 빈 배열이 된다.

```javascript
const arr = [];
console.log(arr.length); // 0
```

배열 리터럴에 요소를 생략하면 희소 배열이 생성된다.

```javascript
const arrr = [1, , 3]; // 희소 배열

// 희소 배열의 length는 배열의 실제 요소 개수보다 언제나 크다.
console.log(arr.length); // 3
console.log(arr);				 // [1, empty, 3]
console.log(arr[1]);		 // undefined
```

위 예제의 `arr` 은 인덱스가 1인 요소를 갖지 않는 희소 배열이다. `arr[1]` 이 `undefined` 인 이유는 사실은 객체인 `arr` 에 프로퍼티 키가 '1'인 프로퍼티가 존재하지 않기 때문이다.

#### 27.4.2 Array 생성자 함수

`Object` 생성자 함수를 통해 객체를 생성할 수 있듯이 `Array` 생성자 함수를 통해 배열을 생성할 수도 있다. `Array` 생성자 함수는 전달된 인수의 개수에 따라 다르게 동작하므로 주의할 필요가 있다.

- 전달된 인수가 1개이고 숫자인 경우 `length` 프로퍼티 값이 인수인 배열을 생성한다.

  ```javascript
  const arr = new Array(10);
  
  console.log(arr); // [empty × 10]
  console.log(arr.length); // 10
  ```

  이때 생성된 배열은 희소 배열이다. `length` 프로퍼티 값은 0이 아니지만 실제 배열의 요소는 존재하지 않는다.

  ```javascript
  console.log(Object.getOwnPropertyDescriptors(arr));
  /*
  {
    length: {value: 10, writable: true, enumerable: false, configurable: false}
  }
  */
  ```

  배열은 요소를 최대 2<sup>32</sup> - 1(4,294,967,295)개 가질 수 있다. 따라서 `Array` 생성자 함수에 전달한 인수는 0 또는 2<sup>32</sup> - 1 이하인 양의 정수이어야 한다. 전달된 인수가 범위를 벗어나면 `RangeError` 가 발생한다.

  ```javascript
  // 배열은 요소를 최대 4,294,967,295개 가질 수 있다.
  new Array(4294967295);
  
  // 전달된 인수가 0 ~ 4,294,967,295를 벗어나면 RangeError가 발생한다.
  new Array(4294967296); // RangeError: Invalid array length
  
  // 전달된 인수가 음수이면 에러가 발생한다.
  new Array(-1); // RangeError: Invalid array length
  ```

- 전달된 인수가 없는 경우 빈 배열을 생성한다. 즉, 배열 리터럴 `[]` 과 같다.

  ```javascript
  new Array(); // -> []
  ```

- 전달된 인수가 2개 이상이거나 숫자가 아닌 경우 인수를 요소로 갖는 배열을 생성한다.

  ```javascript
  // 전달된 인수가 2개 이상이면 인수를 요소로 갖는 배열을 생성한다.
  new Array(1, 2, 3); // -> [1, 2, 3]
  
  // 전달된 인수가 1개지만 숫자가 아니면 인수를 요소로 갖는 배열을 생성한다.
  new Array({}); // -> [{}]
  ```

  `Array` 생성자 함수는 `new` 연산자와 함께 호출하지 않더라도, 즉 일반 함수로서 호출해도 배열을 생성하는 생성자 함수로 동작한다. 이는 `Array` 생성자 함수 내부에서 `new.target` 을 확인하기 때문이다.

  ```javascript
  Array(1, 2, 3); // -> [1, 2, 3]
  ```

#### 27.4.3 Array.of

ES6에서 도입된 `Array.of` 메서드는 전달된 인수를 요소로 갖는 배열을 생성한다. `Array.of` 는 `Array` 생성자 함수와 다르게 전달된 인수가 1개이고 숫자이더라도 인수를 요소로 갖는 배열을 생성한다.

```javascript
// 전달된 인수가 1개이고 숫자이더라도 인수를 요소로 갖는 배열을 생성한다.
Array.of(1); // -> [1]

Array.of(1, 2, 3); // -> [1, 2, 3]

Array.of('string'); // -> ['string']
```

#### 27.4.4 Array.from

ES6에서 도입된 `Array.from` 메서드는 유사 배열 객체 또는 이터러블 객체를 인수로 전달받아 배열로 변환하여 반환한다.

```javascript
// 유사 배열 객체를 변환하여 배열을 생성한다.
Array.from({ length: 2, 0: 'a', 1: 'b' }); // -> ['a', 'b']

// 이터러블을 변환하여 배열을 생성한다. 문자열은 이터러블이다.
Array.from('Hello'); // -> ['H', 'e', 'l', 'l', 'o']
```

`Array.from` 을 사용하면 두 번째 인수로 전달한 콜백 함수를 통해 값을 만들면서 요소를 채울 수 있다. `Array.from` 메서드는 두 번째 인수로 전달한 콜백 함수에 첫 번째 인수에 의해 생성된 배열의 요소값과 인덱스를 순차적으로 전달하면서 호출하고, 콜백 함수의 반환값으로 구성된 배열을 반환한다.

```javascript
// Array.from에 length만 존재하는 유사 배열 객체를 전달하면 undefined를 요소로 채운다.
Array.from({ length: 3 }); // -> [undefined, undefined, undefined]

// Array.from은 두 번째 인수로 전달한 콜백 함수의 반환값으로 구성된 배열을 반환한다.
Array.from({ length: 3 }, (_, i) => i); // -> [0, 1, 2]
```

> ❗️
>
> 유사 배열 객체와 이터러블 객체
>
> 유사 배열 객체는 마치 배열처럼 인덱스로 프로퍼티 값에 접근할 수 있고 `length` 프로퍼티를 갖는 객체를 말한다. 유사 배열 객체는 배열처럼 `for` 문으로 순회할 수도 있다.
>
> ```javascript
> // 유사 배열 객체
> const arrayLike = {
>   '0': 'apple',
>   '1': 'banana',
>   '2': 'orange',
>   length: 3
> };
> 
> // 유사 배열 객체는 마치 배열처럼 for 문으로 순회할 수도 있다.
> for (let i = 0; i < arrayLike.length; i++) {
>   console.log(arrayLike[i]); // apple banana orange
> }
> ```
>
> 이터러블 객체는 `Symbol.iterator` 메서드를 구현하여 `for...of` 문으로 순회할 수 있으며, 스프레드 문법과 배열 디스트럭처링 할당의 대상으로 사용할 수 있는 객체를 말한다.