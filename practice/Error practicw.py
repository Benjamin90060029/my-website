print('pls give mme two number')
print('press q to quit')
start = True
while start:
    frist_number  = input('give me the frist number:')
    if frist_number == 'q':
        break
    second_number = input('give me the second number ')
    if second_number == 'q':
        break
    try:
        total = int(frist_number) / int(second_number)
    except ZeroDivisionError:
        pass
    except ValueError:
        print('pls input number thank you')
    else:
        print(total)