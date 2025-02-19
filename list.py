# arrays
# string[] names = new {'Anish','sony','Gopika'}

names = ['Anish','anish','sony','Gopika']
names2 = ['Vinish','sunil','remo']

data = ['Sony',24,True]

empty_list = []

print(names[2])

print("Anish" in names)

print(names[-1])
print(names.index('Gopika'))

print(names[0:2])
print(names[1:1])
print(names[-3:-1])

print(names[:])
print(names[: :-1])
print(names[0:2])

print(len(names))

names.append('Vishnu')

names += ['gopi','suthakar']
names.extend(['robi','kanna'])
names.extend(names2)

print(names)

# names2.insert(1,'abi')
# print(names2)

print(names2)
names2[0:2] = ['ai','ci','llm','bbc']
print(names2)

# remove

names2.remove('ai')
print(names2)

print(names2.pop()) # remove and return
print(names2)

del names2[0:2]
print(names2)

names2.clear()
print(names2)

#sorting

names.sort()
print(names)

names.sort(key=str.lower)
print(names)

nums = [2,4,6]
nums.sort()
# nums.sort(reverse=True)
nums.reverse()
print(nums)

print(sorted(nums,reverse=True))

print("Copy Layer Start")
print("--------------------")
print()
# --- List Copying ---

num_copy = nums.copy()
mylist = list(nums)
my_copy = nums[0:2]

print(num_copy)
print(mylist)
print(my_copy)

print(type(mylist))

new_list = list([1,'Sony',True])
print(new_list)

print("")
print("--------------------")