# https://www.w3schools.com/python/python_while_loops.asp
#
# 1. Write a program to construct the following pattern.
#       *
#       * *
#       * * *
#       * * * *
#       * * * * *
#       * * * *
#       * * *
#       * *
#       *
maxRow = 5
for i in range(maxRow):
    for j in range(i):
        print('* ', end="")
    print('')

for i in range(maxRow,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')

print('____________________________________________________')


# 2. Write a program to create the multiplication table (from 1 to 10) of a number.
#       Input a number: 6
#       6 x 1 = 6
#       6 x 2 = 12
#       6 x 3 = 18
#       6 x 4 = 24
#       6 x 5 = 30
#       6 x 6 = 36
#       6 x 7 = 42
#       6 x 8 = 48
#       6 x 9 = 54
#       6 x 10 = 60
userInp = int(input("Please type one number: "))    # userInpute == 6
for i in range(1, 11):
    mult = userInp * i
    print(userInp, '*', i, '=', mult)

print('____________________________________________________')

# 3. Write a program to print alphabet pattern 'O'
#    Expected Output:
#          *
#        *   *
#        *   *
#        *   *
#        *   *
#        *   *
#          *

symbol = '*'
for col in range(7):
    if col == 0 or col == 6:
        print(' ', symbol)
    elif col > 0 and col != 6:
        print(symbol, ' ', symbol)

print('____________________________________________________')


# 4. Calculate the sum of all numbers from 1 to a given number from user
userNum = int(input('Please type one number: '))
sum = 0
for i in range(1, (userNum + 1)):
    sum = sum + i

print(sum)
print('____________________________________________________')


# 5. Write a program to check whether a specified list is sorted or not
myList = [5, 4, 1]
if myList == sorted(myList) or myList == sorted(myList, reverse=True):
    print(myList, 'list is sorted')
else:
    print(myList, 'list is not sorted')
