# # rules for declaring variables
# # must start with alphabet or underscore
# # must not be a keyword or reserved word
# # must not have special characters e.g, $
# # must not have space between
# # syntax def <function-name>([<parameters>])
# # def add(num1,num2)
# #   sum=num1+num2
# #   print(sum)
# # add()  call
# # diff btwn argument and parameter...arguments are values passed when calling a function...code below marks1 and marks2 are parameters
def average():
     math = int(input("Enter math marks"))
     eng = int(input("Enter Eng:"))
     avg = (eng + math) / 2
     print(f"Average:{avg}")


average()
# def average2(marks1, marks2):
#     avg = (marks1 + marks2) / 2
#     print(f"Average:{avg}")
#
#
# # average2(37,48)
# def average3(marks1, marks2):  # ->float...specifies data type:
#     avg = (marks1 + marks2) / 2
#     return avg
#
#
# a = average3(8, 9)  # call
# print(a)
#
#
# # a=average3(marks3=4,marks2=8)...keyword argument
def get_Student_Details(name, regnumber, age, yearofstudy, dateofbirth, is_self_sponsored=True):
     print(f"Name: {name}")
     print(f"Reg: {regnumber}")
     print(f"Age: {age}")
     print(f"YOS: {yearofstudy}")
     print(f"DOB: {dateofbirth}")
     print(f"Self sponsored: {is_self_sponsored}")

get_Student_Details("Odegi", "sct211-0093/2022", 19, 2022,"15-09-2003", True)
# get_Student_Details(
#
#
#     "Odegi",
#     "sct211-0093/2022",
#     age=19,
#     dateofbirth="15-09-2003",
#     yearofstudy=2022
# )
# #default arguments...in the above code is_self_sponsi
# def print_number():
#     print(1)
#     print_number()
# print_number()
def factorial(num:int):
    if(num > 0):
        print(num)
        factorial(num-1)

factorial(5)
def factorial(num:int):
    if(num>1):
        return num*factorial(num-1)
    else:
        return 1
f=factorial(5)
print(f)

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
g=factorial(7)
print(g)