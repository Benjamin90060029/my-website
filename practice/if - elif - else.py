name_list = ['eric','ben','admin','jam','jannie']

name_list2 = ['erics','Ben','admins','Jam','jannies']

for jack in name_list2:
    if jack.lower() not in name_list:
        print('hi ' + jack)
    elif jack.lower()  in name_list:
        print('fuck of '+ jack)
if len(name_list2) > 3:
    name_list2.append('leep')
print(name_list2)
number = []
for value in range(1,11) :
    number.append(value)
    if value == 1:
        print(str(value)+'st')
    elif value == 2:
        print(str(value) + 'nd')
    elif value == 3:
        print(str(value) + 'rd')
    else:
        print(str(value) + 'th')