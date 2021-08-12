# Section07-1
# 파이썬 클래스 상세 이해
# Self, 클래스, 인스턴스 변수

# 클래스, 인스턴스 차이 중요
# 네임스페이스 : 객체(함수)를 인스턴스화(변수에 할당) 할 때 저장된 공간 -> 각각의 인스턴스 내에 존재하는 각각의 저장공간
# 클래스 변수 : 직접 사용 가능, 객체(함수)보다 먼저 생성
# 인스턴스 변수 : 객체(함수)마다 별도로 존재, 인스턴스 생성 후 사용

# 예제1


class UserInfo:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def print_info(self):
        print("Name: " + self.name)
        print("Height: " + str(self.height))

    def __del__(self):
        print("Instance removed!")


user1 = UserInfo("Kim", 183)
user2 = UserInfo("Park", 165)

print(id(user1))
print(id(user2))

user1.print_info()
user2.print_info()

print('user1 : ', user1.__dict__)  # 클래스 네임스페이스 확인
print('user2 : ', user2.__dict__)

print(user1.name)


# 예제2
# self의 이해

class SelfTest:
    def function1():
        print("function1 called!")

    def function2(self):
        print(id(self))
        print("function2 called!")


f = SelfTest()
# print(dir(f))
print(id(f))
# f.function1() #예외 발생
f.function2()
print(SelfTest.function1())


# print(SelfTest.function2()) #예외 발생


# 예제3
# 클래스 변수 , 인스턴스 변수(self)

class Warehouse:
    # 클래스 변수
    stock_num = 0

    def __init__(self, name):
        # 인스턴스 변수
        self.name = name
        Warehouse.stock_num += 1

    def __del__(self):
        Warehouse.stock_num -= 1


user1 = Warehouse('Kim')
user2 = Warehouse('Park')

print(user1.name)
print(user2.name)
print(user1.__dict__)
print(user2.__dict__)
print(Warehouse.__dict__)  # 클래스 네임스페이스 , 클래스 변수 (공유)

# Warehouse.stock_num = 50 # 직접 접근 가능

print(user1.stock_num)
print(user2.stock_num)
