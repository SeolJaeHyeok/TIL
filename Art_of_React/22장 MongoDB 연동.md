이 장에서는 우리가 만들 Node.js 서버와 MongoDB를 연동할 수 있도록 MongoDB 기초 지식을 알아 본다. 그리고 mongoose를 이용하여 서버에서 직접 데이터를 추가, 조회, 삭제, 수정 하는 방법 또한 알아본다.

이번 실습은 다음과 같은 흐름으로 진행된다.

> MongoDB 기본 지식 알아보기 → 작업 환경 설정하기 → mongoose로 데이터베이스 연결하기 → esm로 ES 모듈 import/export 문법 사용하기 → 스키마와 모델 이해하기 → REST API 구현하기 → 페이지네이션 구현하기

## 22.1 소개

서버를 개발할 때 데이터베이스를 사용하면 웹 서비스에서 사용되는 데이터를 저장하고, 효율적으로 조회하거나 수정할 수 있다. 기존에는 MySQL, OracleDB, PostgreSQL 같은 RDBMS(관계형 데이터베이스)를 자주 사용했다.

그런데 관계형 데이터베이스는 몇 가지 한계가 있다.

첫 번째는 **데이터 스키마가 고정적이라는 것**이다. 여기서 스키마란 **데이터베이스에 어떤 형식의 데이터를 넣을지에 대한 정보** 를 뜻한다. 예를 들어 회원 정보 스키마라면 계정명, 이메일, 이름 등이 될 것이다. 새로 등록하는 데이터 형식이 기존에 있던 데이터들과 다르다면 기존 데이터를 모두 수정해야 새 데이터를 등록할 수 있다. 그래서 데이터양이 많을 때는 데이터베이스의 스키마를 변경하는 작업이 매우 번거로워질 수 있다.

두 번째는 **확장성**이다. RDBMS는 저장하고 처리해야 할 데이터양이 늘어나면 여러 컴퓨터에 분산시키는 것이 아니라, 해당 데이터베이스 서버의 성능을 업그레이드 하는 방식으로 확장해 주어야 했다.

MongoDB는 이런 한계를 극복한 문서 지향적 NoSQL 데이터베이스다. 이 데이터베이스에 등록하는 데이터들은 유동적인 스키마를 지닐 수 있다. **종류가 같은 데이터라고 하더라도, 새로 등록해야 할 데이터 형식이 바뀐다고 하더라도 기존 데이터까지 수정할 필요는 없다.** 서버의 데이터양이 늘어나도 한 컴퓨터에서만 처리하는 것이 아니라 여러 컴퓨터로 분산하여 처리할 수 있도록 확장하기 쉽게 설계되어 있다.

물론 MongoDB가 무조건 RDBMS보다 좋은 것은 아니다. 예를 들어 데이터의 구조가 자주 바뀐다면 MongoDB가 유리하지만, 까다로운 조건으로 데이터를 필터링해야 하거나 ACID 특성을 지켜야 한다면 RDBMS가 더 유리할 수 있다.

> ❗️ACID 특성이란 원자성(Atomicity), 일관성(Consistency), 고립성(Isolation), 지속성(Durability)의 앞 글자를 따서 만든 용어로, 데이터베이스 트랜잭션이 안전하게 처리되는 것을 보장하기 위한 성질을 의미

앞으로 구현하게 될 서버는 RDBMS로도 만들 수 있고, MongoDB로도 만들 수 있다. MongoDB를 사용하는 이유는 조금만 배워도 유용하게 활용할 수 있기 때문이다. 

#### 22.1.1 문서란?

여기서 말하는 *'문서(documents)'* 는 RDBMS의 *레코드('record')* 와 개념이 비슷하다. 문서의 데이터 구조는 한 개 이상의 키-값 쌍으로 되어 있다.

아래는 MongoDB에서 사용하는 문서 예시다.

```jsx
{
	"_id": ObjectId("55099803df3f4948bd2f98391"),
  "username": "milkboy",
  "name": { first: "J.H", last: "Seol"}
}
```

문서는 BSON(바이너리 형태의 JSON) 형태로 저장된다. 그렇기 때문에 나중에 JSON 형태의 객체를 데이터베이스에 저장할 때, 큰 공수를 들이지 않고도 데이터를 데이터베이스에 등록할 수 있어 매우 편하다.

새로운 문서를 만들면 _id라는 고윳값을 자동으로 생성하는데, 이 값은 시간, 머신 아이디, 프로세스 아이디, 순차 번호로 되어 있어 값의 고유함을 보장한다.

여러 문서가 들어 있는 곳을 *컬렉션*이라고 한다. 기존 RDBMS에서는 테이블 개념을 사용하므로 각 테이블마다 같은 스키마를 가지고 있어야 한다. 새로 등록해야 할 데이터가 다른 스키마를 가지고 있다면, 기존 데이터들의 스키마도 모두 바꾸어 주어야 한다.

반면 MongoDB는 다른 스키마를 가지고 있는 문서들이 한 컬렉션에서 공존할 수 있다. 다음 예시를 한번 보자.

```jsx
{
  "_id": ObjectId("594948a081ad6e0ea526f3f5"),
  "username": "milkboy"
},
{
  "_id": ObjectId("594948fca1ad6q4ed5f7f1c4"),
  "username": "milkboy2",
  "phone": "010-9996-3326"
}
```

처음에는 데이터에 전화번호가 필요 없었는데, 나중에 필요해졌다고 가정해 보자. RDBMS에서는 한 테이블의 모든 데이터가 같은 스키마를 가져야 하기 때문에, 기존 데이터 전체를 일일이 수정해야 한다. 하지만 MongoDB에서는 컬렉션 안의 데이터가 같은 스키마를 가질 필요가 없으므로 그냥 넣어 주면 된다.

#### 22.1.2 MongoDB 구조

MongoDB 구조는 다음과 같다. 서버 하나에 데이터베이스를 여러 개 가지고 있을 수 있다. 각 데이터베이스에는 여러 개의 컬렉션이 있으며, 컬렉션 내부에는 문서들이 들어 있다.

![](https://thebook.io/img/080203/639.jpg)

#### 22.1.3 스키마 디자인

MongoDB에서 스키마를 디자인하는 방식은 기존 RDBMS에서 스키마를 디자인하는 방식과 완전히 다르다. RDBMS에서 블로그용 데이터 스키마를 설계한다면 각 포스트, 댓글마다 테이블을 만들어 필요에 따라 *JOIN* 해서 사용하는 것이 일반적이다.

RDBMS에서 데이터베이스를 설계한다면 그 구조는 다음과 유사하다.

![](https://thebook.io/img/080203/639_2.jpg)

하지만 NoSQL에서는 그냥 모든 것을 문서 하나에 넣는다. 문서 예시의 형식을 한번 보게 되면

```javascript
{
  _id: ObjectId,
  title: String,
  body: String,
  username: String,
  createdDate: Date,  
  comments: [
    {
      _id: ObjectId,
      text: String,
      createdDateL Date,
    },
  ],
};
```

이런 상황에서 보통 MongoDB는 댓글을 포스트 문서 내부에 넣는다. 문서 내부에 또 다른 문서가 위치할 수 있는데, 이를 *서브다큐먼트(subdocument)*라고 한다. 서브다큐먼트 또한 일반 문서를 다루는 것처럼 쿼리할 수 있다.

문서 하나에는 최대 16MB만큼 데이터를 넣을 수 있는데 100자 댓글 데이터라면 대략 0.24KB를 차지한다. 16MB는 16,384KB이니 문서 하나에 댓글 데이터를 약 68000개 넣을 수 있는 것이다. 

서브 다큐먼트에서 이 용량을 초과할 가능성이 있다면 컬렉션을 분리시키는 것이 좋다.

## 22.2 MongoDB 서버 준비

#### 22.2.1 설치

MongoDB 서버를 사용하려면 우선 설치를 해야 한다.

**macOS**

macOS 사용사는 Homebrew를 이용하여 간편하게 설치할 수 있다.

`$ brew tap mongdb/brew`

`$ brew install mongodb-community@4.2`

`$ brew services start mongodb-community@4.2`

위 명령어를 입력하게 되면 설치할 수 있다.

(본인은 macOS를 사용중이므로 따로 윈도우 및 리눅스 환경에서의 설치법은 다루지 않겠다)

#### 22.2.2 MongoDB 작동 확인

MongoDB가 성공적으로 설치되었고 제대로  가동 중인지 확인하려면, 터미널에서 mongo를 입력하면 터미널 기반의 MongoDB 클라이언트가 실행되는 것을 확인할 수 있다.

<img src="./images/22_01.png" />

> ❗️
>
> 처음 mongo 명령어를 터미널에 실행하니 zsh: command not found: mongo 오류가 발생했었다.
>
> 이를 해결하기 위해 경로를 따로 설정을 해주는 작업을 거쳤는데
>
> .zshrc 파일 내에 들어가 **export PATH="$PATH:/usr/local/Cellar/mongodb-community@4.2/4.2.12/bin"** 
>
> 위 문장을 추가를 해줘서 해당 명령어의 경로를 저 위치로 설정을 해주니 해결이 됐다.

## 22.3 mongoose의 설치 및 적용

mongooose는 Node.js 환경에서 사용하는 MongoDB 기반 ODM(Object Data Modelling) 라이브러리다. 이 라이브러리는 데이터베이스 문서들을 자바스크립트 객체처럼 사용할 수 있게 해 준다.

우선 백엔드 프로젝트 디렉터리에서 아래 명령어를 입력해 라이브러리들을 설치해 준다.

`$ yarn add mongoose dotenv`

dotenv는 환경변수들을 파일에 넣고 사용할 수 있게 하는 개발 도구다. mongoose를 사용하여 MongoDB에 접속할 때, 서버에 주소나 계정 및 비밀번호가 필요할 경우도 있다. 이렇게 **민감하거나 환경별로 달라질 수 있는 값은 코드 안에 직접 작성하지 않고, 환경변수로 설정하는 것이 좋다.** 프로젝트를 깃허브, 깃랩 등의 서비스에 올릴 때는 .gitignore를 작성하여 환경변수가 들어 있는 파일은 제외시켜 주어야 한다.

#### 22.3.1 .env 환경변수 파일 생성

환경번수에는 서버에서 사용할 포트와 MongoDB 주소를 넣어 주도록 하자. 프로젝트의 루트 경로에 .env 파일을 만들고 아래와 같이 입력해 준다.

```jsx
PORT=4000
MONGO_URI=mongodb://localhost:27017/blog
```

여기서 blog는 우리가 사용할 데이터베이스 이름이다. 지정한 데이터베이스가 서버에 없다면 자동으로 만들어 주므로 사전에 직접 생성할 필요는 없다.

다음으로 src/index.js 파일의 맨 위에 다음과 같이 dotenv를 불러와서 config()함수를 호출해 준다. Node.js에서 환경변수는 process.env 값을 조회할 수 있다.

```jsx
require('dotenv').config();
const Koa = require('koa');
const Router = require('koa-router');
const bodyParser = require('koa-bodyparser');

// 비구조화 할당을 통해 process.env 내부 값에 대한 레퍼런스 만들기
const { PORT } = process.env;

const api = require('./api');

const app = new Koa();
const router = new Router();

// 라우터 설정
router.use('/api', api.routes()); // api 라우트 적용

// 라우터 적용 전에 bodyParser 적용
app.use(bodyParser());

// app 인스턴스에 라우터 적용
app.use(router.routes()).use(router.allowedMethods());

// PORT가 지정되어 있지 않다면 4000을 사용
const port = PORT || 4000;
app.listen(port, () => {
  console.log('Listening to port %d', port);
});
```

.env 파일에서 PORT를 4001로 변경한 뒤 서버를 재시작 해보면 (nodemon에서는 .env 파일을 변경할 때는 자동으로 재시작 하지 않으므로 직접 재시작 해야 한다.)

<img src="./images/22_02.png" />

위와 같이 바뀐 포트로 실행이 되는 것으 확인할 수 있다.

#### 22.3.2 mongoose로 서버와 데이터베이스 연결

이 mongoose를 이용하여 서버와 데이터베이스를 연결해보자. 연결할 때는 mongoose의 connect 함수를 사용한다.

```jsx
require('dotenv').config();
const Koa = require('koa');
const Router = require('koa-router');
const bodyParser = require('koa-bodyparser');
const mongoose = require('mongoose');

// 비구조화 할당을 통해 process.env 내부 값에 대한 레퍼런스 만들기
const { PORT, MONGO_URI } = process.env;

mongoose
  .connect(MONGO_URI, {
    useNewUrlParser: true,
    useFindAndModify: false,
    useUnifiedTopology: true,
  })
  .then(() => {
    console.log('Connected to MongoDB');
  })
  .catch((e) => {
    console.log(e);
  });

(...)
```

코드를 저장한 뒤 터미널을 보면 아래와 같은 문구가 나오는데 이는 데이터베이스가 성공적으로 연결된 것이고 mongoose를 사용할 준비가 끝난다.

<img src="./images/22_03.png" />

> ❗️
>
> 책에 서술된대로 입력하니 
>
> Warning: Current Server Discovery and Monitoring engine is deprecated, and will be removed in a future version. To use the new Server Discover and Monitoring engine, pass option { useUnifiedTopology: true } to the MongoClient constructor.
>
> 위와 같은 경고문이 나왔다.  이는 현재 서버 검색 및 모니터링 엔진은 더이상 사용되지 않으면 이후 버전에서 제거된다는 뜻이기에 
>
>  useUnifiedTopology: true 이 옵션을 MongoClient 생성자에게 전달해주면서 해결했다.

## 22.4 esm으로 ES 모듈 import/export 문법 사용하기

기존 리액트 프로젝트에서 사용해 오던 ES 모듈 import/export 문법은 Node.js에서 아직 정식으로 지원되지 않는다. Node.js에 해당 기능이 구현되어 있기는 하지만 아직 실험적인 단계이기 때문에 기본 옵션으로는 사용할 수 없으며, 확장자를 .mjs로 사용하고 node를 실행할 때 --experimental-modules라는 옵션을 넣어 주어야 한다.

Node.js에서 import/export 문법을 꼭 사용해야 할 필요는 없지만, 이 문법을 사용하면 VSC에서 자동 완성을 통해 모듈을 자동으로 쉽게 불러올 수 있고 코드도 더욱 깔끔해진다. 그래서 esm이라는 라이브러리를 이용해 해당 문법을 사용해보도록 하자.

먼저 `$ yarn add esm` 으로 라이브러리를 설치해 주고 기존 src/index.js 파일의 이름을 main.js로 변경하고, index.js 파일을 새로 생성해서 다음과 같이 입력해 준다.

```jsx
// 이 파일에서만 no-global-assgin ESLint 옵션을 비활성화 한다.
// eslint-disable no-global-assign

require = require('esm')(module /*, option */);
module.exports = require('./main.js');
```

그런 다음 package.json에서 만들었던 스크립트를 조금 수정해 준다.

```jsx
{
  (...)
  "scripts": {
    "start": "node -r esm src",
    "start:dev": "nodemon --watch src/ -r esm src/index.js"
  }
}

```

ESLint에서 import/export 구문을 사용해도 오류로 간주하지 않도록 다음과 같이 .eslintrc.json에서 soureType 값을 "module"로 설정해 준다.

```jsx
{
  "env": {
    "node": true,
    "commonjs": true,
    "es6": true
  },
  "extends": ["eslint:recommended", "prettier"],
  "globals": {
    "Atomics": "readonly",
    "SharedArrayBuffer": "readonly"
  },
  "parserOptions": {
    "ecmaVersion": 2018,
    "soureType": "module"
  },
  "rules": {}
}

```

이제 프로젝트에서 import/export 구문을 자유롭게 사용할 수 있다. 

기존에 실행 중이던 서버는 종료하고, 다시 `yarn start:dev` 명령어를 입력하고 새로운 스크립트로 서버를 구동한다.

#### 22.4.1 기존 코드 ES Module 형태로 바꾸기

먼저 api/posts/posts.ctrl.js 파일을 열어 exports 코드를 export const로 모두 변환해 준다.

```jsx
(...)
export const write = (ctx) => {
  (...)
};

export const list = (ctx) => {
  ctx.body = posts;
};

export const read = (ctx) => {
  (...)
};

export const remove = (ctx) => {
  (...)
};

export const replace = (ctx) => {
	(...)
};

export const update = (ctx) => {
  (...)
};
```

다음 src/api/posts/index.js 파일 수정하자.

```jsx
import Router from 'koa-router';
import * as postsCtrl from './posts.ctrl';

const posts = new Router();

posts.get('/', postsCtrl.list);
posts.post('/', postsCtrl.write);
posts.get('/:id', postsCtrl.read);
posts.delete('/:id', postsCtrl.remove);
posts.put('/:id', postsCtrl.replace);
posts.patch('/:id', postsCtrl.update);
export default posts;
```

이제 다음 두 파일을 수정하자.

```jsx
import Router from 'koa-router';
import posts from './posts';

const api = new Router();

api.use('/posts', posts.routes());

// 라우터를 내보낸다.
export default api;
```

```jsx
require('dotenv').config();
import Koa from 'koa';
import Router from 'koa-router';
import bodyParser from 'koa-bodyparser';
import mongoose from 'mongoose';

import api from './api';

// 비구조화 할당을 통해 process.env 내부 값에 대한 레퍼런스 만들기
const { PORT, MONGO_URI } = process.env;

(...)
```

이제 Postman으로 http://localhost:4000/api/posts에 요청을 보내면 우리가 만든 서버가 오류 발생으로 종료되지 않고 잘 작동하는 것을 확인할 수 있다.

이제 마지막으로 프로젝트 루트 디렉터리에 jsconfig.json을 작성해 준다.

```jsx
{
  "compilerOptions": {
    "target": "es6",
    "module": "es2015"
  },
  "include": ["src/**/*"]
}
```

이 파일을 위 코드와 같이 작성해 주면 나중에 자동 완성을 통해 모듈을 불러올 수 있다. Src 디렉터리에 sample.js라는 파일을 작성하고, api를 입력했을 때 자동 완성할 수 있는 인텔리센스창이 뜨는지 확인해 보자.

<img src="./images/22_04.png" />

이 상태에서 엔터를 누르면 import가 잘 될 것이다. 확인이 됐으면 sample.js는 삭제해 준다.

## 22.5 데이터베이스의 스키마와 모델

mongoose에는 스키마와 모델이라는 개념이 있는데, 이 둘은 혼동하기 쉽다. 스키마는 컬렉션에 들어가는 문서 내부의 각 필드가 어떤 형식으로 되어 있는 지 정의하는 객체다. 이와 달리 모델은 스키마를 사용하여 만드는 인스턴스로, 데이터베이스에서 실제 작업을 처리할 수 있는 함수들을 지니고 있는 객체다.

![](https://thebook.io/img/080203/651.jpg)

#### 22.5.1 스키마 생성

모델을 만들려면 사전에 스키마를 만들어 주어야 한다. 우리는 블로그 포스트에 대한 스키마를 준비할 텐데, 어떤 데이터가 필요할지 한 번 생각해보자.

- 제목
- 내용
- 태그
- 작성일

포스트 하나에 이렇게 총 네 가지 정보가 필요하다. 각 정보에 대한 필드 이름과 데이터 타입을 설정하여 스키마를 만든다.

| 필드 이름     | 데이터 타입 | 설명      |
| ------------- | ----------- | --------- |
| title         | 문자열      | 제목      |
| body          | 문자열      | 내용      |
| tags          | 문자열 배열 | 태그 목록 |
| publishedDate | 날짜        | 작성 날짜 |

이렇게 네 가지 필드가 있는 스키마를 만들어 보자. 스키마와 모델에 관련된 코드는 src/models 디렉터리에 작성한다. 이렇게 디렉터리를 따로 만들어서 관리하면 나중에 유지 보수를 좀 더 편하게 할 수 있다. models 디렉터리를 만들고, 그 안에 post.js 파일을 만들어 아래와 같이 작성해 준다.

```jsx
import mongoose from 'mongoose';

const { Schema } = mongoose;

const PostSchema = new Schema({
  title: String,
  body: String,
  tags: [String], // 문자열로 이루어진 배열
  publishedDate: {
    type: Date,
    default: Date.now, // 현재 날짜를 기본값으로 지정
  },
});
```

스키마를 만들 때는 mongoose 모듈의 Schema를 사용하여 정의한다. 그리고 각 필드 이름과 필드의 데이터 타입 정보가 들어 있는 객체를 작성한다. 필드의 기본값으로는 default 값을 설정해 주면 된다.

Schema에서 기본적으로 지원하는 타입을 다음과 같다.

| 타입                            | 설명                                         |
| ------------------------------- | -------------------------------------------- |
| String                          | 문자열                                       |
| Number                          | 숫자                                         |
| Date                            | 날짜                                         |
| Buffer                          | 파일을 담을 수 있는 버퍼                     |
| Boolean                         | True 또는 false 값                           |
| Mixed(Schema.Types.Mixed)       | 어떤 데이터도 넣을 수 있는 형식              |
| ObjectId(Schema.Types.ObjectId) | 객체 아이디, 주로 다른 객체를 참조할 때 사용 |
| Array                           | 배열 형태의 값으로 []로 감싸서 사용          |

우리가 만들 프로젝트에는 필요하지 않지만, 이 스키마를 활용하여 좀 더 복잡한 방식의 데이터도 저장할 수 있다.

```jsx
const AuthorSchema = new Schema({
  name: String,
  email: String,
});
const BookSchema = new Schema({
  title: String,
  description: String,
  authors: [AuthorSchema],
  meta: {
    likes:Number,
  },
  extra: Schema.Types.Mixed
});
```

위 코드에서 authors 부분에 [AuthorSchema]를 넣어 주었는데 이는 Author 스키마로 이루어진 여러 개의 객체가 들어 있는 배열을 의미한다. 이렇게 스키마 내부에 다른 스키마를 내장시킬 수도 있다.

#### 22.5.2 모델 생성

모델을 만들 때는 mongoose.model 함수를 사용한다. post.js 파일 맨 하단에 다음 코드를 입력해 준다.

```jsx
import mongoose from 'mongoose';

const { Schema } = mongoose;

const PostSchema = new Schema({
  title: String,
  body: String,
  tags: [String], // 문자열로 이루어진 배열
  publishedDate: {
    type: Date,
    default: Date.now, // 현재 날짜를 기본값으로 지정
  },
});

const Post = mongoose.model('Post', PostSchema);
export default Post;
```

모델 인스턴스를 만들고, export default를 통해 내보내 주었다. 여기서 사용한 model() 함수는 기본적으로 두 개의 파라미터가 필요하다. 첫 번째 파라미터는 스키마 이름이고, 두 번째 파라미터는 스키마 객체다. 데이터베이스는 스키마 이름을 정해 주면 그 이름의 복수 형태로 데이터베이스에 컬렉션 이름을 만든다.

예를 들어 스키마 이름을 Post로 설정하면, 실제 데이터베이스에 만드는 컬렉션 이름은 posts다. BookInfo로 입력하면 bookinfos를 만든다.

MongoDB에서 컬렉션 이름을 만들 때, 권장되는 컨벤션은 구분자를 사용하지 않고 복수 형태로 사용하는 것이다. 이 컨벤션을 따르고 싶지 않다면, 다음 코드 처럼 세 번쨰 파라미터에 원하는 이름을 입력하면 된다.

```jsx
mongoose.model('Post', PostSchema, 'custom_book_collection');
```

이 경우 첫 번째 파라미터로 넣어 준 이름은 나중에 다른 스키마에서 현재 스키마를 참조해야 하는 상황에서 사용한다.

