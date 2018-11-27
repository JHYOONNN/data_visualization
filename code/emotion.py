import requests

client_id = "YOUR_CLIENT_ID"
client_secret = "YOUR_CLIENT_SECRET"
url = "https://openapi.naver.com/v1/vision/face" 
files = {'image': open('t2.jpg', 'rb')}
headers = {'X-Naver-Client-Id': '1dTA0Fc_u_IVnCMsVMM3', 'X-Naver-Client-Secret': 'r8ndfo5jR5' }
response = requests.post(url,  files=files, headers=headers)
rescode = response.status_code

if(rescode==200):
    data = response.json()
    print(data["faces"][0]["emotion"]["value"])
    print(data["faces"][0]["emotion"]["confidence"])
else:
    print("Error Code:" + rescode)