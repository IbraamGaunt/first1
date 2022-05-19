i=0
names = []
ages = []
f = open('Personal.txt','w')
while i==0:
    print('Name?')
    a1 = input()
    if a1 == "no":
        break
    names.append(a1)
    print ('age?')
    b1 = input()
    ages.append(b1)
f.write(str(names))
f.write(str(ages))
print("kirgizia")
f.close()