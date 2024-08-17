# 3.1.1 Numbers 

# classic division returns a float 
print(17/2) # 5.666666666667
print(17//3) # 5 floor division descars the fractional part 
print(17%3)  # the % operator returns the remainder of the division 

print(5*3+2) # floored quotient * divison +remainder

# with python , it si possible to use the ** operator to calculate powers
print(5**2) # 25 squared 
print(2**7) # 128

#if a variable is not "defined "(assigned a value) , try to use it will give an error:
#  n 
# print(n)

# There is fulll support for floating point, 
#operators with mixed type operands convert the integer operand to floating point:
print(4*3.75 - 1)

#In interactive mode, the last printed expression is assigned to the variable _. 
# This means that when you are using Python as a desk calculator, it is somewhat easier to continue calculations, for example:
tax = 12.5/100
price = 100.50
price*tax


