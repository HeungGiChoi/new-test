# 추상화 클래스

# from abc import ABC, abstractmethod

# # 추상클래스 정의
# class PaymentSystem(ABC):

#     # 추상 메서드
#     @abstractmethod
#     def authenticate(self):
#         pass

#     @abstractmethod
#     def process_payment(self, amount):
#         pass

#     def payment_summary(self, amount):
#         print(f"{amount} 원 결제가 완료되었습니다.")

# class KakaoPay(PaymentSystem):
#     def authenticate(self):
#         print("신용카드 인증 완료.")

#     def process_payment(self, amount):
#         print(f"신용카드로 {amount} 원을 결제합니다.")

# print("신용카드 결제: ")
# credit_card = KakaoPay()
# credit_card.authenticate()
# credit_card.process_payment(2000)
# credit_card.payment_summary(2000)

# 클래스 메서드
# class Converter:
#     conversion_rate = 1.60934

#     @classmethod
#     def miles_to_kilometer(cls, mile):
#         return mile * cls.conversion_rate
    
# print()
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     @classmethod
#     def from_birth_year(cls, name, birth_year):
#         age = 2025 - birth_year + 1
#         return cls(name, age)
    
# p1 = Person.from_birth_year("홍길동", 2000)
# print(p1.name, p1.age)

# 클래스변수를 사용
# class Counter:
#     count = 0

#     @classmethod
#     def increment(cls):
#         cls.count += 1

#     @classmethod
#     def get_count(cls):
#         return cls.count
    
# print(Counter.get_count())
# Counter.increment()
# print(Counter.get_count())

# # 정적메서드
# class MathUtils:
#     @staticmethod
#     def add(a, b):
#         return a + b
    
#     @staticmethod
#     def minus(a, b):
#         return a - b
    
# print(MathUtils.add(20, 40))
# print(MathUtils.minus(40, 20))

# 실습 3. 종합 프로그래밍
# from abc import ABC, abstractmethod

# electricity_usage = [
#     {"date": "2024-11-01", "usage": 12.5},
#     {"date": "2024-11-02", "usage": 15.3},
#     {"date": "2024-11-03", "usage": 10.8},
#     {"date": "2024-11-04", "usage": 14.2},
#     {"date": "2024-11-05", "usage": 13.6},
# ]

# # 추상 클래스
# class ElectricityData:
#     def __init__(self, usage_data, total_usage):
#         self.__usage_data = usage_data
#         self.__total_usage = total_usage
    
#     @property
#     def use_data(self):
#         return self.__usage_data
    
#     @use_data.setter
#     def use_data_set1(self, ):
#         pass

#     @property
#     def total_usage_data(self):
#         pass
    
#     @total_usage_data.setter
#     def total_use(self, usage):
#         self.__total_usage += usage
#         return self.__total_usage

#     @abstractmethod
#     def calculate_total_usage(self):
#         pass

#     @abstractmethod
#     def get_usage_on_date(self, date):
#         pass

#     def add_usage(self, date, usage):
#         self.__usage_data = [{"date": date, "usage": usage}]
#         ElectricityData.append(self.__usage_data)

#     def remove_usage(self, date): # for 문gkrh items() 사용해서 날짜 뽑아낸 다음에 if 써서 같은 날짜 찾으면 그 딕셔너리 삭제
#         pass

# # 자식 클래스
# class HomeElectricityData(ElectricityData):
#     def calculate_total_usage(self):
#         pass

#     def get_usage_on_date(self, date):
#         return super().get_usage_on_date(date)
    
#     # 클래스 메서드
#     @classmethod
#     def filter_date(cls, self, date):
#         pass

#     # 정적 메서드
#     @staticmethod
#     def max_usage_data(electricityData):
#         pass

from abc import ABC, abstractmethod

# 초기 데이터
electricity_usage = [
    {"date": "2024-11-01", "usage": 12.5},
    {"date": "2024-11-02", "usage": 15.3},
    {"date": "2024-11-03", "usage": 10.8},
    {"date": "2024-11-04", "usage": 14.2},
    {"date": "2024-11-05", "usage": 13.6}
]

# 추상클래스
class ElectricityData(ABC):
    def __init__(self, usage_data):
        self._usage_data = usage_data
        self._total_usage = self.calculate_total_usage()

    @property
    def usage_data(self):
        return self._usage_data

    @usage_data.setter
    def usage_data(self, new_data):
        self._usage_data = new_data
        self._total_usage = self.calculate_total_usage()

    @property
    def total_usage(self):
        return self._total_usage

    @total_usage.setter
    def total_usage(self, value):
        self._total_usage = value

    @abstractmethod
    def calculate_total_usage(self):
        pass

    @abstractmethod
    def get_usage_on_date(self, date):
        pass

    def add_usage(self, date, usage):
        self._usage_data.append({"date": date, "usage": usage})
        self._total_usage = self.calculate_total_usage()

    def remove_usage(self, date):
        self._usage_data = [item for item in self._usage_data if item["date"] != date]
        self._total_usage = self.calculate_total_usage()

# 자식 클래스
class HomeElectricityData(ElectricityData):
    def calculate_total_usage(self):
        return sum(item["usage"] for item in self._usage_data)

    def get_usage_on_date(self, date):
        for item in self._usage_data:
            if item["date"] == date:
                return item["usage"]
        return None

    def get_usage_in_range(self, start_date, end_date):
        return [
            item for item in self.usage_data
            if start_date <= item["date"] <= end_date
        ]

    def get_max_usage(self):
        return max(self.usage_data, key=lambda x: x["usage"])

home_data = HomeElectricityData(electricity_usage)
print("총 전력 사용량:", round(home_data.total_usage, 1))
print("2024-11-03의 사용량:", home_data.get_usage_on_date("2024-11-03"))

home_data.add_usage("2024-11-06", 16.4)
print("2024-11-06 추가 후 총 전력 사용량:", round(home_data.total_usage, 1))

usage_in_range = home_data.get_usage_in_range("2024-11-02", "2024-11-04")
print("특정 날짜 범위 내 사용량:", usage_in_range)

max_usage = home_data.get_max_usage()
print("가장 높은 사용량:", max_usage)

