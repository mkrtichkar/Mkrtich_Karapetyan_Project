
def sequence1(num: int):
    for i in range(num + 1):
        print(i)



def sequence2():
    num = int(input("Please type sequence number: "))
    for i in range(num + 1):
        print(i, end=" ")
    print()


def duplicates(myList: list):
    for i in range(0, len(myList)):
        for j in range(i + 1, len(myList)):
            if (myList[i] == myList[j]):
                print(myList[j])

sequence1(5)
sequence2()
duplicates([1, 6, 7, 1, 7])