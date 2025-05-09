## 배열의 유사도
# def solution(s1, s2):
#     count = 0
#     for i in s1:
#         for j in s2:
#             if i == j:
#                 count += 1
#     return count

# s1 = ["a", "b", "c"]
# s2 = ["com", "b", "d", "p", "c"]
# print(solution(s1, s2))

## 문자열안에 문자열
# def solution(str1, str2):
#     for i in range(len(str1)):
#         if str1[i] == str2[0]:
#             if str1[i:i+len(str2)] == str2:
#                 return 1
#     return 2
# str1 = "ab6CDE443fgh22iJKlmn1o"		
# str2 = "6CD"			
# print(solution(str1, str2))

## 배열의 평균값
# def solution(numbers):
#     t = 0
#     for i in numbers:
#         t += i
#     return t/len(numbers)

# ## 배열 뒤집기
# def solution(num_list):
#     new_list = []
#     t = len(num_list)
#     for i in range(len(num_list)):
#         new_list.append(num_list[t-1])
#         t -= 1
#     return new_list

# def solution2(num_list):
#     return num_list[::-1]

# num_list = [1, 2, 3, 4, 5]
# print(solution2(num_list))

## 제곱수 판별
# def solution(n):
#     r = n ** 0.5
#     if int(r) == r:
#         return 1
#     else:
#         return 2
    
## 짝수 홀수 개수
# def solution(num_list):
#     j = 0
#     h = 0
#     for i in num_list:
#         if i % 2 == 0:
#             j+=1
#         else:
#             h+=1
#     result = [j, h]
#     return result

# num_list = [1, 3, 5, 7]
# print(solution(num_list))

## 아이스아메리카노 한잔 5,500원
# def solution(money):
#     return list(divmod(money, 5500))

# print(solution(15000))

## 문자 반복 출력
# def solution(my_string, n):
#     answer = ""
#     for i in my_string:
#         for j in range(n):
#             answer += i
#     return answer

## 편지지 길이
# def solution(message):
#     return len(message) * 2

# message = 'i love you~'
# print(solution(message))        

##삼각형의 완성조건 (1)
# def solution(sides):
#     max_val = max(sides)
#     sides.remove(max(sides))
#     if max_val < sum(sides):
#         return 1
#     else:
#         return 2
# sides = [1, 2, 3]
# print(solution(sides))


## 세균증식
# def solution(n, t):
#     for i in range(t):
#         n = n * 2
#     return n

# print(solution(7, 15))

## 최댓값 만들기
# def solution(numbers):
#     numbers.sort()

numbers = [0, 31, 24, 10, 1, 9]
numbers.sort()
print(numbers)

