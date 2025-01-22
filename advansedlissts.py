lhgzroaj=[19,84,3009,2025,1125,729]
print(lhgzroaj[5])
for i in range(len(lhgzroaj)):
    lhgzroaj[i]+=10
print(lhgzroaj)

#2D List

matrix=[[1,2,3,3],[4,5,6,3],[7,8,9,3]]
print(len(matrix))
print(len(matrix[1]))
for i in matrix:
    print(i)
for i in range(len(matrix)):
    for j in range(len(matrix[1])):
        print(matrix[i][j],end=" ")
    print("\n")