import numpy as np

a = np.array([1,2,3])
print(a)
print(type(a))

# 2 Multi-dimensional Array 
# a = np.array([(1,2,3),(4,5,6,)])
# print(a)
# n1 = np.zeros((1,2))
# print(n1)

# a2 =np.zeros((1,2))
# print(a2)
# Initializing numpy array with same number
# a3 = np.full((5,5),10)
# print(a3)
# arange method 
# n1 = np.arange(10,20)
# print("N1 arange method:", n1)

# you print difference between numer 
# n2= np.arange(10,20,2)
# print(n2)
# numpy array indexing 
# indexing = np.array([1,2,3,4])
# print(indexing[3])
# get third an dfourth element from the array and add them 
# arr = np.array ([1,2,3,4,5],[1,2,3,4,5])
# print(arr[2]+arr[3])
# access the element on the first row , secodn column
# print(arr[0][1])
# negative indexing 
# negindex = np.array([1,2,3,4,5,6],[7,8,9,10])
# print('Last element from 2nd dim',negindex[1][-1])

# take two mattrics and add it print some of it 
# mat1 = np.array([[10,20,30,40,50],[60,70,80,90,100,],[1,20,30,40,50]])
# mat2 = np.array([[10,20,30,40,50],[60,70,80,90,100,],[1,20,30,40,50]])

# result = np.zeros((mat1.shape[0],mat2.shape[1]),dtype=int)

# shape of Numpy arrays 




# for i in range(mat1.shape[0]):  
#   for j in range(mat2.shape[1]):
#     result [i][j] = mat1[i][j] + mat2[i][j]

# print('sum of mat1 & mat2')
# print(result)