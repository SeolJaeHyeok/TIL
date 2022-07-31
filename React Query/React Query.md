# React Query

참고

https://2ham-s.tistory.com/407

https://velog.io/@crazy4u2/React-Query-useQuery-%EC%9E%AC%EC%82%AC%EC%9A%A9

https://thinkforthink.tistory.com/340

https://thinkforthink.tistory.com/356?category=864727



## Stale Time

리액트 쿼리는 기본적으로 캐시된 데이터를 stale한 상태로 여긴다.
stale이란 최신화가 필요한 데이터라는 의미로 stale한 상태가 되면 다음의 경우에 refetch 된다.

- 새로운 query 인스턴스가 마운트될 때

- 브라우저 화면을 이탈했다가 다시 포커스할 때

- 네트워크가 다시 연결될 때

- 특별히 설정한 refetch interval에 의해서 (refetchInterval) 

refetchOnWindowFocus 옵션 등으로 기본 refetch 설정을 막을 수 있고
staleTime 옵션으로 설정한 시간 동안 데이터가 stale 되지 않도록 해 refetch를 막을 수도 있다.

query에 별다른 action이 없으면 inactive 상태로 캐시에 남아 있다가 5분 뒤에 메모리에서 사라진다.
cacheTime 옵션을 설정해서 이 시간을 조정할 수 있다.



## Caching

#### Caching이 안되는 이유  

react querysms staleTime으로 설정한 시간만큼 api 요청한 데이터의 신선도가 유지되고  이 시간이 지나면 fresh -> stale 상태

다시 말해 **신선하지 않은 데이터가 되어 똑같은 데이터를 다시 필요로 할 때 api 요청을 또다시 할 수 밖에 없고** 이러한 경우 캐싱을 정상적으로 이용할 수가 없다.   

따라서 **cacheTime은 staleTime보다 길어야 캐싱이 정상적으로 동작**하고  staleTime은 요구에 따라 적정한 시간으로 설정하는 것이 필요

React-query의 staleTime의 기본값은 0이고 cacheTime은 5분이다. 

이러한 경우 캐싱이 정상적으로 동작하지 않는 flow는 아래와 같다고 생각된다.

-> 요청한 데이터는 받아오자마자 신선하지 않은 데이터(stale)가 됌  -> 따라서 해당 데이터가 필요한 경우 API 요청이 또다시 발생  -> 때문에 staleTime을 기본값으로 설정하면 캐싱이 정상적으로 동작 X  -> why? 이전 API 요청을 통해 캐시된 데이터는 이미 신선하지 않은 데이터(stale)이기 때문에 계속해서 API 요청을 하게 됌 -> 이는 곧 서버 자원의 낭비로 이어짐

