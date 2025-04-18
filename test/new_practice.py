import requests

# 외부 API에서 데이터 가져옴
url = "https://api.sampleapis.com/avatar/info"
response = requests.get(url)

# 응답처리
if response.status_code == 200:
    data = response.json()
    print("API 데이터: ", data)
else:
    print("API 요청 실패:", response.status_code)

