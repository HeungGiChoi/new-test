# 모듈
# 방법1
# import calc

# print(calc.add(2, 3))
# print(calc.sub(2, 3))
# print(calc.multiply(2, 3))
# print(calc.divide(2, 3))

# 방법2

# import calc as a

# print(a.add(2, 3))
# print(a.sub(2, 3))
# print(a.multiply(2, 3))
# print(a.divide(2, 3))

# 방법3
# from calc import *

# print(add(2, 3))
# print(sub(2, 3))
# print(multiply(2, 3))
# print(divide(2, 3))

# 표준모듈
from datetime import *

# now = datetime.today() # 현재시간
# print(now)
# print(now.year)
# print(now.month)
# print(now.day)
# print(now.hour)
# print(now.minute)
# print(now.second)

# print(f"{now.year}년 {now.month}월 {now.day}일 {now.hour}시 {now.minute}분")
# now = datetime.now()
# print(now)

# next_week = now + timedelta(weeks=1, hours=1)
# print(next_week)

# 타임존
# print(timezone.utc)
# print(datetime.now(timezone.utc))
# print(datetime.now(timezone(timedelta(hours=9))))

# # 날짜 포맷 변경
# now = datetime.now()
# print(now.strftime("%y년%m월%d일 %H:%M:%S"))

# from datetime import *

# open_day = date(year=2025, month=3, day=24)
# print(date.today().weekday())
# week = ['월', '화', '수', '목', '금', '토', '일']
# print(week[date.today().weekday()])

# pass_day = date.today() - open_day
# print(f"개강 후 {pass_day.days}일 지났습니다.")

# time 모듈
# import time

# print(time.time())
# print("5초 대기")
# time.sleep(5)
# print("대기완료")
# start = time.perf_counter() # 정밀시간 측정 
# time.sleep(2)
# end = time.perf_counter()
# print(f"{end - start:.2f}")

# 수학모듈
# import math

# print(math.pi)
# print(math.sqrt(25))
# print(math.factorial(5))
# print(math.ceil(2.3)) # 올림
# print(round(4.51)) # 반올림
# print(math.floor(5.9)) # 내림

# import random
# import math

# print(random.randint(100, 999))
# print(random.uniform(1.1, 9.9))
# print(random.random())
# print(random.randrange(100, 999))

# choices = [1, 2, 3, 4, 5, 6, 7, 8]
# print(random.choice(choices))

# rand = 1000 + math.floor(random.random() * 9000)
# print(rand)

# import random

# rand_int = set(random.randint(1, 45) for i in range(6))# 1~45까지 숫자 중 랜덤으로 6개 숫자 뽑기(변수에 리스트로 저장 / 중복 없이 )
# # rand_int.sort()
# print(sorted(rand_int)) # 오름차순으로 정렬(리스트 오름차순 정렬)

# lotto = random.sample(range(1, 46), 6)
# print(sorted(lotto))

# import sys

# print(sys.argv)
# print(sys.argv[1:])

# if "-h" in sys.argv or "--help" in sys.argv:
    # print("사용법: python main.py [옵션]")
    # print("-h, --help       도움말 표시")
    # print("-y, --version    버전정보표시")
    # sys.exit(0)

# print(sys.version)

import os

print("현재 디렉토리:", os.getcwd())
file_path = os.chdir(os.getcwd())
dir = os.popen('ls')
print(dir.read())

# os.mkdir("shell_test")
# os.rmdir("shell_test")
# print("디렉토리 삭제: shell_test")

print("PATH 환경 변수:", os.environ.get('PATH'))
