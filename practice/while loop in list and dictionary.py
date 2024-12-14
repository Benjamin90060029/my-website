dict = { }
conlect_name = True
while conlect_name :
    name = input('name:')
    id = input('your personal id')
    dict[name] = id
    repeat = input('would you like to do this again(yes/no)')
    if repeat == 'no':
        conlect_name = False
print('\n---line---')
for names,ids in dict.items():
    print(names + "'s id is "+ids)