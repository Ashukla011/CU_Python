#SET 
'''
1. A set is an unordered collection of unique elements
2. Sets are defined using curly braces '{}' or the 'set()' function 
3. Since set are unordered , the elements don't have specific position
   and there's no way to access an element by an index like you would in list or tuple

'''

my_set ={1,2,3,4}
another_set =set([1,2,3,4])
print("my set and another set:",my_set,another_set)

#Unordered
my_unordered_set = {3,1,2}
for  i in my_unordered_set:
    print(i)
print(my_unordered_set)

# Mutable
# no indexing or slicing

#common set oration 
# 1. Add
my_set.add(5)

# Removing 
my_set.remove(2)
my_set.remove(5) # does nothng as 5 is not in the set 

a = {1,2,3}
b = {3,4,5}
print(a | b) # {1,2,3,4,5}
print(a & b) # {3}
print (a-b) # {1,2} containig elements that are in set a 
print(a^b) # {1,2,4,5}

#Removing Duplicates
number = [1,2,3,4,5,6,5,]
unique_number = list(set(number))
print(unique_number) # [1,2,3,4,5,6]

# loop 
