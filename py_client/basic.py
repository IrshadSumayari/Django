
import requests

# endpoint = "https://httpbin.org/status/200/"
endpoint = "http://127.0.0.1:8000/api/"

get_request = requests.get(endpoint) #http get request using request library
print(get_request.text)
print(get_request.status_code)
print(get_request.json)
