# https://www.w3schools.com/python/python_lists.asp
# https://www.w3schools.com/python/python_tuples.asp
# https://www.w3schools.com/python/python_sets.asp
# https://www.w3schools.com/python/python_dictionaries.asp
#
# 1. Write a Python program to get the largest number from a list.
# 2. Write a Python program to check a list is empty or not.
# 3. Write a Python program to remove all elements from a given set.
# 4. Write a Python program to check if a given value is present in a set or not.
# 5. Write a Python program to convert a list to a tuple.
# 6. Write a Python program to remove an item from a tuple.
# 7. Write a Python script to check whether a given key already exists in a dictionary or not.
# 8. Write a Python script to merge two Python dictionaries.

def toSecondTask():
    print('                                                ')
    print('___  ___  ___  ___  ___  ___  ___  ___  ___  ___')
    print('                                                ')

# Task_1
print('Write a Python program to get the largest number from a list.')
myList = [1, 9, 38, 3, 0]
myList.sort(reverse=True)
print(myList)
print('The largest number from myList is: ', myList[0])
toSecondTask()


# Task_2
print('Write a Python program to check a list is empty or not.')
myList = [1, 9, 38, 3, 0]
if len(myList) == 0:
    print('myList is empty')
else:
    print('myList is not empty')
toSecondTask()


# Task_3
print('Write a Python program to remove all elements from a given set.')
mySet = {3, 76, 99, 3}
mySet.clear()
print(mySet)
toSecondTask()

# Task_4
print('Write a Python program to check if a given value is present in a set or not.')
mySet = {3, 76, 99}
userAge = int(input('Please input your age: '))
if userAge in mySet:
    print('User age is:', userAge, 'and there is in mySet')
else:
    print('User age is:', userAge, 'and there is not in mySet')

input('Please tap Enter for continue')
toSecondTask()


# Task_5
print('Write a Python program to convert a list to a tuple.')
myList = [1, 9, 38, 3, 0]
myTuple = tuple(myList)
print(myTuple)
toSecondTask()


# Task_6
print('Write a Python program to remove an item from a tuple.')
myTuple = (1, 9, 38, 3, 0)
myTuple = list(myTuple)
myTuple.pop(-1)
myTuple = tuple(myTuple)
print(myTuple)
toSecondTask()


# Task_7
print('Write a Python script to check whether a given key already exists in a dictionary or not.')
myDict = {'name': ['Mkrtich', 'Vardan', 'Hayk'],
          'surname': ['Karapetyan', 'Martirosyan', 'Davtyan'],
          'age': [24, 24, 25]
          }
print(myDict)
userKey = str(input('Please type your key: '))
if userKey in myDict:
    print('User key is present in the myDict')
else:
    print('User key is not present in the myDict')

input('Please tap Enter for continue')
toSecondTask()


# Task_8
print('Write a Python script to merge two Python dictionaries.')
myNameDict = {'name': ['Mkrtich', 'Vardan', 'Hayk']}
myAgeDict = {'age': [24, 24, 25]}
# myMergeDict = myNameDict | myAgeDict
# print(myMergeDict)

myNameDict.update(myAgeDict)
print(myNameDict)





