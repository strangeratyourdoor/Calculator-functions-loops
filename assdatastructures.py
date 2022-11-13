math=int(input('Enter your Mathematics marks: '))
english=int(input('Enter your English marks: '))
kiswahili=int(input('Enter your Kiswahili marks: '))
chemistry=int(input('Enter your Chemistry marks: '))
biology=int(input('Enter your Biology marks: '))
physics=int(input('Enter your Physics marks: '))
geography=int(input('Enter your Geography marks: '))
comp_studies=int(input('Enter your Computer Studies marks: '))
subjects=[math,english,kiswahili,chemistry,biology,physics,geography,comp_studies]
total=0
for sub in subjects:
    total=total+sub
print(total)
avg=total//8
def grade (marks: int):
    if marks>80:
        score='A'
    elif marks>60:
        score='B'
    elif marks>40:
        score='C'
    elif marks>20:
        score='D'
    else:
        score='E'
    return score
print('Subject        Marks       Grade')
print(f'1               {math}           {grade(math)}')
print(f'2               {english}           {grade(english)}')
print(f'3               {kiswahili}           {grade(kiswahili)}')
print(f'4               {chemistry}           {grade(chemistry)}')
print(f'5               {biology}           {grade(biology)}')
print(f'6               {physics}           {grade(physics)}')
print(f'7               {geography}           {grade(geography)}')
print(f'8               {comp_studies}           {grade(comp_studies)}')

