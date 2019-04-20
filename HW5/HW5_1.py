#variables
#==========================================
matrix1 =  [['■','□','□','□','□'],
            ['□','□','■','□','□'],
            ['□','□','□','□','■'],
            ['□','■','□','□','□'],
            ['□','□','□','■','□']
            ]
matrix2 =  [['■','□','□','□','□'],
            ['□','□','□','■','□'],
            ['□','■','□','□','□'],
            ['□','□','□','□','■'],
            ['□','□','■','□','□']
            ]


#main function
#==========================================
print("Pattern 1")
for i in range(0, 5):
    for j in range(i, i+5):
        for k in range(0, 5):
            print(matrix1[j%5][k], end='')
            print(" ", end='')
        print(" ", end=' ')
    print()#'換行'
print()#'換行'
print("Pattern 2")
for i in range(0, 5):
    for j in range(i, i+5):
        for k in range(0, 5):
            print(matrix2[j%5][k], end='')
            print(" ", end='')
        print(" ", end=' ')
    print()#'換行'

