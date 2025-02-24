
# Sets

list = [1,0] 
tuples = (2,5,8)
dic = {"key":"values"}
sets = {2,5,8,0}


sets = {2,5,8,0}
set1 = set((3,4,1,46))

print(type(set1))
print(type(sets))

# No Duplication allowed

num = {1,2,2,3}
print(num)

# True is dupe of 1 , False is dupe of zero
nums = {0,2,True,4,5,7,False,1}
print(nums)

# True r False 
print(2 in nums)


# Adding 
nums.add(9)
print(nums)

other_set = {11,15,19}
nums.update(other_set)

print(nums)


# Merge two set
one = {1,2,3}
two ={3,4,5}

new_set = one.union(two)
print(new_set)

one.intersection_update(two)
print(one)

one.symmetric_difference_update(two)
print(one)