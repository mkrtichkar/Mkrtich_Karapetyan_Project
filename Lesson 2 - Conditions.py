# 1*. Write a Python program that accepts a word from the user and reverse it.
# 2. Write a Python program to count that user inputed number is even or odd.
# 3. Write a Python program to find the inputed number from 100 to 400 (both included).
# 4. Write a Python program that get 2 numbers from user and retur Biggest, Median, Sum, Multiply, Divide and Subtract
# 5. Write a Python program to get next day of a given date.
# 	Expected Output:
#
# 	Input a year: 2016
# 	Input a month [1-12]: 8
# 	Input a day [1-31]: 23
# 	The next date is [yyyy-mm-dd] 2016-8-24

# task_1
yourName = str(input("Please type your name: "))
# nameResult = isinstance(yourName, str)
yourNameReverse = yourName[::-1]

print(yourName)
print(yourNameReverse)


# task_2
userAge = int(input("Please type your age: "))
if userAge % 2 == 0:
    print("Your age is even")
else:
    print('Your age is odd')

# task_3
userLuckyNumber = int(input("Please type your lucky number: "))
if userLuckyNumber >= 100 and userLuckyNumber <= 400:
    print(True)
else:
    print(False)


# Task_4
num1 = int(input("Please type any number: "))
num2 = int(input("Please type any number: "))

if num1 > num2:
    print('The biggest number is: ', num1)
    print('The median number is: ', (num1 - num2) / 2 + num2)
elif num1 == num2:
    print(num1, 'the equal to ', num2)
    print('There is no median number')
else:
    print('The biggest number is: ', num2)
    print('The median number is: ', (num2 - num1) / 2 + num1)

print('The sum is: ', num1 + num2, '\nThe multiple is: ', num1*num2, '\nThe subtract is: ', num1 - num2 )

if num2 != 0:
    print('The divide is: ', num1 / num2)
else:
    print('The divide is not possible')


# Task_5
# year = int(input("Please type any year  [1974 - ]: "))
# month = int(input("Please type month with number: "))
# day = int(input("Please type day: [1 - 31]"))






