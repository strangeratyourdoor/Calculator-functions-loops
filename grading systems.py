print("+-----------------------------------+")
print("|          Grading System           |")
print("+-----------------------------------+")
# english = int(input("Enter your English marks: "))
# maths = int(input("Enter your Maths marks: "))
# science = int(input("Enter your Science marks: "))
english = 50
maths = 80
science = 20
total = english + maths + science
avg = total // 3


def grade(marks: int):
    if marks >= 80:
        score = "A"
    elif marks >= 60:
        score = "B"
    elif marks > 40:
        score = "C"
    else:
        score = "D"
    return score


g = grade(english)
f = grade(maths)
k = grade(science)
m = grade(total)
print("+-----------------------------------+")
print("|    Subject    |  Marks  |  Grade  |")
print("+-----------------------------------+")


def average():
    if avg > 80:
        grade1 = "A"
    elif avg >= 60:
        grade1 = "B"
    elif avg >= 40:
        grade1 = "C"
    elif avg > 20:
        grade1 = "D"
    else:
        grade1 = "E"
    return grade1


t = average()

# avgrade=grade1
print(f"|    English         {english}        {g}    |")
print("+-----------------------------------+")
print(f"|    Maths           {maths}        {f}    |")
print("+-----------------------------------+")
print(f"|    Science         {science}        {k}    |")
print("+-----------------------------------+")
print(f"|    Average         {avg}         {t}   |")
print("+-----------------------------------+")
print(f"|    Total Marks              {total}   |")
print("+-----------------------------------+")
