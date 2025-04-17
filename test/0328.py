# 조건문

# if : 조건문:
#    조건식이 참이라면 실행
""" 
if True:
    print("참 입니다.")

if False:
    print("참 이 아닙니다.") """

""" age = 15

if age > 14:
    print("15살 이상입니다.")

if age >= 15:
    print("15살 이상이 맞습니다.")
 """
""" 
a = input("비밀번호를 입력하세요: ")

if a == "abc123":
    print("비밀번호가 맞습니다.")

b = int(input("숫자를 입력하세요: "))

if b % 2 == 0:
    print("짝수입니다.") """
""" 
age = 15

if age >= 20:
    print("성인입니다.")
else:
    print("미성년자입니다.")

print(f'나이는 {age}세 입니다.') """
""" 
a = input("비밀번호를 입력하세요: ")

if a == "abc123":
    print("비밀번호가 맞습니다.")
else:
    print("비밀번호가 틀렸습니다.")

b = int(input("숫자를 입력하세요: "))

if b % 2 == 0:
    print("짝수입니다.")
else:
    print("홀수입니다.") """

""" score = int(input("점수를 입력하세요: "))

if score < 60:
    print("학점: F")
elif 60 <= score < 70:
    print("학점: D")
elif 70 <= score < 80:
    print("학점: C")
elif 80 <= score < 90:
    print("학점: B")
elif score >= 90:
    print("학점: A")
 """
""" 
age = int(input("나이를 숫자로 입력해주세요: "))
cash_card = input("결제방법을 입력해주세요 (현금 또는 카드): ")

if age < 8:
    print(f'{age}세의 요금은 무료입니다.')
elif 8 <= age < 14:
    print(f'{age}세의 요금은 450원입니다.')
elif 14 <= age < 20:
    if cash_card == "카드":
        print(f'{age}세의 {cash_card} 요금은 720원입니다.')
    elif cash_card == "현금":
        print(f'{age}세의 {cash_card} 요금은 1,000원입니다.')
elif 20 <= age < 75:
    if cash_card == "카드":
        print(f'{age}세의 {cash_card} 요금은 1,200원입니다.')
    elif cash_card == "현금":
        print(f'{age}세의 {cash_card} 요금은 1,300원입니다.')
elif 75 <= age:
    print(f'{age}세의 요금은 무료입니다.') """
""" 
age = int(input("나이를 입력하세요: "))
message = "성인입니다." if age > 19 else "미성년자입니다."
print(message) """
""" 
fruit = input("과일을 입력하세요.")

if fruit in ["사과", "바나나", "체리"]:
    print("이 과일은 포함되어 있음.")
else:
    print("존재하지 않는 과일") """
""" 
fruit_cal = {'apple': 95, 'banana': 105, 'cherry': 50}
fruit = input("과일을 영문으로 입력하세요. :")

if fruit in fruit_cal:
    print(f'{fruit}의 칼로리는 {fruit_cal.get(fruit)}kcal입니다.')
else:
    print("포함되지 않은 과일") """

""" i = 1
total = 0
while i <= 10:
    total += i
    i += 1

print(f'1부터 10까지의 합은 {total}입니다.')
 """
""" 
num = input("양수를 입력하세요.")

sum = 1
total = 0

while True:
    if not num.isdigit():
        num = input("양수를 입력하세요.")
        continue

    number = int(num)
    total += sum
    sum += 1

    if num == 0:
        num = input("다시 입력하세요.(양수)")
        continue
    elif num < 0:
        num = input("양수를 입력하세요.")
        continue
    elif sum == number:
        print(f'1부터 {num}까지의 합은 {total}입니다.')
        num = input("계속하시겠습니까?")
        if num == "종료":
            print("프로그램을 종료합니다.")
            break
        elif num == "네":
            sum = 1
            total = 0
            num = input("양수를 입력하세요.")
            continue
print("프로그램 종료") """

# 실습 1.
""" num1 = int(input("몇단을 출력할까요?: "))
num2 = 0
for i in range(1, 10):
    num2 = num1 * i
    print(f'{num1} x {i} = {num2}')

print("구구단 종료") """

# 실습 2.
""" num3 = int(input("어디까지 계산할까요?: "))
sum = 0

for i in range(1, num3+1):
    if i % 2 == 1:
        sum += i

print(f'1부터 {num3}까지의 홀수의 합: {sum}')
 """
# 실습 3.
""" students = {'학생1': [83, 92, 88], '학생2': [90, 79, 86], '학생3': [88, 86, 94]}
avr = 0

for key, value in students.items():
    avr = value
    avr = (avr[0] + avr[1] + avr[2]) // len(avr)
    print(f'{key}의 평균값은 {avr} 입니다.') """

""" matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

total = 0

for row in matrix:
    for element in row:
        total += element

print(total)

for i in range(0, 3):
    for j in range(0, 3):
        print(matrix[i][j]) """

""" print("구구단 출력")

for i in range(2, 10):
    print("")
    print(f'[{i}단]')
    for j in range(1, 10):
        print(f'{i} x {j} = {i * j}') """

# 과제. 자판기 프로그램

vending_machine = ['게토레이', '게토레이', '레쓰비', '레쓰비', '생수', '생수', '생수', '이프로']
print(f'남은 음료수: {vending_machine}')

while True:
    user = input("사용자 종류를 입력하세요: \n1. 소비자\n2. 주인\n")
    if user != "소비자" and user != "주인":
        print("잘못된 값")
        continue

    if user == "소비자":
        drink = input("마시고 싶은 음료는?: ")
        if drink in vending_machine:
            print(f'{drink} 드릴께요.')
            vending_machine.remove(drink)
            print(f'남은 음료수: {vending_machine}')
        else:
            print("음료 없음")

    if user == "주인":
        print("할 일 선택: \n1. 추가\n2. 삭제")
        func = input()
        if func != "추가" and func != "삭제":
            print("잘못된 값")

        if func == "추가":
            print(f'남은 음료수: {vending_machine}')

            new_drink = input("추가할 음료수는?: ")
            vending_machine.append(new_drink)
            print("추가완료")
            print(f'남은 음료수: {sorted(vending_machine)}')
        elif func == "삭제":
            del_drink = input("삭제할 음료수는?: ")
            if del_drink in vending_machine:
                vending_machine.remove(del_drink)
                print("삭제완료")
                print(f'남은 음료수: {sorted(vending_machine)}')
            else:
                print(f'{del_drink}는 지금 없네요.')
