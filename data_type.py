import math

# String data type

first = "Anish"
last = 'sony'

print(type(first))           # <str>
print(type(last) == str)     # True
print(isinstance(first,str)) # True

# constructor function

girl = str('Gopika')
print(type(girl))   # str
print(type(girl) == str)     # True
print(isinstance(girl,str))


# Concatenation 
full_name = first + "  " + last

print(full_name)

# full_name = full_name + " !"
full_name += " !"

print(full_name)

#type Casting a num to String

num  = 10 # int
num = str(num) # str
print(type(num)) #str


statement = "I like a Cricket player num " + num +" ! ." 

print(statement)

mulitline = '''
hey , Gopika 
sugam ano
Work ila?

'''
print(mulitline)

sentence = 'I\'m back at Work! \tHey!\n\nWhere\'s this at \\located?'

# String methods

print(full_name.upper())
print(full_name.lower())

print(full_name)

print(full_name.title())
print(full_name.replace('s','mony'))

print(len(full_name)) #13

full_name += '              '

full_name = '              ' + full_name

print(len(full_name)) # 41

print(len(full_name.lstrip())) 
print(full_name.lstrip())
print(len(full_name.rstrip()))
print(full_name.rstrip())


print(full_name.strip())

print(len(full_name.strip()))

full_name = full_name.strip()

print(full_name)

# index in string

print(full_name[0]) # A
print(full_name[-6]) # s
print(full_name[1:5]) #nish
print(full_name[1:]) #nish sony !
print(full_name[ :8]) # Anish s
print(full_name[ : ]) # Anish sony !

print(full_name[ : : -1])

student = "Gopika"

# some boolen meathed in String 
print(student.startswith('G')) # True
print(student.endswith('a')) # True
print(student.startswith('g')) # False
 
# boolen
myvalue = True
x = bool(False)

print(type(x)) # bool
print(isinstance(myvalue,bool)) # True

# Numerical Data types 

#int 
price = 100
best_price = int(200)

print(type(best_price)) # int
print(isinstance(price,int)) # True

# folat type 

gpa = 21.2
y = float(20.45)

print(type(gpa)) # float
print(isinstance(y,float)) # True


# complex type
complex_val = 5+3j
print(type(complex_val))
print(complex_val.real)
print(complex_val.imag)

x = int(complex_val.real)

print(type(x))

# Bulit-in functions for nums

print(math.sqrt(25))
print(math.pow(2,2))
print(math.floor(gpa))
print(math.ceil(gpa))
print(math.pi)

zipcode = "10001"

zip_val = int(zipcode)

print(type(zip_val))
