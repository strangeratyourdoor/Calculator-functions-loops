numbers=[15,10,7,6,90,12,8,76,207,34,76,109,345]
type(numbers)

def add():
    total=0
    for number in numbers:
        total=total+number
    print(total)
    return total
add()

def average():
    total = 0
    for number in numbers:
        total = total + number
    avg=total/len(numbers)
    print(avg)
    return avg
average()

def maximum():
    mx = numbers[0]
    for i in numbers:
        if i > mx:
            mx = i
    print('Maximum= ',mx)
maximum()

def minimum():
    mn = numbers[0]
    for i in numbers:
        if i < mn:
            mn = i
    print('Minimum= ',mn)
minimum()

print(pow(3,2)) #calculates 3 raised to 2
print(pow(9,0.5)) #calaculates the square root of 9
print(pow(8,1/3)) #calculates the cube root of 8


# print(type(numbers))...prints the type of object numbers is
# print(len(numbers))
#start parameter is not provided
# Sum=sum(numbers)
# print(Sum)
#start parameter is provided
# Sum=sum(numbers, 0)
# print(Sum)
# average=Sum/len(numbers)
# print(average)

    