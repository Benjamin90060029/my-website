prompt = "How old are you:"
achieve = True
while achieve:
    pizza = input(prompt)
    pizza = int(pizza)
    if pizza < 3 :
        print('your ticket is free')
    elif pizza < 12:
        print('your tickit is 10 dollar')
    else:
        print('your pizza is 15 dollar')
