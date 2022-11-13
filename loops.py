for index in range(100):
    print("odegi")
    print(index)
while True:
    number=input("Enter any integer ")
    num1=int(number)
    if num1<0:
        break
    if num1%2==0:
        print(f"Number {num1} is even")
    else:
        print(f"Number {num1} is odd")

math=input('enter marks for math ')
computer=input("Computer ")
physics=input('Physics ')
sum=int(math)+int(computer)+int(physics)
average=int(sum)/2
print(f"math= {math}")
print(f'Computer= {computer}')
print(f'Physics= {physics}')
print(f'Average= {average}')
if average>70:
    print('Distinction')
elif average>60:
    print('Credit')
elif average>40:
    print('pass')
else:
    print('fail')








