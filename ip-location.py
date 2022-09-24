from requests import get

ip = get('https://api.ipify.org').text
print(f'My public IP address is: {ip}')
response=get(f'http://ip-api.com/json/{ip}').json()
print(response)