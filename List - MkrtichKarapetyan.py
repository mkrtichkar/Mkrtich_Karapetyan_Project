# https://www.w3schools.com/python/python_lists.asp
#
# 01. Write a program to print odd index elements in a list
# 02. Write a program to get the largest number from a list
# 03. Write a program to remove duplicates from a list
# 04. Write a program to convert a string to a list
# 05. Write a program to find the item with maximum occurrences in a given list
# 06. Write a program to check whether a specified list is sorted or not

# 01. Write a program to print odd index elements in a list
myList = [1, 5, 8, 1, 45, 789, 0, 0, 13, 45, 65, 35, 1, 222]
print(myList[1::2])
print('_____________________________________________________')


# 02. Write a program to get the largest number from a list
myList = [1, 5, 8, 1, 45, 789, 0, 0, 13, 45, 65, 35, 1, 222]
myList.sort()
print(myList[-1])
print('_____________________________________________________')


# 03. Write a program to remove duplicates from a list
myList = [1, 5, 8, 1, 45, 789, 0, 0, 13, 45, 65, 35, 1, 222]
myListWithoutDuplicates = set(myList)
myList = list(myListWithoutDuplicates)
print(myList)
print('_____________________________________________________')


# 04. Write a program to convert a string to a list
myWord = 'lifeisgood'

myWord = list(myWord)
print(myWord)
print('_____________________________________________________')


# 05. Write a program to find the item with maximum occurrences in a given list

myList = [1, 5, 8, 1, 34, 34, 34, 34]

maxOccur = max(myList, key=myList.count)

print(maxOccur)
print('_____________________________________________________')


# 06. Write a program to check whether a specified list is sorted or not

# myList = [1, 0, 65, 35, 5, 8, 45, 13, 789, 222]

myList = [99, 98, 97]
sortList = myList.copy()
myList.sort()

if myList == sortList:
    print(True)
else:
    print(False)





# Tak_7
print("_______________________________________________")

varFalse = ['year', 'new', 'Merry', 'and', 'Happy', 'Christmas']


