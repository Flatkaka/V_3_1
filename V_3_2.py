n = int(input("Enter the length of the sequence: ")) # Do not change this line
n1 = 1
n2 = 2
n3 = 3
count = 1
while count < n+1:
    summa = 0
    if count == 1:
        print(n1)
    elif count == 2:
        print(n2)
    elif count == 3:
        print( n3)
    else:
        summa = n1 + n2 + n3
        print(summa)
        n1 = n2
        n2 = n3
        n3 = summa
    count += 1