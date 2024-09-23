# TUPLES
''' 
1. a tuple is an ordered collection of elements that is immutable,meanign its contents con not be changed after it is created 
2. Tuples are defined by placing a comma-separated sequence of elements inside parenthese '()'
'''

my_tuple = (1,2,3)
mixed_tuple = (1,2,'hello',2.14)
x =len(mixed_tuple)
getmix_mx =([1,2,3,4,5])
location_dict = {("New York","USA"):8175133,("Paris","France"):2140526}
point =(4,5)
x,y = point
print(x,y)
print(location_dict)
print("get min max:",getmix_mx)
print(my_tuple)
print(x)
print(mixed_tuple)

for i in my_tuple:
    print(i)

'''
Tuples are a powerful tool in Python when you need an ordered,
 immutable collection of items. They are particularly useful when
   you want to ensure that the data remains unchanged, need to return
     multiple values from a function, or use complex keys in dictionaries.
       Their immutability, efficiency, and ability to store heterogeneous 
       data make them a versatile and essential part of Python programming.
'''