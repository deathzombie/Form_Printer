name = input("Enter your Name :")
age = input("ENter your Age :")
gend = input("F/M :")
occ = input("Enter your Occupation :")

if gend == "f":
    gend = "Female"
elif gend == "F":
    gend = "Female"    
else : 
    gend = "Male"


if occ == "" :
    occ = "Student/Juvenile"
else : 
    occ = occ

print("Name :{0}\nAge :{1}\nGender :{2}\nOccupation :{3}\n".format(name,age,gend,occ))
