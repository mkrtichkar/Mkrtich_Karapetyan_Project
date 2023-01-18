# # while loop
#
# # number = 1
# # while number <= 20:
# #     print(number)
# #     number +=1
# #
#
#
# # useric tiv vercnel, tpel 0ic minchev ayd tiv@
#
# #
# # userAge = int(input("Please type your age"))
# #
# # for i in range(userAge+1):
# #     print(i)
# #
# # i = 0
# # while userAge >= i:
# #     print(i)
# #     i += 1
#
#
# # vor@ useric vercne 2 tiv u aranqi tver@ veradardzne
#
#
# userNum1 = int(input("please type one number: "))
# userNum2 = int(input("please type one number: "))
#
# if userNum1 > userNum2:
#     while userNum2 <= userNum1:
#         print(userNum2)
#         if userNum2 % 2 == 0:
#             print(userNum2)
#         userNum2 += 1
# elif userNum2 == userNum1:
#     print("there is no numbers")
# else:
#     while userNum1 <= userNum2:
#         print(userNum1)
#         if userNum1 % 2 == 0:
#             print(userNum1)
#         userNum1 += 1
#
# # print(myList)
# # for i in myList:
# #     if i % 2 == 0:
# #         print(i)
#


userStart = input("Please type a min number: ")
if type(userStart) == str:
    print(int(input("Please type integer: ")))
userEnd = int(input("PLease type a max number: "))
userStep = int(input("Please type a step: "))



while userEnd >= userStart:
    print(userStart)
    userStart = userStart + userStep


firstList = [1, 2, 2, 3, 3, 9, 45, 5000]
secondList = [2, 5, 2, 9, 10, 8, 45, 5000]
list3 = []

for i in firstList:
    if i in secondList:
        if i not in list3:
            list3.append(i)
print(list3)







































