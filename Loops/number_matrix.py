
# NUMBER MATRIX

rows = int(input('number of rows: '))
cols = int(input('number of cols: '))

for i in range(1, rows+1):
    for j in range(cols):
        print(f'{i}{j+1}', end=' ')
    print()