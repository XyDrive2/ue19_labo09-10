from requests import get
r = get("https://punapi.rest/api/pun", auth=('user', 'pass'))
print(r.json()['pun'])
a = input('[ENTER] To Leave')
