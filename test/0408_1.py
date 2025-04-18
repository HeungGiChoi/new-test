# 파일 입출력

# 파일 쓰기
# with open("test_35.txt", 'w', encoding="utf-8") as file:
#     file.write('안녕하세요.\n')
#     file.write("파이썬 파일 쓰기 연습\n")

# 내용 추가
# with open("test.txt", "a", encoding="utf-8") as file:
#     file.write("내용추가\n")
#     file.write("12345") # 숫자는 문자열 형태로 작성

# 여러개를 한번에 추가
# lines = ['첫번째\n', '두번째\n', '세번째\n', '네번째\n']
# with open("list.txt", "w", encoding="utf-8") as f:
#     f.writelines(lines)

# 사용자로부터 내용 입력 받기
# with open("user.txt", "w", encoding="utf-8") as f:
#     while True:
#         line = input("파일에 넣을 문자열입력(종료하면 '종료'입력)")
#         if line == '종료':
#             print("입력을 종료합니다.")
#             break
#         f.write(line + "\n")

# 파일 읽기
# with open("user.txt", "r", encoding="utf-8") as file:
#     print(file.read())

# with open("user.txt", "r", encoding="utf-8") as file:
#     print(file.readline())
#     print(file.readline())

# with open("user.txt", "r", encoding="utf-8") as file:
#     print(file.readlines())


# 공백제거
# with open("user.txt", "r", encoding="utf-8") as file:
#     line = file.readline()
#     while line:
#         print(line.strip()) # 양쪽공백제거
#         line = file.readline()

# eumerate() : 리스트를 튜플형태로 반환, 반환값이 두개(인덱스, 값)
# with open("user.txt", "r", encoding="utf-8") as file:
#     lines = file.readlines()

#     for idx, value in enumerate(lines):
#         print(f"{idx} 인덱스 값은 : {value.strip()}입니다.")

# 바이너리 파일
# with open("ramen.png", "rb") as file:
#     # data = file.read()
#     # print(f"{len(data)} 바이트")

#     header = file.read(10)
#     print(header)

# def identity_file(file_path):
#     with open(file_path, "rb") as file:
#         header = file.read(4) # 4바이트가 확장자의 매직넘버
#         print(header)
#         if header[:2] == b'\x89PNG': #png 첫 4바이트가 89 50 4e 47
#             return "png"
#         else:
#             return "unknown"
    
# identity_file("ramen.png")

# # 바이너리 파일 쓰기
# with open("ramen.png", "rb") as file:
#     data = file.read()

# with open("ramen_copy.png", "wb") as file:
#     file.write(data)

# 예외처리

# try:
#     x = int(input("숫자를 입력하세요: "))
#     result = 10 / x
# except (ZeroDivisionError, ValueError) as e: # 여러 에러메시지 한번에 처리 가능
#     print("예외메세지: ", e)
# else:
#     print(f"result: {result}")
# finally:
#     print("무조건 실행된 부분")

# x = int(input("숫자를 입력하세요: "))
# result = 10 / x

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("0으로 나눌 수 없습니다.")
    return a / b

try:
    result = divide(10, 0)
except ZeroDivisionError as e:
    print(e)
else:
    with open("result.txt", 'w', encoding="utf-8") as file:
        file.write(f"{result}")
