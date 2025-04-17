""" season = ['봄', '여름', '가을', '겨울']

print(season)
print('season[0]', season[0])
print('season[1]', season[1])

text = 'hello'
letters = list(text)
print('letters', letters) """
"""
shop = ['반팔', '청바지', '이어폰', ['무선이어폰', '유선키보드']]
shop[0] = '긴팔'
print(shop)
del shop[0]
print(shop)
del shop[0:1]
print(shop) """
"""
num = [3, 1, 7, 8]
num_asc = sorted(num)
print(num)
print(num_asc) """
"""
num = [3, 1, 2, 4]
num.sort()
print(num)
num.sort(reverse=True)
print(num) """
"""
num = ['a', 'b', 'c', 'd', 'c']
print(num.count('c')) """
""" 
rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']
print(rainbow[1])
print(sorted(rainbow))
rainbow.append('mint')
print(rainbow)
del rainbow[2:6]
print(rainbow) """
""" 
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]
value = matrix[1][2]
print(value)

matrix[1] = matrix[1] + [100]
print(matrix)
matrix = matrix + [[10, 11, 12]]
print(matrix)
del matrix[1]
print(matrix)

rows = len(matrix)
cols = len(matrix[0])
print(f'행: {rows}, 열: {cols}') """

""" 
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
s3 = {2, 3, 4, 9, 10, 11}

s4 = (s1 & s2) - s3
print(s4)

dict1 = {}
print('dict1', dict1)
dict2 = ()
print('dict2', dict2)

dict1 = {
    'name': '홍길동',
    'age': 30,
    'city': "서울"
}
print('dict1', dict1)
print(dict1['name'])
dict1['name'] = "최흥기"
print(dict1)

dict1['city'] = "인천"
print(dict1)

dict1['생년월일'] = 20020625
print(dict1)

dict1["hobby"] = ["캠핑", "등산", "러닝"]
print(dict1)

del dict1["hobby"]
print(dict1) """

""" fruits = {'apple': '사과', 'banana': '바나나'}
print(fruits)
fruits.update({'grapes': "포도", 'melon': '멜론'})
print(fruits)
 """

""" student_test = {'Alice': 85, 'Bob': 90, 'Charlie': 95}
print(student_test)
student_test.update({'David': 80})
print(student_test)
student_test.update({'Alice': 88})
print(student_test)
del student_test['Bob']
print(student_test)
 """

numbers = [10, 20, 30, 40]
result = sum(numbers)
print(result)

scores = {'국어': 85, '영어': 90}
total_score = sum(scores.values())
print(total_score)
