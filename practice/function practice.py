def display_message(fr_name,la_name):
    full_name = fr_name + ' ' + la_name
    return full_name.title()
button = True
while button:
    print('Please tell me your name')
    f_name = input('Frist_name:')
    l_name = input('Last_Name:')
    copilet_name = display_message(f_name,l_name)
    print('\nfhello '+copilet_name)
    stop = input('do you what to input again(YES  N0?)')
    if stop.lower() == 'no':
        button = False
        print("thanks for using")

