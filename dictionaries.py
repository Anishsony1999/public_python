# Dictionary

student1 = {
    "Name" : "Anish",
    "Age" : 24,
}

student2 = dict(Name = "Gopika" , Age = 28)

print(student1["Name"])
print(student2["Age"])

# gives All keys
print(student2.keys()) 

# gives all values
print(student1.values()) 

# give a key and values as tuples
print(student1.items())

# verify a key exits
print("Name" in student2) # True
print("Anu" in student2)  # False

nums = [1,2,3,4,5,6]
nums[0] = 11

print(nums)

# Changing Value

student1["Name"] = "Manish"
print(student1)

student2.update({"Age":22})
print(student2)

# Remove Items

print(student2.pop("Age"))
print(student2)

print(student2.popitem()) # tuple
print(student2)

# Del and Clear

del student1["Age"]

print(student1)

# Clear
student1.clear()

del student1

# copy Dictionaries

car = {
    "Eng" : "Lab",
    "Tire" : "MRF"
}

# car2 = car

# print(car2)
# # but this is bad copy

# car["Eng"] = "BMW"
# print(car)

# car2["Eng"] = "Maruthi"
# print(car)

car2 = car.copy()

car2["Eng"] = "BMW"
print(car)
print(car2)

# dict() constructor function
car3 = dict(car)

# Nested Dict

member1 = {
    "Name" : "Vinish",
    "Age" : 55
}

member2 = {
    "Name" : "Binish",
    "Age" : 34
}

members = {
    "member1" : member1,
    "member2" : member2
}

print(members)

print("")
