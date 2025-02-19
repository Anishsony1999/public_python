
mytuple = tuple(('Dave',55,True))
nums = (2,4,2,1,46,8,95,3,21,4,6)

print(mytuple)
print(type(mytuple))
print(type(nums))

print(mytuple[0])
# mytuple[0] = 'ani'  / error

mylist = list(mytuple)
print(type(mylist)) # type  -> list

# [] -> list
# () -> Tuple

mylist.append('Sony')
print(mylist)

mytuple = tuple(mylist)

(*one,two,three) = mytuple

print(one)
print(two)
print(three)

print(len(mytuple))

print(mytuple.count('Sony'))

# Hello World -> dlroW olleH -Task one
# Hello World -> olleH dlroW -Task Two
