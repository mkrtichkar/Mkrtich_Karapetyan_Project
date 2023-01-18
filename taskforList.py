list_int = [1, 2, 3, [4, 5, 6], [7, 8, 9, [10, 11, 12, [14, 15, 16]]]]
print(list_int)

list_string = str(list_int).replace('[', '').replace(']', '').replace(' ', '')
list_string = list_string.split(',')
print(list_string)

list_string = list(map(int, list_string))
print(list_string)

# list1 = list(list_string)
# print(list1)




# result = 0
# for i in range(len(list_int)):
#     result = isinstance(list_int[i], list)
#     if result == True:
#         print(list_int[i])
#     else:
#         continue
#
#
#
#
#
# print(list(map(str, list_int)))


