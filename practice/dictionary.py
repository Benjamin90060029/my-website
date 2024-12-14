car = input('what car do you what:')
print('ok i got it')
dinner = input('how many people is going to have dinner:')
dinner = int(dinner)
if dinner > 8:
    print('we have no seat')
else:
    print('we have ' + ' ' +str(8 - dinner) + ' seat left')
numbers = input('what numbers:')
numbers = int(numbers)
if numbers % 10 == 0 :
    print("是10的倍數")
else:
    print("不是10的倍數")
