print('Insert the coordinates of the cell in chess table...')
x = int(input('Row: '))
y = int(input('Column: '))
if (x+y) % 2 == 0:
    print("It's a black cell")
else:
    print("It's a white cell")
