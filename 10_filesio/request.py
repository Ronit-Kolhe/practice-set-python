import requests

r = requests.get('https://api.github.com/user/codewithharry')
print(r.text)

with open("rk.txt", "w") as f:
    f.write(r.text)