import requests as requests

result = []
response = requests.get('https://jsonmock.hackerrank.com/api/article_users?page=1')
responseDict = response.json()

userList = list(responseDict.get('data'))
for user in userList:
    submission_count = int(user.get('submission_count'))

