
# Loops :-

# 1, while
# 2, for

value = 1

# while True :

while value <= 10 :
    value +=1  
    print(value)
else :
    print("Condition false")
    
print("loop End")


# for(i=1; i<=10; i++ )
for value in range(1,11):
    print(value)

for i in range(1,101):
    if i % 2 == 0:
        print(i)

# take input , ex:2
# 1 * 2 = 2
# 10 * 2 = 20

print("==============")
print()
print()

for i in range(0,11):
    if i == 5:
        print(i)
else:
    print("loop end")

print("==============")
print()
print()

for i in range(11,0,-1):
    print(i)


names = ['Anish','Gopika','Sony','Ameen']
name = ''
for i in names :
    if i == 'Anish':
        name += i
    elif i == 'Sony':
        name += ' '+i

print(name)

for i in "Anish Sony":
    print(i)

for name in names :
    name = name.lower()
    if name == 'gopika':
        break
    print(name.title())

skils = ['Wake','Code','Eat','Sleep']

for i in range(0,len(skils)):
    print(skils[i])

for i in range(0,len(names)): # i = 0
    for j in range(0,len(skils)): # j = 0
        print(names[j] +" "+ skils[i])



