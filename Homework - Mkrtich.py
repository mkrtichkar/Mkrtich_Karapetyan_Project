maxRow = int(input('Please type number: '))
for i in range(maxRow + 1):
    for j in range(i):
        print('* ', end="")
    print('')

print()

# maxRow2 = int(input('Please type number: '))
for i in range(maxRow,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')


print()


for i in range(maxRow):
    for j in range(maxRow - i):
        print(' ', end="")
    print('*')

