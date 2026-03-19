array = [1, 4, 2, 8, "G"]
array2 = [6, False, "W", 4.1]

array2d = [array, array2]
print(array2d)
for i in range(len(array2d)):
    for j in range(len(array2d[i])):
        print(array2d[i][j])