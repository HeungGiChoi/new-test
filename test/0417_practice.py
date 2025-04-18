# def str_func(strlist):
#     len_li = [len(i) for i in strlist]
#     return len_li

# li_str = ['abdc', 'maple', 'avengerse', 'rollipop']
# print(str_func(li_str))
# file = open("new_test.txt", 'w')
# file.write("녕안녕안녕안")
# file.close

# with open("new_test.txt", 'a') as file:
#     file.write("\n이바이바이바이바이")
#     encoding = "utf-8"

# lines = ["첫 번째 줄\n", "두 번째 줄\n", "세 번째 줄\n"]

# with open("testlist.txt", 'w') as file:
#     file.writelines(lines)

# with open("user_input.txt", 'w') as file:
#     while True:
#         line = input("파일에 저장할 내용 입력: ")
#         if line == "종료":
#             print("입력 종료")
#             break
#         file.write(line + "\n")
# print("사용자 입력 종료")

# with open("user_input.txt", "r") as file:
#     content = file.read()
#     print("파일 내용 : ")
#     print(content)

# with open("user_input.txt", 'r') as file:
#     print(file.readline())
#     print(file.readline())
#     print(file.readline())

# with open("user_input.txt", 'r') as file:
#     lines = file.readlines()
#     print(lines)


# with open("user_input.txt", 'r') as file:
#     line = file.readline()
#     while line:
#         print(line.strip())
#         line = file.readline()

with open("user_input.txt", 'r') as file:
    lines = file.readlines()
    for idx, line in enumerate(lines):
        print(f"{idx + 1}번째 줄: {line.strip()}")