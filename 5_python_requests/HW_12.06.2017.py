import requests

url = 'https://httpbin.org/post'

data = {
    'first_name': 'Yurii',
    'last_name': 'Khomych',
    'email': 'yuriykhomich@gmail.com',
    'password': '12345'
}
my_request = requests.post(url, data)
data = my_request.json()
print(data['form'])