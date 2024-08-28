# in python small anonymous function it can take any number of argument but can have only one exprestion 
# lambada argument:expression 

# addtion in lambda function 
y= lambda a : a+10
print("add singl:",y(6))

# multiplication in lambda function 
x = lambda a,b : a*b
print("multi of numer:",x(20,10))

Z = lambda a,b,c : a+b+c
print("three add: ",Z(20,30,40))

# this lambda function is very usefull when we used it as an anonymous function inside other function 
# note : use lambda function when an anonymous function is requred for a short perioud of time 

def myfunc(n):
 for i in range(1,n) :
  return lambda a: a*i

mydub = myfunc(10)

print(mydub(2))

# map function 
'''The map function exicutes a spacific function for each items in an iterable  '''

def square (num):
 return num**2

num = [1,2,3,4,5]
squared = map(square,num) 

squared_list = list(squared)

print(squared_list)

# Filter function 
''' The filter function in python is used to crate a new iterator from an iterable for which 
    a fuction return true or we can say that filter fuction can be used to extract element 
     from in iterable that meets or stisfied sertain condition  '''
# filter () 

num = [6,10,15,18,31,27,64,100]

def vote (x):
  if x<18 :
    return True 
  else:
    return False

minor = filter (vote , num)
for x in minor:
 print(x)
 
 
 # Reduce function 
 '''The reduce function access a fuction in sequance and returns a single value based 
    following calculation intialy the function is called with the first two items from the 
    sequance and result is return , the function is then called again with the result optained 
    step one and the next value in the sequance the avobe proccess is step two keeps repeting 
    untill there are items in the sequance , 
    In python 2 reduce was a build in function in python 3 it is move to "functools module" 
     '''

from functools import reduce

def sum (x1,x2):
    return x1+x2

x = reduce(sum,[20,30,10,10,30,40])
print("reduce or sum :",x)

# REPL - Read Evaluate Print Loop 
'''  '''