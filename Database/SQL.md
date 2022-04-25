# 1. Basic

#### DESC

`DESC` 는 테이블의 구조를 출력하는 문이다.

```sql
DESC employees;

DESC students;
```

----

### 1. 테이블에서 데이터 검색

#### 테이블의 구성 *요소*

- 테이블이란 컬럼과 레코드로 구성된 표를 의미
- 컬럼은 열을 의미하고 주제나 제목 등을 나타낸다.
- 레코드는 행을 의미하고 내용이나 값을 나타낸다.
- 모든 테이블을 **고유의 이름**으로 구분

#### 테이블에서 데이터를 가져오는 대표적인 명령어 3가지 - SELECT, FROM, WHERE

**SELECT**

- 모든 쿼리의 시작점이며 엑셀의 필터 기능과 유사

- ```sql
  SELECT 검색할 대상;
  ```

**FROM**

- ~로부터 라는 뜻으로 특정 테이블에서 데이터를 조회할 때 사용

- ```sql
  FROM 테이블명;
  ```

**WHERE**

- 조건을 위한 명령어

- ```sql
  WHERE 조건
  ```

#### SELECT

***Syntax & Sample***

```sql
SELECT title, author -- 명령 + 검색할 컬럼
FROM book; -- 테이블

-- 세미 콜론을 통해서 쿼리문을 끝낸다
```

```sql
SELECT * -- 모든 컬럼 가져오기
FROM book;
```

```sql
SELECT DISTINCT title, author
FROM book
/*
1. DISTINCT는 '뚜렷한'이라는 사전적 의미와 같이 뒤에 나오는 컬럼에서 똑같은 데이터의 중복을 제거하고 보여준다. 다시 말해, DISTINCT는 중복을 제거하기 위해 사용하는 명렬

2. DISTINCT는 SELECT와 검색할 컬럼 사이에 위치해야 한다.

3. 2개 이상의 컬럼을 적으면 한 쪽 컬럼에 중복이 있어도 다른 쪽 컬럼의 값이 다르면 다르게 취급한다.
ex) 
1Q84 무라카미 하루키			1Q84 설재혁
와 같이 title 컬럼의 값이 같지만 author 컬럼의 값이 다르다면 
두 개의 데이터는 다르게 취급된다.
*/
```

----

### 2. 원하는 데이터만 검색 - 조건 설정하여 검색하기

**WHERE**

- 컬럼명을 통해 데이터를 검색하는 `SELECT` 와는 달리 `WHERE` 은 레코드명(데이터)를 통해 데이터를 검색

```sql
SELECT * -- 검색할 컬럼
FROM book -- 테이블
WHERE title = '1Q84'; -- 조건

/*

1. 제목이 '1Q84'인 책 데이터를 book 테이블에서 검색 

2. SQL에서 작은 따옴표는 문자열 상수 또는 날짜 / 시간 상수를 구분하고 큰 따옴표는 테이블 이름 또는 열 이름과 같은 식별자를 구분한다.
*/
```

***Syntax & Sample***

```sql
SELECT *
FROM employees
WHERE gender = 'M';

SELECT *
FROM book
WHERE author = 'Joanne Kathleen Rowling';
/*
1. employees 테이블로부터 성별이 남자인 직원만 검색
2. book 테이블로부터 작가가 Joanne Kathleen Rowling인 책만 검색
*/
```

----

### 3. 여러 개의 조건 추가

- 조건이 여러 개일 때 

  - ex) 성적을 저장하는 테이블 안에서 국어 성적이 90점 이상이거나 수학 성적이 80점 초과인 데이터를 검색하는 경우

- 비교 연산자는 기존의 프로그래밍 연산자와 동일하게 사용

  - 단, 동등 연산자는 `=` ,  `!=` 

- 복합조건 연산자 또한 기존 프로그래밍 연산자와 동일하게 사용

  - 단, `AND` 와 `&&`, `OR` 와 `||`, `NOT` 과 `!` 와 같이 두 가지 방법으로 모두 사용 가능

- 기타 연산자

  ```sql
  1. BETWEEN - 나이대 또는 날짜에서 많이 사용하는 연산자
  ex) A BETWEEN 10 AND 20
  - (10과 20을 포함해서) A가 두 값 사이에 포함된 값
  2. IN
  ex) A IN B
  - B에 A가 포함된 값
  3. NOT IN
  ex) A NOT IN B
  - B에 A가 포함되지 않은 값
  
  SELECT *
  FROM score
  WHERE math BETWEEN 80 AND 90
  
  /*
  1. (80과 90을 포함해서) score 테이블에서 수학 점수가 80과 90사이의 값 검색
  */
  ```

***Syntax & Sample***

```sql
SELECT *
FROM score
WHERE korean >= 90;

SELECT *
FROM score
WHERE math > 80;

SELECT *
FROM score
WHERE korean >= 90 OR math > 80;
/*
1. score 테이블에서 국어 성적이 90점 이상이 학생을 검색
2. score 테이블에서 수학 성적이 80점 초과인 학생을 검색
3. score 테이블에서 국어 성적이 90점 이상이거나 수학 성적이 80점 초과인 학생을 검색
*/
```

----

### 4. Exercise

```sql
SELECT *
FROM employees
WHERE 
(first_name = 'Chirstian' OR first_name = 'Georgi') 
AND 
gender = 'M'
AND 
hire_date != '1986-06-26';

/*
1. employees 테이블에서 first_name이 'Chirstian'이거나 'Georgi'이면서 gender는 남자고 hire_date는 '1986-06-26'이 아닌 데이터
*/
```

```sql
DESC score;

-- 짜장면을 받을 수 있는 학생을 조회하는 쿼리
SELECT *
FROM score
WHERE math = 100 OR korean = 100 OR english = 100;

-- 과자를 받을 수 있는 학생을 조회하는 쿼리
SELECT *
FROM score
WHERE 
math BETWEEN 70 AND 95
AND
korean BETWEEN 70 AND 95
AND
english BETWEEN 70 AND 95

/*
1. score 테이블에서 수학, 국어, 영어 중 하나라도 100점이 있는 학생을 검색
2. score 테이블에서 수학, 국어, 영어 성적이 모두 70점 ~ 95점인 학생을 검색
*/
```

```sql
-- 1980~1989년도에 입사한 직원
SELECT *
FROM employees
WHERE hire_date BETWEEN '1980-01-01' AND '1989-12-31';

-- 1990~1999년도에 입사한 직원
SELECT *
FROM employees
WHERE hire_date BETWEEN '1990-01-01' AND '1999-12-31';

/*
1. employees 테이블에서 1980-1989년도에 입사한 직원을 검색
2. employees 테이블에서 1990-1999년도에 입사한 직원을 검색
*/
```

```sql
-- 해당하는 작가가 쓴 책만 골라서 출력
SELECT *
FROM book
WHERE author = 'William Shakespeare' OR author = 'John Ronald Reuel Tolkien' OR author =  'Joanne Kathleen Rowling'

SELECT *
FROM book
WHERE author in ('William Shakespeare', 'John Ronald Reuel Tolkien', 'Joanne Kathleen Rowling')

/*
다음 작가가 작성한 책들만 검색
'William Shakespeare'
'John Ronald Reuel Tolkien'
'Joanne Kathleen Rowling'

1. OR 연산자를 통해 조건 설정
2. IN 연산자를 통해 조건 설정
두 값은 동일한 결과를 출력하지만 IN 연산자를 사용하는 것이 더욱 직관적이고 복잡한 조건을 설정할 필요도 없다.
*/
```

----

# 2. DML







