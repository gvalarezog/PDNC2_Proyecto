import requests

url = 'https://dummy.restapiexample.com/api/v1/employees'

respuesta = requests.get(url).json()
print(respuesta)