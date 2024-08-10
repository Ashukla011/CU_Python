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
