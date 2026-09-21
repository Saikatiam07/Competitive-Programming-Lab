a = [10, 20, 30, 40, 50]
position = int(input("Enter position to delete: "))
a.pop(position - 1)
print("Array after deletion:", a)

/*
Output:
 Enter position to delete: 3 
Array after deletion: [10, 20, 40, 50]
*/    