

1, -1, 0 

1, 1, 0
-1, -1, 0

matrix = [
            [1,0,1],
            [0,1,1],
            [1,1,0]
        ]

# print(matrix[1][1])

# matrix[1][1] =  3


nextStep = []

for row in range(len(matrix)):
    rowCount = 0
    lastSeenZeroCol = 0
    for col, val in enumerate(matrix[row]):
        rowCount = rowCount + val
        if val == 0:
            lastSeenZeroCol = col
    
    if abs(rowCount) == 3:
        print ("Lose")
    if abs(rowCount) == 2:
        nextStep = [row, lastSeenZeroCol]

    print(nextStep)
