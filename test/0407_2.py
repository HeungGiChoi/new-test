# import json

# data = {
#     "name": '홍길동',
#     "age": 20,
#     "city": '서울'
# }

# json_str = json.dumps(data)
# print(json_str)

# json_obj = json.loads (json_str)
# print(json_obj)
import random
import time

eng_voka = ['apple', 'truck', 'gun', 'mountain', 'silver', 'gold', 'avengers', 'ironman', 'captinAmerica', 'TheGreat_showman']

while True:
    total_words = 0
    start = time.perf_counter()
    for i in eng_voka:
        print(f"단어: {i}")
        input_voka = input("입력: ")
        if i == input_voka:
            print("통과!")
            total_words += 1
            continue
        else:
            while True:
                print("오타! 다시 시도하세요.")
                print(f"단어: {i}")
                input_voka = input("입력: ")
                if input_voka == i:
                    print("통과!")
                    total_words += 1
                    break
                else:
                    continue
    end = time.perf_counter()
    total_time = end - start
    print("게임 종료!")
    print(f"총 입력 단어: {total_words}")
    avg_time = total_time / total_words
    print(f"평균 단어당 입력 시간: {avg_time:.4f}")
    print(f"총 걸린 시간: {end - start:.4f}초")
    break

# 또한 한 단어당 입력에 걸리는 시간 측정
# 한 단어 입력 완료 시간 - 한 단어 시작 시간 측정
#   한 단어 입력 시간 저장하는 리스트
#   f"{리스트 sum / len(리스트):.4f}" 이렇게 하면 한 단어당 평균 입력 시간 구함
