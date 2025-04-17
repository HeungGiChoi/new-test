# 실습 1.
# # 날짜, 지역, 온도, 강수량
# weather_data = [
#     ["2024-11-20", "서울", 15.2, 0.0],
#     ["2024-11-20", "부산", 18.4, 0.0],
#     ["2024-11-21", "서울", 10.5, 2.3],
#     ["2024-11-21", "부산", 14.6, 1.2],
#     ["2024-11-22", "서울", 8.3, 0.0],
#     ["2024-11-22", "부산", 12.0, 0.0]
# ]

# # 도시별 평균기온 계산
# def avg_temp(city1):
#     city_data = filter(lambda x: x[1] == city1, weather_data)
#     temp_data = list(map(lambda x: x[2],city_data))
#     avg_data1 = sum(temp_data) / len(temp_data)
#     return avg_data1

# # 도시별 최고/최소 기온 찾기
# def max_min_temp(city2):
#     city_data = filter(lambda x: x[1] == city2, weather_data)
#     temp_data = list(map(lambda x: x[2],city_data))
#     return temp_data

# # 도시별 강수량 분석
# def func_city(city3):
#     city_data = filter(lambda x: x[1] == city3, weather_data)
#     rain_data = list(map(lambda x: x[3],city_data))
#     rainday_count = [i for i in rain_data if i > 0.0]
#     return rain_data, rainday_count

# # 데이터 추가
# def add_weather_data():
#     day_input = input("날짜를 입력하세요 (YYYY-MM-DD): ")
#     city4 = input("도시를 입력하세요: ")
#     temp_data = input("평균 기온을 입력하세요 (℃): ")
#     rain_data = input("강수량을 입력하세요 (mm): ")
#     new_data = [day_input, city4, temp_data, rain_data]
#     weather_data.append(new_data)
#     print(f"{city4}의 날씨 데이터가 추가되었습니다.")

# # 전체 데이터 출력
# def print_allData():
#     for data in weather_data:
#         print(f"날짜: {data[0]}, 도시: {data[1]}, 평균 기온: {data[2]}℃, 강수량: {data[3]}mm")

# def main():
#     while True:
#         print("[날씨 데이터 분석 프로그램]")
#         print("1. 평균 기온 계산\n2. 최고/최저 기온 찾기\n3. 강수량 분석\n4.날씨 데이터 추가\n5. 전체 데이터 출력\n6. 종료")
#         func1 = input("원하는 기능의 번호를 입력하세요: ")
#         if func1 == '1':
#             city1 = input("도시 이름을 입력하세요: ")
#             city_name = [row[1] for row in weather_data]
#             if city1 in city_name:
#                 avg_temp1 = avg_temp(city1)
#                 print(f"{city1}의 평균 기온: {avg_temp1:.2f}")
#             else:
#                 print(f"{city1} 데이터가 없습니다. ")
#         elif func1 == '2':
#                 city2 = input("도시의 이름을 입력하세요: ")
#                 city_name = [row[1] for row in weather_data]
#                 if city2 in city_name:
#                     temp_data = max_min_temp(city2)
#                     print(f"{city2}의 최고 기온: {max(temp_data)}℃, 최저 기온: {min(temp_data)}℃")
#                 else:
#                     print(f"{city2} 데이터가 없습니다. ")
#         elif func1 == '3':
#             city3 = input("도시의 이름을 입력하세요: ")
#             city_name = [row[1] for row in weather_data]
#             if city3 in city_name:
#                 rain_data, rainday_count = func_city(city3)
#                 print(f"{city3}의 총 강수량: {sum(rain_data)}mm")
#                 print(f"{city3}의 강수량이 있었던 날: {len(rainday_count)}일")
#             else:
#                 print(f"{city3} 데이터가 없습니다. ")
#         elif func1 == '4':
#             add_weather_data()
#         elif func1 == '5':
#             print_allData()
#         elif func1 == '6':
#             print("[날씨 데이터 분석 프로그램 종료]")
#             break
#         else:
#             print("값을 잘못 입력하셨습니다. 1~6범위 내에서 다시 입력해주세요.")

# main()

# 실습 2.
# class Health:
#     def __init__(self):
#         self._name = ""
#         self._hp = 0

#     def setname(self, name):
#         self._name = name
    
#     def getname(self):
#         return self._name
    
#     def sethp(self, hp):
#         if 1 <= hp <= 100:
#             self._hp = hp
#         else:
#             print("hp 범위 초과!! hp를 다시 설정하세요.")
    
#     def gethp(self):
#         return self._hp
    
#     def exercise_day(self, exercise_time):
#         print(f"{exercise_time}시간 운동하다")
#         for i in range(exercise_time):
#             self._hp += 1

#     def alchole_day(self, alchole_count):
#         print(f"술을 {alchole_count}잔 마시다")
#         for i in range(alchole_count):
#             self._hp -= 1

#     def hp_info(self):
#         print(f"{Health.getname(self)} - hp: {Health.gethp(self)}")
#         print("=====================")

# p1 = Health()
# p1.setname("나몸짱")
# p1.sethp(95)

# p1.exercise_day(5)
# p1.alchole_day(2)
# p1.hp_info()

# p2 = Health()
# p2.setname("나약해")
# p2.sethp(11)

# p2.exercise_day(1)
# p2.alchole_day(12)
# p2.hp_info()

# getter, setter test
# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age

#     # Getter
#     @property
#     def name(self):
#         return self.__name
    
#     # Setter
#     @name.setter
#     def name(self, value):
#         self.__name = value
    
#     # Getter
#     @property
#     def age(self):
#         return self.__age
    
#     # Setter
#     @age.setter
#     def age(self, value):
#         self.__age = value
    
# person = Person("홍길동", 30)
# print(person.name)
# print(person.age)

# person.name = "최흥기"
# person.age = 32
# print(person.name)
# print(person.age)

# 실습 3(getter, setter).
# 건강상태 클래스

# class Health2:
#     def __init__(self, name, hp, exercise, alchole_drink):
#         self.__name = name
#         self.__hp = hp
#         self.__exercise = exercise
#         self.__alchole_drink = alchole_drink
    
#     # getter-name
#     # @property
#     def name(self):
#         return self.__name
    
#     # # setter-name
#     # @name.setter
#     def name(self, value):
#         self.__name = value
    
#     # getter-hp
#     @property
#     def hp(self):
#         return self.__hp
    
#     # setter-hp
#     @hp.setter
#     def hp(self, value):
#         if 1 <= value <= 100:
#             self.__hp = value
#         else:
#             print("1~100사이 값을 다시 입력하세요.")
    
#     def get_info(self):
#         print(f"{self.__exercise}시간 운동하다")
#         print(f"술을 {self.__alchole_drink}잔 마시다")
#         print(f"{self.__name} - hp: {self.__hp + self.__exercise - self.__alchole_drink}")
#         print("======================")

# p1 = Health2("나몸짱", 95, 5, 2)
# p1.get_info()

# p2 = Health2("나약해", 11, 1, 12)
# p2.get_info()

# 부모 클래스: 생성자 없음
# class Animal:
#     def speak(self):
#         print("동물이 소리를 냅니다.")

#     def move(self):
#         print("동물이 움직입니다.")
    
# # 자식 클래스
# # Animal 클래스를 상속
# class Dog(Animal):
#     def bark(self):
#         print("멍멍!")

# dog = Dog()
# dog.speak()
# dog.move()
# dog.bark()

# 부모 클래스: 생성자 있음
# class Animal:
#     def __init__(self, name):
#         self.name = name
    
#     def speak(self):
#         print(f"{self.name}가 소리를 냅니다.")

#     def move(self):
#         print(f"{self.name}가 움직입니다.")
    
# class Dog(Animal):
#     def __init__(self, name, sound):
#         super().__init__(name)
#         self.sound = sound

#     def bark(self):
#         print(f"{self.name}가 {self.sound} 짖습니다.")

# dog = Dog("백구", "멍멍")
# dog.speak()
# dog.move()
# dog.bark()

# 다중상속
# class Engine:
#     def __init__(self, horsepower):
#         self.horsepower = horsepower

# class Wheels:
#     def __init__(self, wheel_count):
#         self.wheel_count = wheel_count
    
# class Car(Engine, Wheels):
#     def __init__(self, horsepower, wheel_count):
#         Engine.__init__(self, horsepower)
#         Wheels.__init__(self, wheel_count)

#     def info(self):
#         print(f"이 자동차는 {self.horsepower} 마력 엔진과 {self.wheel_count}개의 바퀴를 가지고 있습니다.")

# car = Car(150, 4)
# car.info()
# print(Car.mro())

# 다형성 test
# class Parent:
#     def greet(self):
#         print("안녕하세요, 저는 부모 클래스입니다.")

# class Child(Parent):
#     def greet(self):
#         super().greet()
#         print("안녕하세요, 저는 자식 클래스입니다.")

# parent = Parent()
# child = Child()
# parent.greet()
# print()
# child.greet()


# 실습(상속과 오버라이딩).
# class Product:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
    
#     # 재고 업데이트 메서드
#     def update_quantity(self, amount):
#         self.quantity += amount
#         print(f"{self.name} 재고가 {amount}만큼 {'증가' if amount > 0 else '감소'}했습니다. 현재 재고: {self.quantity}")

#     def display_info(self):
#         print(f"상품명: {self.name}")
#         print(f"가격: {self.price}원")
#         print(f"재고: {self.quantity}개")

# class Electronic(Product):
#     def __init__(self, name, price, quantity, warranty_period = 12):
#         super().__init__(name, price, quantity)
#         self.warranty_period = warranty_period

#     def extend_warranty(self, month):
#         self.warranty_period += month
#         print(f"보증 기간이 {month}개월 연장되었습니다. 현재 보증 기간 : {self.warranty_period}개월")

#     def display_info(self):
#         super().display_info()
#         print(f"보증 기간 : {self.warranty_period}개월")
    
# class Food(Product):
#     def __init__(self, name, price, quantity, expiration_date):
#         super().__init__(name, price, quantity)
#         self.expiration_date = expiration_date

#     def is_expired(self, current_date):
#         if current_date > self.expiration_date:
#             print(f"{self.name}는 유통기한이 지났습니다.")
#             super().display_info()
#         else:
#             print(f"{self.name}는 유통기한이 지나지 않았습니다.")
#             super().display_info()

#     def display_info(self):
#         super().display_info()
#         print(f"유통기한 : {self.expiration_date}")
    
# product1 = Product("스마트 TV", 1500000, 5)
# product1.display_info()
# product1.update_quantity(3)
# product1.display_info()

# print()

# product2 = Electronic("스마트 TV", 1500000, 5, 24)
# product2.display_info()
# product2.extend_warranty(12)
# product2.display_info()

# print()

# product3 = Food("사과", 3000, 50, "2024-09-20")
# product3.display_info()
# product3.is_expired("2025-09-20")

# 추상클래스
# from abc import ABC, abstractmethod

# class PaymentSystem(ABC):
#     @abstractmethod
#     def authenticate(self):
#         pass

#     @abstractmethod
#     def process_payment(self, amount):
#         pass

#     def payment_summary(self, amount):
#         print(f"{amount} 원 결제가 완료되었습니다.")

# class CreditCard(PaymentSystem):
#     def authenticate(self):
#         print("신용카드 인증 완료.")

#     def process_payment(self, amount):
#         print(f"신용카드로 {amount} 원을 결제합니다.")

# print("신용카드 결제: ")
# credit_card = CreditCard()
# credit_card.authenticate()
# credit_card.process_payment(50000)
# credit_card.payment_summary(50000)

# 클래스 메서드
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     @classmethod
#     def from_birth_year(cls, name, birty_year):
#         age = 2024 - birty_year
#         return cls(name, age)
    
# # 클래스 메서드를 통해 객체 생성
# p = Person.from_birth_year("홍길동", 1990)
# print(p.name, p.age)

# 정적 메서드
# class MathUtils:
#     @staticmethod
#     def add(a, b):
#         return a + b
    
#     @staticmethod
#     def multiply(a, b):
#         return a * b
    
# print(MathUtils.add(10, 20))
# print(MathUtils.multiply(10, 20))


# 종합 클래스 실습
from abc import ABC, abstractmethod

electricity_usage = [
    {'date': '2024-11-01', 'usage': 12.5},
    {'date': '2024-11-02', 'usage': 15.3},
    {'date': '2024-11-03', 'usage': 10.8},
    {'date': '2024-11-04', 'usage': 14.2},
    {'date': '2024-11-05', 'usage': 13.6}
]

class ElectricityData(ABC):
    def __init__(self, usage_data, total_usage=0):
        self._usage_data = usage_data
        self._total_usage = total_usage
    
    # getter-usage_data
    @property
    def using_data(self):
        return self._usage_data
    
    # setter-usage_data
    @using_data.setter
    def using_data(self, usage):
        self._usage_data += usage # usage는 날짜와 사용량을 포함한 딕셔너리 형태

    # getter-total_data
    @property
    def total_using_data(self):
        return self._total_usage
    
    # setter-total_data
    @total_using_data.setter
    def total_using_data(self, total):
        self._total_usage += total

    @abstractmethod
    def calculate_total_usage(self, electricity_usage):
        pass

    @abstractmethod
    def get_usage_on_date(self, date):
        pass

    def add_usage(self, date, usage):
        self._usage_data.append({'date': date, 'usage': usage})
        # dict1 = dict(date= date, usage= usage)
        # self._usage_data.append(dict1)

    def remove_usage(self, date):
        self._usage_data = [i for i in self._usage_data if i["date"] != date]
        # for i in self._usage_data:
        #     if i["date"] == date:
        #         self._usage_data.remove(i)
        #         break

class HomeElectricityData(ElectricityData):
    def calculate_total_usage(self):
        self._total_usage = sum([i['usage'] for i in self._usage_data])

    def get_usage_on_date(self, date):
        usage = [i["usage"] for i in self._usage_data if i["date"] == date]
        print(f"{date}일의 사용량: {usage[0]}")

    @classmethod
    def filter_data(cls, usage_data, date1, date2):
        range_date = filter(lambda x: date1 < x["date"] < date2 , usage_data)
        return cls(list(range_date))

    @staticmethod
    def max_usage(usage):
        # return max(usage, key=lambda x: x["usage"])
        max_data = max([i["usage"] for i in usage])
        for i in usage:
            if i["usage"] == max_data:
                return i

home1 = HomeElectricityData(electricity_usage)

home1.calculate_total_usage()
print(f"총 전력 사용량: {home1.total_using_data:.1f}")
home1.get_usage_on_date("2024-11-04")
home1.add_usage("2024-11-06", 40.3)
home1.remove_usage("2024-11-01")
home1.calculate_total_usage()
print(f"날짜 추가 후 총 사용량: {home1.total_using_data:.1f}")
filter_data = HomeElectricityData.filter_data(home1.using_data, "2024-11-01", "2024-11-06")
print("특정 날짜 범위 내 사용량: ", filter_data.using_data)
print("가장 높은 사용량: ", HomeElectricityData.max_usage(home1.using_data))

## 위 코드와 비교
## 리더 코드
#실습. 클래스 종합 프로그래밍

# from abc import ABC, abstractmethod

# electricity_usage = [
#     {"date": "2024-11-01", "usage": 12.5},
#     {"date": "2024-11-02", "usage": 15.3},
#     {"date": "2024-11-03", "usage": 10.8},
#     {"date": "2024-11-04", "usage": 14.2},
#     {"date": "2024-11-05", "usage": 13.6}
# ]

# #추상클래스
# class EletrictiyData:
#     def __init__(self, usage_data, total_usage = 0):
#         self._usage_data = usage_data
#         self._total_usage = total_usage

#     @property
#     def usage_data(self):
#         return self._usage_data
    
#     @usage_data.setter
#     def usage_data(self, new_data):
#         self._usage_data = new_data

#     @property
#     def total_usage(self):
#         return self._total_usage
    
#     @total_usage.setter
#     def total_usage(self, new_total):
#         self._total_usage = new_total

#     #추상메서드
#     @abstractmethod
#     def calculate_total_usege(self):
#         pass

#     @abstractmethod
#     def get_usage_on_date(self, date):
#         pass

#     #메서드
#     def add_usage(self, date, usage):
#         self._usage_data.append({"date": date, "usage": usage})

#     def remove_usage(self, date):
#         self._usage_data = [ i for i in self._usage_data if i['date'] != date ]


# # 자식클래스
# class HomeElectricityData(EletrictiyData):
#     #추상메서드 구현
#     def calculate_total_usege(self):
#         self._total_usage = sum( i["usage"] for i in self._usage_data )

#     def get_usage_on_date(self, date):
#         for i in self._usage_data:
#             if i["date"] == date:
#                 return i["usage"]
            
#     # 클래스 메서드
#     @classmethod
#     def filter_date(cls, usage_data, start_date, end_date):
#         filter_data = [ i for i in usage_data if start_date <= i['date'] <= end_date ]
#         return cls(filter_data)
    
#     # 정적메서드
#     @staticmethod
#     def max_usage(usage_data):
#         return max(usage_data, key=lambda x: x["usage"])
    

# home = HomeElectricityData(electricity_usage)
# home.calculate_total_usege()
# print("총 전력 사용량: ",home.total_usage)
# print("특정날짜 :", home.get_usage_on_date("2024-11-03"))
# home.add_usage("2025-04-07", 10.0)
# home.remove_usage("2024-11-01")
# print(home.usage_data)
# print()
# filter_data =  HomeElectricityData.filter_date(home.usage_data, "2024-11-04", "2025-04-07")
# print("필터 :", filter_data.usage_data)
# max_data = HomeElectricityData.max_usage(filter_data.usage_data)
# print("최대사용량"  ,max_data)

# print(max(electricity_usage, key=lambda x :x["usage"]))