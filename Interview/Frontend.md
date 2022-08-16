

## 프론트엔드 전반

### - 브라우저 렌더링 과정

[참고](https://github.com/baeharam/Must-Know-About-Frontend/blob/main/Notes/frontend/browser-rendering.md)

1. HTML 파싱 후 DOM(Document Object Model) 트리 구축
2. CSS 파싱 후 CSSOM(CSS Object Model) 트리 구축
3. JavaScript 실행 - 주의 HTML 중간에 스크립트가 있다면 HTML 파싱 중단
4. DOM트리와 CSSOM트리를 조합하여 렌더 트리 구축
5. 뷰포트를 기반으로 각 노드가 가지는 정확한 위치 설정(Layout/Reflow)
6. 위에서 계산된 위치를 바탕으로 화면에 Paint

----

### - CSR과 SSR

[참고](https://github.com/baeharam/Must-Know-About-Frontend/blob/main/Notes/frontend/csr-ssr.md)

**CSR(Client Side Rendering) **- 브라우저가 서버에 HTML파일과 JS 파일을 요청한 후 로드되고 사용자의 상호작용에 따라 JS를 이용하여 동적으로 화면을 렌더링 시킴

**장점**

-  초기 화면만 서버에 요청하여 렌더링 시키고 그 이후는 동적으로 빠르게 렌더링되기 때문에 사용자 경험이 좋다.
-  서버에 요청하는 횟수가 적어 서버에 부담이 덜하다

**단점**

- 모든 스크립트 파일이 로드될 때까지 기다려야 한다. 프로젝트의 규모가 커진다면 초기 화면 로딩이 길어질 수 있다.
  - 청크 파일 단위로 요청이 올때만 다운받게 할 수 있지만(코드 스플리팅) 완벽한 해결책은 아니다.
- 크롬을 제외한 다른 검색엔진들은 JS를 지원하지 않기 때문에 검색 엔진 봇이 크롤링하는 데에 문제가 있다. 따라서 검색 엔진 최적화의 어려움이 있다.

**SSR(Server Side Rendering)** - 브라우저의 요청이 있을 때마다 서버에 HTML, CSS, JS 파일 및 데이터 받아와서 화면을 렌더링 시킴

**장점**

- 초기 로딩 속도가 빠르다
- JS를 활용한 렌더링이 아니기 때문에 검색 엔진 최적화가 용이하다.

**단점**

- 매번 페이지를 요청할 때마다 새로고침되기 때문에 사용자 경험이 좋지 않다.
- 서버에 많은 요청을 하기 때문에 서버에 부담이 크다.

----

### - CI/CD

[참고](https://github.com/baeharam/Must-Know-About-Frontend/blob/main/Notes/frontend/ci-cd.md)

**CI(Continuous Integration)** - 지속적 통합, 빌드와 테스트를 자동화해서 공유 저장소에 병합시키는 프로세스를 말한다. git과 같은 버전 관리 시스템을 이용할 경우 여러 개발자들 하나의 저장소를 사용하는 경우가 많은데 새로운 커밋같은 변경사항들이 하나의 저장소에 통합되지 않을 경우 서로 충돌하는 경우가 생긴다. 이를 방지하고 빌드 테스트/자동화부터 코드의 일관성을 제공하는 것을 말한다. 

**CD(Continuous Delivery/Deploy)** - CD는 CI의 빌드/테스트를 통해 정상적으로 수행됨을 확인하면 배포를 수동으로 하느냐에 따라 2가지 단계로 나뉜다.

- 지속적 전달: 프로덕션 배포를 위한 상태가 되고 배포는 수동으로 이루어짐 -> 개발팀과 비즈니스팀의 커뮤니케이션 부족 문제를 해결할 수 있음
- 지속적 배포: 프로덕션까지 자동으로 배포 -> 어플리케이션 제공 속도 증가

Jenkins, gitlab 등

----

### - 모듈 번들러와 트랜스파일러

[참고](https://github.com/baeharam/Must-Know-About-Frontend/blob/main/Notes/frontend/bundler-transpiler.md)

**모듈 번들러** - 모듈 단위로 개발을 하게 된다면 수많은 모듈의 순서는 어떻게 처리할 것인가? 각각의 모듈마다 많은 HTTP 요청이 있을 것이고 이로 인한 오버헤드는 어떻게 처리할 것인가? ES6+ 스펙의 코드는 어떻게 처리할 것인가? 와 같은 문제들이 나타나게 된다. 이러한 문제점들을 해결하여 하나의 자바스크립트 파일로 만드는 도구를 모듈 번들러라고 말한다.

Webpack, Parcel, Rollup 등

**트랜스파일러** - 특정 언어로 작성된 파일을 다른 언어로 변환시키는 것을 트랜스파일링이라고 말하며 이를 수행하는 것이 트랜스파일러다. 예를 들어 리액트의 JSX 코드를 자바스크립트 코드로 변환한다거나 타입스크립트를 자바스크립트로 변환하는 것을 트랜스파일링이라고 하고 이를 도와주는 Babel과 같은 도구들을 트랜스파일러라고 한다.

