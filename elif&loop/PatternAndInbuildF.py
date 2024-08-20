# Pertter and inbuild-function in python 

#  Find the give number is prime or not 
# To determine whether 13 is a prime number, we'll check if it has any divisors other than 1 and itself.
# A prime number has no divisors other than 1 and itself, so we'll check for divisibility from 2 to the square root of 13.

import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

is_prime(13)

# Right angle tringle 

row = 5
for i in range(1,row+1):
    print("*" * i)
# Equalatral Trangle Pattern 
rows = 5
for i in range(1, rows + 1):
    print(' ' * (rows - i) + '*' * (2 * i - 1))
#3. Square Pattern
rows = 5
for i in range(rows):
    print('*' * rows)

# 4 4. Hollow Square Pattern
rows = 5
for i in range(rows):
    if i == 0 or i == rows - 1:
        print('*' * rows)
    else:
        print('*' + ' ' * (rows - 2) + '*')

# 5. Rhombus Pattern
rows = 5
for i in range(rows):
    print(' ' * (rows - i - 1) + '*' * rows)

# 6. Hollow Rhombus Pattern
rows = 5
for i in range(rows):
    if i == 0 or i == rows - 1:
        print(' ' * (rows - i - 1) + '*' * rows)
    else:
        print(' ' * (rows - i - 1) + '*' + ' ' * (rows - 2) + '*')

#7. Diamond Pattern

rows = 5
for i in range(1, rows + 1):
    print(' ' * (rows - i) + '*' * (2 * i - 1))
for i in range(rows - 1, 0, -1):
    print(' ' * (rows - i) + '*' * (2 * i - 1))

# 8. Hollow Diamond Pattern

rows = 5
for i in range(1, rows + 1):
    print(' ' * (rows - i) + '*' + ' ' * (2 * i - 3) + ('*' if i != 1 else ''))
for i in range(rows - 1, 0, -1):
    print(' ' * (rows - i) + '*' + ' ' * (2 * i - 3) + ('*' if i != 1 else ''))

