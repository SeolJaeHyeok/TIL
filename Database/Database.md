Database의 본질은 Create,  Read, Update, Delete 즉, CRUD라고 부르는 것이다.

- Create
- Read
- Update
- Delete

----

데이터를 저장하기 위한 수단으로는 대표적으로 File, Spreadsheet, Database가 있다.

Spreadsheet는 File에서는 가능하지 못한 데이터의 구조화 및 가공을 가능하게 하는 수단이다.

Database는 Spreadsheet에서는 가능하지 못한 프로그래밍 언어를 통한 CRUD를 가능하게 하고 이는 곧 자동화를 할 수 있게 하는 수단이 된다.

즉, File과 Spreadsheet는 Database로 가는 길목에 존재하는 데이터 저장 수단이다.

- Database: SQL 이라는 컴퓨터 언어를 사용해 데이터 제어 가능
- Spreadsheet: 사용자의 클릭을 통해 데이터 제어 가능

데이터 베이스의 데이터들을 앱, 웹을 사용해 다른 이들에게도 보여줄 수 있음

----

# MySQL

테이블(Table): 데이터들이 저장되어 있는 표. 엑셀의 스트레트시트와 비슷한 구조를 지니고 있음

스키마(Schema) == 데이터베이스(Databse): 테이블들을 그룹핑(Grouping)하기 위한 일종의 디렉터리. 즉, 서로 연관된 데이터들을 그룹핑하기 위한 용도

데이터베이스 서버(Database Server): 그룹핑된 데이터들로 나누어진 여러 스키마들이 저장되어 있는 공간. Ex)MySQL, Oracel, MongoDB 등

<img src="./images/01.png" />

### 터미널을 통해 MySQL 서버에 접속하는 방법

1. Terminal에 `/usr/local/mysql/bin` 을 입력한다.

   <img src="./images/02.png" />

2. `./mysql -u[사용자명] -p` 명령어를 입력하고 비밀번호를 입력한 다음 접속을 한다.

   <img src="./images/03.png" />

<img src="./images/04.png" />

