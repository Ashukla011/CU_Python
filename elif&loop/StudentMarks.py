# write a program to input a persentage maked of student grad as per following 

S_Scrore = float(80)

S_gread = "",

if S_Scrore >= 90:
    S_gread = 'A'
  
elif S_Scrore >= 75 and S_Scrore <=89:
     S_gread = "B"
    
elif S_Scrore >= 60 and S_Scrore <= 74:
     S_gread = "C"
   
else:
     S_gread = 'D'
    
print("Gread is :" , S_gread)
