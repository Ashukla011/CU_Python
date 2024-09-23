# 1. Creating list 
Vegitables = ['Tomato','Putato','Carrot','Mashroom','Pampkin',]

# 2. Accessing  elements  
first_element = Vegitables[0]
last_element =  Vegitables[-1]

# 3. Adding elements
Vegitables.append("Kiwi") # Adds to the end 
Vegitables.insert(2,'Broccoli') # Insert at index 2
fruits = ["Papaya","Banana"] # add it in Vegitable list
Vegitables.extend(fruits) # Added in Vegitable lis 

# 4. Removing elements
Vegitables.remove("Tomato")
popped_element = Vegitables.pop(2) # Remove and return the element at index 2
del Vegitables[3] # Deletes the element at index 3

# 5.  Slicing The List 
subList1 = FromtwoTothree= Vegitables[2:4] # from index 2 to 3 
lastthree = Vegitables[-3:] # last 3 element
startthree = Vegitables[:3]  # start three element 

# 6. Length of the Vegitable list 
x = len(Vegitables)

# 7. Reverse the Given Vegiatbel list 
Vegitables.reverse()

# 8. shorting the list asc and desc order 
Vegitables.sort()

# 9. Looping the list element 
for i in Vegitables:
    print(i)

# printing the final list and other outputs
print("Final List:",Vegitables)
print("First Element:",first_element)
print("Last Element:",last_element)
print("sublist:",subList1)
print("last three:",lastthree)
print("Start Three :",lastthree)
print("Length:",x)
print("Popped element:",popped_element)
