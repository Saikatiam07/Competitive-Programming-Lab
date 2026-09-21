a = [
    [1, 2, 3],
    [4, 5, 6]
]

print("Row Major Order in Binary:")

for row in a:
    for value in row:
        print(format(value, "08b"), end=" ")
        
  */
  Output:
 Row Major Order in Binary:
00000001 00000010 00000011 00000100 00000101 00000110
*/