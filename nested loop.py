for i in range(5):
    for j in range(5):
        print(j, end=" ")
    print()
for j in range(5):
    print(j, end=" ""\n")
for i in range(5):
    for j in range(1, i + 2):
        print(j, end=" ")
    print()
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
for i in range(4):
    for j in range(4):
        if i == 0 or i == 3:
            print(j, end=" ")
        else:
            if j == i:
                print(j, end=" ")
            else:
                print(" ", end=" ")
    print()
for i in range(4):
    for j in range(4):
        if i == 0 or i == 3:
            print("*",end=" ")
        else :
            if j == i:
                print("*",end=" ")
            else:
                print("$", end=" ")
    print()
for i in range(4):
    for j in range(4):
        if i == 0 or i == 3:
            print("*",end=" ")
        else:
            if j==i+1 and j<3:
                print("*", end=" ")
            else:
                if j==i-1 and j>0:
                    print("*", end=" ")
                else:
                    print("&", end=" ")
    print()
for i in range (5,10):
    for j in range (i,i-5,-1):
        if j<=5:
            print(j, end=" ")
        else:
            print(" ",end=" ")
    print()
