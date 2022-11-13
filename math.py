# contains static methods
import math

p = math.sqrt(25)
print(p)



class Numbers:
    x = 15
    z = 81
    y = 27

    def sum(self,num1,num2,num3):
        s = num1+num2+num3
        avg = s / 3
        print(f'Sum= {s}')
        print(f'Average= {avg}')

    def max(self,num1,num2,num3):
        if num1 > num2:
            if num1 > num3:
                print(f'Max={num1}')
            else:
                print(f'Max={num3}')
        else:
            if num2 > num3:
                print(f'Max={num2}')

    def min(self, num1,num2,num3):
        if num1 < num3:
            if num1 < num2:
                print(f'Min={num1}')
            else:
                print(f'Min={num2}')
        else:
            if num3 < num2:
                print(f'Min={num3}')

no=Numbers()
no.sum(15,81,27)
no.max(15,81,27)
no.min(15,81,27)



