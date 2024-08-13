# my list 

mylist_no = [1,2,3,4,5,6,7]
print(mylist_no)

# list of string
mylist_str = ['a','b','c','d','e','f']
print(mylist_str) #['a','b','c','d','e','f']

# list of boolean value
mylist_bool = [True, False, False, True]
print(mylist_bool) #[True, False, False, True]

#data type of list 
print(type(mylist_no), type(mylist_str), type(mylist_bool))

#list can contain data of different data type
mylist_diffirent_data_type = [True,'false',False,1,'string',]
print(mylist_diffirent_data_type) #[True,'false',False,1,'string']

#INDEXING
#Index start with zero
mylist = [1,2,3,4,5,6]
print(mylist[3]) # 4
mylist[3] = 19
print(mylist) # [1,2,3,19,5,6]
#duplicate list 
mylist_duplicate = [2,2,3,3,4,5,6,7]
print(mylist_duplicate) # [2,2,3,4,5,6,7]

#constractore in the list 
mylist_constractor = list((2,3,4,5,6,7,8))
print(mylist_constractor) # [2,3,4,5,6,7,8]

# how many item in the list 
mylist_l = [1,2,3,4,5]
print(len(mylist_l)) #5

#print minus index value it will give from end 
mylist_with_negative = [1,2,3,4,5,6,7]
print(mylist_with_negative[-1]) # 7

# strt : end  , there end index value is excluded always but start included 

mylist_start_end = [1,2,3,4,5,6,7,8,9]
print(mylist_start_end[2:4]) #[3,4]
print(mylist_start_end[ :6]) #[1,2,3,4,5,6]
print(mylist_start_end[4:]) #[5,6,7,8,9]
print(mylist_start_end[4:-1]) #[5,6,7,8]

# HOME WORK 
#Sort the list, alphabeticaly and numericaly 
unsorted_list  = [4,2,2,7,4,1,3,8,10]
unsorted_list.sort()
print("now it is sorted:",unsorted_list)

unsorted_alpha = ['zero','mango','apply','dog','ent','nothing']
unsorted_alpha.sort()
print("now it is sorted:",unsorted_alpha)

# how to appen dmore than one items at list 
appendlist = [1,2,3,4]
appendlist.append(1)
# use extend function to appen more than on list 
appendlist.extend([5,6,7])
print("extentd",appendlist)
# copy of the list 
thislist = ["apple", "banana", "cherry"]
x =thislist.count("apple")
print("count:",x)
mylist = thislist.copy()
print(mylist)
# this is l1 and l2 list append list l2 at the en dof list l1 
l1 =[1,2,3,4]
l2 = [5,6,7]
l1.extend(l2)
print("l1&l2",l1)
l3 = l1+l2
print("join list :", l3)
# pop 
popoflist = [1,2,3]
popoflist.pop()
print("popoflist:",popoflist)
thislist.clear()
print("clear this list :",thislist)

# all posiblity of rang e
mylist = [100,200,300,400,500]
print("range",mylist[-5:-2]) # print the entaire list 

# mylist[1:4] , print from [200,300,400]
# mylist [:3] , print from [100,200,300]
# mylist [2:] , print fomr [300,400,500]
# mylist [-3:] , print last three [300,400,500] 
# mylist [:-2], print firt two [100,200]
# mylist [-2:-3] , nothing 
# mylist [-4,:-3], []
# mylist [-5:-2], [100,200,300]
abc =[1,2,3]
if 10 in abc :
    print ("it is true:",True)
else :
    print ("it is false:",False)

# for loop 

mylistforloop = [1,2,3,4,5,6]
for x in mylistforloop:
    print(x)

