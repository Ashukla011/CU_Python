import numpy as np 

n1 = np.array([(1,2,3),(4,5,6)])

print(n1.shape) # dimention of array nomber of row and column

n1.shape=(3,2)
print(n1) # 3 tow and 2 column matrix

# n1.shape =(6,1)
n1.shape = (6,1)
print("shape one :",n1) 

# Convert the following 1-p array 12 element inot a 2-d array
'''
Shape of an array in the number of element in each dimention 
with the help of reshape adding or removing of element in turn dimention 
in earch dimention can be done 
''' 
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr = arr.reshape(4,3)
newarr2 = arr.reshape(2,3,2)
print("new array using reshape:",newarr)
print("new array using reshaped sec. :",newarr2)

# Iterating arrays 
for x in arr:
  print("Interating arrays:",x)

twodarr= [[1,2,3],[4,5,6]]
for x in twodarr:
  for y in x:
    print(y)

# Joining Numpy Arrays:

a1 = np.array([(1,2,3),(1,2,3)])
a2 = np.array([(6,7,8),(6,7,8)])

# print(np.vstack(a1,a2))

'''
How Work 

1- what is the meaning of axes parameter  in sum function 
2- Explaor spliting of arry for multidimantional 
'''
''' 
img. 1 - Recall and explain different methmetical and statical funciton in numpy with exmple 
at lets 10 mathe and 10 statical 

'''
# splitting Numpy Arrays:

splitarr = np.array([1,2,3,4,5,6])
newsplitarr = np.array_split(splitarr,3)
print(newsplitarr)


# Searching and Sorting Numpy Arrays:

serarr = np.array([1,2,3,4])
x = np.where(serarr == 4)
print(x)
