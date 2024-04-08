import requests

url = 'http://localhost:5000/predict'
response = requests.post(url)
print('Status Code:', response.status_code)
print('Response Text:', response.text)

try:
    print('JSON Response:', response.json())
except requests.exceptions.JSONDecodeError as e:
    print('Decoding JSON has failed:', e)

