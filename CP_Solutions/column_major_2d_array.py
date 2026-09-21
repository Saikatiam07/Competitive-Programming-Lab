a = [
    [1, 2, 3],
    [4, 5, 6]
]

print("Column Major Order:")

for j in range(3):
    for i in range(2):
        print(a[i][j], end=" ")
        
 /*
Output:
    Column Major Order:
1 4 2 5 3 6
*/