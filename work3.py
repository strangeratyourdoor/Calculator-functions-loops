Fullname=input('Enter full name')
# print(Fullname.split(" "))
fname,lname=Fullname.split(" ")
fchar=fname[0].upper()
fchar2=lname[0].upper()
fname1=fchar+fname[1:].lower()
lname1=fchar2+lname[1:].lower()
nm = f"{fname1} {lname1}"
print(nm)

