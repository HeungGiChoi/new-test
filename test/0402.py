# # 재귀함수
# def sos(i):
#     print("help me!!")
#     if i == 1:  # 종료조건
#         return ""
#     else:
#         return sos(i - 1)


# sos(10)

# # 팩토리얼


# def factorial(n):
#     print("n의 값 ", n)
#     if n == 1:  # 종료조건
#         return 1
#     else:
#         return n * factorial(n - 1)


# print(factorial(5))

# # 실습-피보나치 수열.
# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)

# print(fibonacci(6))

# 람다식
# # 일반 함수
# def add(x, y):
#     return x + y


# print(add(3, 4))

# # 람다함수

# add = lambda x, y: x + y
# print(add(3, 4))

# # 매개변수가 1개인 람다 함수

# oneup = lambda x: x + 1
# print(oneup(1))
# print((lambda x: x+1)(1))
# print((lambda x:x+1)(2))

# squared = lambda x: x ** 2
# print(squared(2))

# print(square(4))
# print((lambda x: x**2)(4))

# 람다함수를 매개변수로 전달
# def call_10(func):
#     for _ in range(10):
#         func()

# hello2 = lambda : print("안녕하세요.")
# call_10(hello2)

# # map() 람다 이용
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# def square(x):
#     return x ** 2
# print(list(map(square, numbers)))
# print(list(map(lambda x: x ** 2, numbers)))

# # 필터 람다 이용
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# def even_number(x):
#     return x % 2 == 0
# print(list(filter(even_number, numbers)))
# print(list(filter(lambda x: x % 2 == 0, numbers)))

# lambda 실습

# def counts_num(num):
#     lists = [i for i in range(1, 31) if i % num == 0]
#     count = len(lists)
# #     return lists, count
# num = 4

# lists = list(filter(lambda x: x % num == 0, range(1, 31)))

# print(f'{num}의 배수: {lists}')
# print(f'{num}의 갯수: {len(lists)}')

# 실습 6.
# weather_data = [ 
#     ["2024-11-20", "서울", 15.2, 0.0],
#     ["2024-11-20", "부산", 18.4, 0.0],
#     ["2024-11-21", "서울", 10.5, 2.3],
#     ["2024-11-21", "부산", 14.6, 1.2],
#     ["2024-11-22", "서울", 8.3, 0.0],
#     ["2024-11-22", "부산", 12.0, 0.0]
#     ]
# 함수화 해보기
# 기능들을 함수화 하고
# 함수화 된 기능들을 호출하는 main 함수
# 그리고 그 main 함수를 호출

# while True:
#     print("[날씨 데이터 분석 프로그램]")
#     print("1. 평균 기온 계산\n2. 최고/최저 기온 찾기\n3. 강수량 분석\n4. 날씨 데이터 추가\n5. 전체 데이터 출력\n6. 종료")
#     func_input = input("원하는 기능의 번호를 입력하세요: ")

#     if func_input == "1" or func_input == "평균 기온 계산":
#         city = input("도시 이름을 입력하세요: ")
#         temp_data = [data[2] for data in weather_data if data[1]==city]
#         #city_data = filter(lambda x: x[1]==city, weather_data)
#         #temp_data = list(map(lambda x: x[2], city_data))
#         avg_temp = sum(temp_data) / len(temp_data)
#         print(f'{city}의 평균 기온: {avg_temp:.2f}C')
#     elif func_input == "2" or func_input == "최고/최저 기온 찾기":
#         city = input("도시 이름을 입력하세요: ")
#         city_data = filter(lambda x: x[1]==city, weather_data)
#         temp_data = list(map(lambda x: x[2], city_data))
#         print(f'{city}의 최고 기온: {max(temp_data)}C, 최저 기온: {min(temp_data)}C')
#     elif func_input == "3" or func_input == "강수량 분석":
#         city = input("도시 이름을 입력하세요: ")
#         city_data = filter(lambda x: x[1]==city, weather_data)
#         rain_day_data = list(filter(lambda x: x[3] != 0.0, city_data))
#         rain_data = list(map(lambda x: x[3], rain_day_data))
#         sum_rain = sum(rain_data)
#         print(f'{city}의 총 강수량: {sum_rain}mm')
#         print(f'{city}의 강수량이 있었던 날: {rain_day_data[0][0][-2:]}일')
#     elif func_input == "4" or func_input == "날씨 데이터 추가":
#         day_input = input("날짜를 입력하세요 (YYYY-MM-DD): ")
#         city_input = input("도시를 입력하세요: ")
#         avg_temp_input = float(input("평균 기온을 입력하세요 (℃): "))
#         rain_data_input = float(input("강수량을 입력하세요 (mm): "))
#         new_weather_data = [day_input, city_input, avg_temp_input, rain_data_input]
#         weather_data.append(new_weather_data)
#         print(f'{city_input}의 날씨데이터가 추가되었습니다.')
#     elif func_input == "5" or func_input == "전체 데이터 출력":
#         print("\n현재 저장된 날씨 데이터:")
#         for data in weather_data:
#             print(f'날짜: {data[0]}, 도시: {data[1]}, 평균 기온: {data[2]}℃, 강수량: {data[3]}mm')
#     elif func_input == "6" or func_input == "종료":
#         print("프로그램 종료")
#         break
#     else:
#         print("1~6까지 번호를 입력하세요.")