# https://www.w3schools.com/python/python_for_loops.asp
#
# 1. Перемножить все не чётные значения в диапазоне от 9173 до 9435;
i = 9173
mult = 1
while i >= 9173 and i <= 9435:
    mult = mult * i
    i = i + 2
print(mult)

print('____________________________________________________')


# 2*. Print the following pattern
#     5 4 3 2 1
#     4 3 2 1
#     3 2 1
#     2 1
#     1

col = int(input('Please type one number: '))   # col = 5
while col >= 1:
    print(col, end=" ")
    row = col - 1
    while row >= 1:
        if row != 1:
            print(row, end=" ")
        else:
            print(row)
        row -= 1
    col -= 1


print('')
print('_____________________________________________')

# 3. Display numbers from -10 to -1 using for loop
i = -10
while i <= -1:
    print(i)
    i += 1

print('')
print('_____________________________________________')


# 4. Calculate the cube of all numbers from 1 to a given number from user
userNum = int(input('Please type one number: '))
i = 1
while i <= userNum:
    print('The cube of', i, 'is: ', i**3)
    i += 1

print('')
print('_____________________________________________')


# 5. Find the factorial of a given number
factorialNumFromUser = int(input('Please type number which you want to do factorial: '))

i = 1
fact = 1
while i <= factorialNumFromUser:
    fact = fact * i
    i += 1
print('The factorial for', factorialNumFromUser, 'is: ', fact)



