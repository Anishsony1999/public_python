
name = input('Enter Your Name \n')

if type(name) == str :
    print(name)
else :
    print('please Enter a valid Name')


#Ternary oprater

print('Yes This is Str!') if type(name) == int else print('Not Str')