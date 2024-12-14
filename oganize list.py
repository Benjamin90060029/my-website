names = ['k','f']
s1 = 'hello\t'+names[0]
s2 = 'hello\t'+names[1]
s3 = 'hello\t'+names[2]
print(s1+'\n'+s2+'\n'+s3)
names[0] = 'magi'
print(names)
name2 = names.pop(1)
names.insert(1,'han')
print(name2)
print(names)
s1 = 'hello\t'+names[0]
s2 = 'hello\t'+names[1]
s3 = 'hello\t'+names[2]
print(s1+'\n'+s2+'\n'+s3)
names.append('bee')
names.append('cat')
names.append("gg")
print(names)
while len(names) > 2:
    sorry = "i am sorry "+"\t"+names.pop()+"\t"+"we can't have dinner"
    print(sorry)
print(names)
while len(names) > 0:
    youarein = names.pop() + "\t" + "wish we have a great dinner"
    print(youarein)
print(names)