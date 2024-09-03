import numpy as np
a = np.array([1,2,3])
print(a)
print(type(a))

# 2 Multi-dimensional Array 
a =np.array([(1,2,3),(4,5,6)])
print(a)

n1 = np.zeros((1,2))
print(n1)

n2 = np.zeros((5,5))
print(n2)

n3 = np.full((5,5),10)
print(n3)
# arange method 
n4 = np.arange(10,30)
print(n4)

n5 = np.arange(10,20,3)
print(n5)

arr1 = np.array([1,2,3,4,1,2,3,4])
print(arr1[0])

arr2 = np.array([[1,2,3,4,5],[6,7,9,20,10]])
print('2nd elemement on 1st row:',arr2[0,1])
print('last element of 2nd row :',arr2[1,-1])

# Array slicing 

print(arr1[1:5])

print(arr2[1,1:3])




# take two mattrics and add it print some of it 
mat1 = np.array([[10,20,30,40,50],[60,70,80,90,100,],[1,20,30,40,50]])
mat2 = np.array([[10,20,30,40,50],[60,70,80,90,100,],[1,20,30,40,50]])

result = np.zeros((mat1.shape[0],mat2.shape[1]),dtype=int)



for i in range(mat1.shape[0]):  
  for j in range(mat2.shape[1]):
    result [i][j] = mat1[i][j] + mat2[i][j]

print('sum of mat1 & mat2')
print(result)