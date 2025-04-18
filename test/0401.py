""" def gugudan(dan, end):
    print(f'{dan}단')
    for i in range(1, end):
        print(f'{dan} x {i} = {dan * i}')


gugudan(8, 15) """


# def say_hello():
#     print("Hello, World")


# say_hello()


# def say_hello(year, name):
#     age = 2025 - year
#     print(f'{name}님의 나이는 {age}살 입니다.')


# say_hello(1994, "최흥기")

# # 결과값이 있는 함수
# def calculate_sum(num1, num2):
#     total = 0
#     for i in range(num1, num2 + 1):
#         total += i

#     return total


# print(calculate_sum(1, 10))

# # 리스트 반환
# def fruits():
#     return ["apple", "banana", "peach"]


# print(fruits())

# def student():
#     return {
#         "name": "홍길동",
#         "age": 20,
#         "major": "컴퓨터공학"
#     }


# result = student()
# print(result["name"])

# #실습 1.
# def mul_sum(num1, num2):
#     if num1 == num2:
#         return num1 * num2
#     else:
#         return num1 + num2


# result = mul_sum(2, 3)
# print(result)

# #실습 2.
# def transport_price(price):
#     if price < 20000:
#         print(f'상품 가격: {price + 2500}')
#     else:
#         print(f'상품 가격: {price}')


# transport_price(30000)

# def times(num):
#     return [i * 3 for i in num]


# arr = [1, 2, 3, 4, 5]
# newArr = times(arr)
# print(newArr)

# 과제. 자판기 프로그램

def check_machine(vending_machine):
    print(f'남은 음료수: {vending_machine}')


def is_drink(drink, vending_machine):
    if drink in vending_machine:
        print(f'{drink}가 자판기에 {vending_machine.count(drink)}개 있습니다.')
    else:
        print("음료 없음")


def add_drink(new_drink, vending_machine):
    vending_machine.append(new_drink)
    print("추가완료")
    print(f'남은 음료수: {sorted(vending_machine)}')


def remove_drink(del_drink, vending_machine):
    if del_drink in vending_machine:
        vending_machine.remove(del_drink)
        print("삭제완료")
        print(f'남은 음료수: {sorted(vending_machine)}')
    else:
        print(f'{del_drink}는 지금 없네요.')


vending_machine = ['게토레이', '게토레이', '레쓰비', '레쓰비', '생수', '생수', '생수', '이프로']

# 함수
# def say_hello():
#     print("Hello world")

# say_hello()

# 매개변수가 있는 함수
# def say_hello(year, name):
#     age = 2025 - year
#     print(f"{name}님의 나이는 {age} 입니다.")

# say_hello(2000, "민지")
# say_hello(2001, "혜린")

# # 구구단 함수
# def gugudan(dan, end):
#     print(f"{dan}단")
#     for i in range(1, end + 1):
#         print(f"{dan} x {i} = {dan * i}")

# gugudan(7, 10)

# # 결과값이 있는 함수
# def calc_sum(num1, num2):
#     total = 0
#     for i in range(num1, num2 + 1):
#         total += i
#     return total

# print(calc_sum(1, 10))

# # 리스트반환
# def fruits():
#     # 코드....
#     return ["apple", "banana", "peach"]

# lists = fruits()
# print(lists)

# # 딕셔너리 반환
# def students():
#     # 코드...
#     return {
#         "name": "홍길동",
#         "age": 20,
#         "major": "컴퓨터공학"
#     }

# dicts = students()
# print(dicts)


# 실습1
# def multi_or_add(num1, num2):
#     if num1 == num2:
#         return num1 * num2
#     else:
#         return num1 + num2

# result1 = multi_or_add(3, 3)
# print(result1)
# result2 = multi_or_add(6, 5)
# print(result2)

# #실습2
# def calc_price(price):
#     fee = 2500
#     if price < 20000:
#         total = price + fee
#     else:
#         total = price
#     return total

# result1 = calc_price(15000)
# print(result1)
# result2 = calc_price(25000)
# print(result2)


# #함수 매개변수로 리스트 전달
# def times(nums):
#     return [ i ** 2 for i in nums]

# number = [2,3,4,5]
# print(times(number))

# 자판기 실습

# 음료수가 있는지 확인하는 함수
# def is_drink(drink):
#     return drink in vending_machine

# # 음료수를 제거하는 함수
# def remove_drink(drink, user):
#     if user == "1" or user == "소비자":
#         vending_machine.remove(drink)
#         print(f"{drink}가 뽑아져나왔습니다.")
#     else:
#         vending_machine.remove(drink)
#         print(f"{drink}가 제거되었습니다.")


# # 남은 음료수를 확인하는 함수
# def check_machine():
#     print("남은음료수는 : ", vending_machine)

# # 음료수를 추가하는 참수
# def add_drink(drink):
#     vending_machine.append(drink)
#     print("추가완료")

"""
vending_machine = ["게토레이", "게토레이", "레쓰비", "레쓰비", "생수", "생수", "생수", "이프로"]

while True:
    user_input = input("사용자를 선택하세요. (1.소비자, 2.주인, 3.종료): ")

    if user_input == "1" or user_input == "소비자":
        drink = input("마시고 싶은 음료는? ")

        if is_drink(drink):
            remove_drink(drink, user_input)
        else:
            print("음료수가 존재하지 않습니다.")
        check_machine()

    elif user_input == "2" or user_input == "주인":
        move = input("할일을 선택하세요. (1. 추가, 2. 삭제)")

        if move == "1" or move == "추가":
            drink = input("추가할 음료수는? ")
            add_drink(drink)
        elif move == "2" or move == "삭제":
            drink = input("삭제할 음료수는? ")
            if is_drink(drink):
                remove_drink(drink, user_input)
            else:
                print(f"{drink}는 존재하지 않습니다.")
        else:
            print("값을 잘못입력하셨습니다다")

        check_machine()

    elif user_input == "3" or user_input == "종료":
        print("자판기 프로그램을 종료합니다")
        break
    else:
        print("값을 잘못입력하셨습니다다") """

# # 전역변수

# quantity = 10


# def get_price(price):
#     price = price * quantity
#     return price


# print(f'{quantity}개의 가격은 {get_price(20000)}원 입니다.')

# # 지역변수


# def oneup():
#     x = 0
#     x = x + 1
#     return x


# print(oneup())

# # global 키워드

# x = 0


# def oneup():
#     global x
#     x += 1
#     return x

# print(oneup())
# print(oneup())
# print(oneup())
# print(oneup())

# def pr_str(txt="안녕하세요", count=1):
#     for _ in range(count):
#         print(txt)


# pr_str()
# pr_str("반갑습니다")
# pr_str("어서오세요", 3)

# # 함수 호출 키워드
# def intro(name, age, city):
#     print(f'{name}의 나이는 {age}이고 {city}에 삽니다.')


# intro("홍길동", 23, "서울 은평구")
# intro(age=25, city="광주광역시", name="최흥기")
# intro(city="광주광역시", 25, name="최흥기")

# # 가변 매개변수
# def calc_avg(*args):
#     print(args)
#     total = 0
#     for i in args:
#         total += i
#     return total / len(args)


# print(calc_avg(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# def text_def(a, b, *args):
#     print("a", a)
#     print("b", b)
#     print("args", args)


# text_def(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# def intro(**kwargs):
#     for key, value in kwargs.items():
#         print(f'{key}: {value}')


# intro(name="최흥기", age=32, city="광주광역시", gender="남")

# 내장함수
# # 절대값 - abs(정수)
# def myabs(x):
#     if x < 0:
#         return -x
#     else:
#         return x


# print(myabs(-10))
# print(abs(-20))

# 거듭제곱
# print(pow(3, 4))


# def mypow(x, y):
#     num = 1
#     for i in range(y):
#         print(f'i = {i}, {num*x} = {num}x{x}')
#         num = num * x
#     return num


# print(mypow(3, 4))

# # map()
# def square(x):
#     return x ** 3


# numbers = [2, 4, 6, 8]
# squared = map(square, numbers)
# print(list(squared))

# # filter()
# def even_number(x):
#     result = x % 2 == 0
#     return result


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list(filter(even_number, numbers)))

# def mul_num(x, y):
#     for i in range(1, y + 1):
#         print(x * i, end=" ")
#     print()
#     print(f'{x}의 배수의 개수: {y}')

# mul_num(3, 10)

# # 한꺼번에 여러 개 반환
# def get_return():
#     arr = ["사과", "바나나", "망고"]
#     dic = {
#         "name": "홍길동"
#         "age": 20
#     }
#     num = 30
#     return arr, dic, num


# arrs, dics, nums = get_return()
# print(arrs)
# print(dics)
# print(nums)

# 실습4


def counts_num(num):
    lists = [i for i in range(1, 31) if i % num == 0]
    count = len(lists)
    return lists, count


num = 4
lists, count = counts_num(num)
print(f'{num}의 배수: {lists}')
print(f'{num}의 갯수: {count}')
