# JWT를 통한 회원 인증 시스템 구현하기

## 23.1 JWT의 이해

이 장에서는 우리가 만든 서버에 회원 인증 시스템을 구현해 보자. 이 시스템을 구현하기 위해 JWT라는 기술을 사용한다. JWT는 JSON Web Token의 약자로, 데이터가 JSON으로 이루어져 있는 토큰을 의미한다. 두 개체가 서로 안전하게 정보를 주고 받을 수 있도록 웹 표준으로 정의된 기술이다.

#### 23.1.1 세션 기반 인증과 토큰 기반 인증의 차이

사용자의 로그인 상태를 서버에서 처리하는 데 사용할 수 있는 대표적인 두 가지 인증방식이 있다. 하나는 세션을 기반으로 인증하는 것이고, 다른 하나는 토큰을 기반으로 인증하는 것이다. 두 방식의 차이점에 대해서 알아보도록 하자.

**세션 기반 인증 시스템**

세션을 기반으로 인증 시스템을 만든다는 것은 어떤 의미일까? 한마디로 말하면, 서버가 사용자가 로그인 중임을 기억하고 있다는 뜻이다.

![](https://media.vlpt.us/images/zwon111/post/faab80bb-9450-4e17-811f-e057077e3cfe/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202020-08-03%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%203.30.12.png)

세션 기반 인증 시스템에서 사용자가 로그인을 하면, 서버는 세션 저장소에 사용자의 정보를 조회하고 세션 id를 발급한다. 발급된 id는 주로 브라우저의 쿠키에 저장한다. 그다음에 사용자가 다른 요청을 보낼 때마다 서버는 세션 저장소에서 세션을 조회한 후 로그인 여부를 결정하여 작업을 처리하고 응답을 한다. 세션 저장소는 주로 메모리, 디스크, DB 등을 사용한다.

세션 기반 인증의 단점은 서버를 확장하기가 번거로울 수 있다는 점이다. 만약 서버의 인스턴스가 여러 개가 된다면, 모든 서버끼리 같은 세션을 공유해야 하므로 세션 전용 데이터베이스를 만들어야 할 뿐 아니라 신경 써야 할 것도 많다.

**토큰 기반 인증 시스템**

토큰은 로그인 이후 서버가 만들어 주는 문자열이다. 해당 문자열 안에는 사용자의 로그인 정보가 들어 있고, 해당 정보가 서버에서 발급되었음을 증명하는 서명이 들어 있다.

서명 데이터는 해싱 알고리즘을 통해 만들어지는데, 주로 HMAC SHA256 혹은 RSA SHA 256알고리즘이 사용된다.

![](https://media.vlpt.us/images/zwon111/post/de9008b9-c927-4698-99c0-06caacd93673/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202020-08-03%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%203.37.30.png)

**서버에서 만들어 준 토큰은 서명이 있기 때문에 무결성이 보장**된다. 여기서 무결성이란 정보가 변경되거나 위조되지 않았음을 의미하는 성질이다. 사용자가 로그인을 하면 서버에서 사용자에게 해당 사용자의 정보를 지니고 있는 토큰을 발급해 주고, 추후 사용자가 다른 API를 요청하게 될 때 발급받은 토큰과 함께 요청하게 된다. 그러면 서버는 해당 토큰이 유효한지 검사하고, 결과에 따라 작업을 처리하고 응답한다.

토큰 기반 인증시스템의 장점은 서버에서 사용자 로그인 정보를 기억하기 위해 사용하는 리소스가 적다는 것이다. 사용자 쪽에서 로그인 상태를 지닌 토큰을 가지고 있으므로 서버의 확장성이 매우 높다. 서버의 인스턴스가 여러 개로 늘어나도 서버끼리 사용자의 로그인 상태를 공유하고 있을 필요가 없다.

여기서는 두 가지 시스템 중 토큰 기반 인증 시스템을 사용할 예정이다. 실습은 다음과 같은 흐름으로 진행된다.

> User 스키마/모델 만들기 → 회원 인증 API 만들기 → 토큰 발급 및 검증하기 → posts API에 회원 인증 시스템 도입하기 → username/tags로 포스트 필터링 하기

## 23.2 User 스키마/모델 만들기

User 스키마와 모델을 작성하여 사용자의 정보를 MongoDB에 담고 조회해 보자. 앞으로 만들 사용자 스키마에는 사용자 계정명과 비밀번호가 필요하다.

비밀번호를 데이터베이스에 저장할 때 플레인 텍스트로 저장하면 보안상 매우 위험하다. 따라서 단방향 해싱 함수를 지원해 주는 bcrypt라는 라이브러리를 사용하여 비밀번호를 안전하게 저장해줘야 한다.

우선 User model을 만들고 스키마를 작성한다.

```jsx
import mongoose, { Schema } from 'mongoose';

const UserSchema = new Schema({
  username: String,
  hashedPassword: String,
});

const User = mongoose.model('User', UserSchema);
export default User;
```

다음으로 해시를 만드는 함수와 해시를 검증하는 함수를 만들텐데 먼저 bcrypt를 설치해 준다.

`$ yarn add bcrypt`

#### 23.2.1 모델 메서드 만들기

모델 메서드는 모델에서 사용할 수 있는 함수를 의미하며, 두 가지 종류가 있다. 첫 번째는 인스턴스 메서드로, 몯레을 통해 만든 문서 인스턴스에서 사용할 수 있는 함수를 의미한다.

두 번째는 스태틱 메서드로, 모델에서 바로 사용할 수 있는 함수를 의미한다.

**인스턴스 메서드 만들기**

이제 모델에서 사용할 두 개의 인스턴스 메서드를 만들어 보자. 첫 번째 메서드는 setPassword다. 이 메서드를 통해 비밀번호를 파라미터로 받아서 계정의 hashedPassword 값을 설정해 준다. 

두 번째 메서드는 checkPassword다. 이 메서드는 파라미터로 받은 비밀번호가 해당 계정의 비밀번호와 일치하는지 검증해 준다.

```jsx
import mongoose, { Schema } from 'mongoose';
import bcrypt from 'bcrypt';

const UserSchema = new Schema({
  username: String,
  hashedPassword: String,
});

UserSchema.methods.setPassword = async function (password) {
  const hash = bcrypt.hash(password, this.hashedPassword);
  this.hashedPassword = hash;
};

UserSchema.methods.checkPassword = async function (password) {
  const result = await bcrypt.compare(password, this.hashedPassword);
  return result; // True of False
};

const User = mongoose.model('User', UserSchema);
export default User;
```

인스턴스 메서드를 작성할 때는 화살표 함수가 아닌 function 키워드를 사용하여 구현해야 한다. 함수 내부에서 this에 접근해야 하기 때문인데 여기서 this는 문서 인스턴스를 가리킨다. 화살표 함수를 사용하게 되면 this는 문서 인스턴스를 가리키지 못하게 된다.

#### 23.2.2 스태틱 메서드 만들기

이번에는 스태틱 메서드를 만들어 보자. findByUsername이라는 메서드를 작성할텐데 이 메서드는 username으로 데이터를 찾을 수 있게 해 준다.

```jsx
import mongoose, { Schema } from 'mongoose';
import bcrypt from 'bcrypt';

const UserSchema = new Schema({
  username: String,
  hashedPassword: String,
});

UserSchema.methods.setPassword = async function (password) {
  const hash = bcrypt.hash(password, this.hashedPassword);
  this.hashedPassword = hash;
};

UserSchema.methods.checkPassword = async function (password) {
  const result = await bcrypt.compare(password, this.hashedPassword);
  return result; // True of False
};

UserSchema.statics.findByUsername = function (username) {
  return this.findOne({ username });
};

const User = mongoose.model('User', UserSchema);
export default User;
```

스태틱 함수에서의 this는 모델을 가리킨다. 여기서는 User를 가리키고 있다.