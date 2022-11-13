#dictionary,{"key":"value"}
# #tuple,()
# list,[]
# set
list = ["james  odhiambo", 80, 90.9, 'A']

list.append(98)
print(list)
dictionary = {
    'name' : 'gstrhtgjdyjshntt',
    'age' : 21,
}
print(dictionary['age'])
print(type(dictionary))
jeff={
    'name': "odegi",
    'age': 47,
    'grade': 'd',
}
print(type(jeff))
print(jeff['name'])
mydivtionary={True:1}
print(mydivtionary)
#myv={[]:"value"}
student={
    'name':'Odegi',
    'age':76,
    'reg':'sct211',
    'course':{
        'code':'tid444',
        'name':'programming',
        'units':['maths','english']
    }
}
student.update(17)
print(student.keys())
print(student.values())
print(student.items())
myset2={7,9,8,5,4}
myset={1,2,2,3,5,5}
print(myset)
print(myset.intersection(myset2))
print(myset.union(myset2))
print(myset.difference(myset2))
students=['James','Jane','Mike']
for students in students:
    print(students)