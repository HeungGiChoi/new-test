## 클래스

# 클래스의 정의
# class Car:
#     model = "" 
#     cc = 0

#     # 함수 추가
#     def info(self):
#         print(f'모델명은 {self.model}, 배기량은 {self.cc}cc 입니다.')

# car1 = Car() # 인스턴스 생성
# car1.model = 'K5'
# car1.cc = 2000

# car2 = Car() # 인스턴스 생성
# car2.model = '아반떼'
# car2.cc = 3500

# # print(f'모델명은 {car1.model}이고 {car1.cc}cc 입니다.')
# # print(f'모델명은 {car2.model}이고 {car2.cc}cc 입니다.')

# car1.info()
# car2.info()

# 생성자가 존재하는 클래스
# class Car:
#     def __init__(self, model, cc):
#         self.model = model
#         self.cc = cc
#     def info(self):
#         print(f'모델명은 {self.model}, 배기량은 {self.cc}cc 입니다.')
#     def __str__(self):
#         return f"모델: {self.model}, 배기량: {self.cc}"


# car1 = Car("싼타페", 2000)
# # car1.info()
# car2 = Car("페라리", 5000)
# # car2.info()

# print(car1)
# print(car2)

# # 객체 리스트
# print("승용차 리스트")
# cars = [
#     Car("소나타", 2000),
#     Car("쏘렌토", 2200),
#     Car("K5", 5000)
# ]
# for car in cars:
#     print(car)

# class 실습 1.

# class Plus_Minus:
#     def __init__(self, num1, num2):
#         self.num1 = num1
#         self.num2 = num2

#     def add(self):
#         print(f'{self.num1} + {self.num2} = {self.num1 + self.num2}')

#     def sub(self):
#         print(f'{self.num1} - {self.num2} = {self.num1 - self.num2}')

#     def mul(self):
#         print(f'{self.num1} * {self.num2} = {self.num1 * self.num2}')

#     def div(self):
#         print(f'{self.num1} / {self.num2} = {self.num1 // self.num2}')
    
# plus_minus = Plus_Minus(2, 3)

# plus_minus.add()
# plus_minus.sub()
# plus_minus.mul()
# plus_minus.div()

# 클래스 변수 / 인스턴스 변수
# class Dog:
#     kind = "진돗개" # 클래스 변수

#     def __init__(self, name):
#         self.name = name # 인스턴스 변수

# # 인스턴스 변수 접근
# ob1 = Dog("백구")
# print(ob1.name)
# # 클래스 변수 접근
# print(Dog.kind)

# class Example:
#     shared = "공유변수" # 클래스변수

#     def __init__(self, name):
#         self.name = name # 인스턴스 변수

# example1 = Example("A")
# example2 = Example("B")

# # 클래스변수 변경
# Example.shared = "변경된 변수"
# print(example1.shared)
# print(example2.shared)

# example1.name = "C"
# print(example1.name)
# print(example2.name)

# 사번 자동 발급
# class Employee:
#     Serial_num = 1000

#     def __init__(self, name):
#         self.name = name
#         Employee.Serial_num += 1 # 클래스변수 1씩 증가
#         self.id = Employee.Serial_num # 사번

#     def __str__(self):
#         return f"사번 : {self.id}, 이름 : {self.name}"
    
# e1 = Employee("홍길동")
# print(e1)
# e2 = Employee("임꺽정")
# print(e2)

# employees = [
#     Employee("이몽룡"),
#     Employee("전우치"),
#     Employee("변사또"),
#     Employee("성춘향")
# ]

# for i in employees:
#     print(i)

# 실습 3. 슈퍼마켓
# class Supermarket:
#     customers = 0

#     def __init__(self, location, name, product, customer):
#         self.location = location
#         self.name = name
#         self.product = product
#         self.customer = customer
    
#     def print_location(self):
#         print(f'위치: {self.location}')
    
#     def change_category(self, new_product):
#         self.product = new_product

#     def show_list(self):
#         print(f'상품: {self.product}')
    
#     def enter_customer(self):
#         Supermarket.customers += self.customer
    
#     def show_info(self):
#         print(f'위치: {self.location}, 가게이름: {self.name}, 상품: {self.product}, 고객수: {Supermarket.customers}')

# supermarket1 = Supermarket("서구 풍암동", "당근 마켓", "과자", 12)
# supermarket2 = Supermarket("강남구 양제동", "당근 마켓", "사과", 15)
# supermarket3 = Supermarket("강북구 연남동", "당근 마켓", "음료", 20)
# supermarket4 = Supermarket("강동구 몰라동", "당근 마켓", "오렌지", 13)
# supermarket5 = Supermarket("강서구 당근동", "당근 마켓", "쥬스", 8)


# supermarket1.print_location()
# supermarket1.show_list()
# supermarket1.enter_customer()
# supermarket1.show_info()

# supermarket2.print_location()
# supermarket2.show_list()
# supermarket2.enter_customer()
# supermarket2.show_info()

# supermarket3.print_location()
# supermarket3.show_list()
# supermarket3.enter_customer()
# supermarket3.show_info()

# supermarket4.print_location()
# supermarket4.show_list()
# supermarket4.enter_customer()
# supermarket4.show_info()

# supermarket5.print_location()
# supermarket5.show_list()
# supermarket5.enter_customer()
# supermarket5.show_info()


# 캡슐화
# class Person:
#     def __init__(self):
#         self._name = ""
#         self._age = 0

#     # 이름을 설정
#     def setname(self, name):
#         self._name = name

#     # 이름을 출력
#     def getname(self):
#         return self._name
    
#     # 나이를 설정
#     def setage(self, age):
#         self._age = age

#     # 나이를 출력
#     def getage(self):
#         return self._age
    
# p1 = Person()
# p1.setname("홍길동")
# print(p1.getname())

# p1.setage(20)
# print(p1.getage())

# getter, setter
# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age

#     # getter
#     @property
#     def name(self):
#         return self.__name
    
#     # setter
#     @name.setter
#     def name(self, name):
#         self.__name = name

#     # age getter
#     @property
#     def age(self):
#         return self.__age
    
#     # age setter
#     @age.setter
#     def age(self, age):
#         self.__age = age
    
# p1 = Person("홍길동", 20)
# print(p1.name)
# print(p1.age)

# p1.name = "최흥기"
# p1.age = 32

# print(p1.name)
# print(p1.age)