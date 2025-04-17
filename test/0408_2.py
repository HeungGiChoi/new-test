import requests
import json

# 외부 API에서 데이터를 가져옴
url = "https://api.sampleapis.com/avatar/info"
response = requests.get(url)

# print(response.status_code)
if response.status_code == 200:
    data = response.json() # json값으로 가져오기
    # print(data)
    # for i in data:
    #     print(f"ID: {i['id']}, 제목: {i['synopsis']}")

print(response.text)