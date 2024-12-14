import json
username = input('please input your name.')

filename = 'username.json'
with open(filename , 'w') as gg:
    json.dump(username, gg)
    try:
        username
    except ValueError:
        print('pls input word')
    else:
        print('hello ' + username)