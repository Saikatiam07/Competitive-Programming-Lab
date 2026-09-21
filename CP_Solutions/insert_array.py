a = [10, 20, 30, 40, 50]
element = int(input("Enter element: "))
position = int(input("Enter position: "))
a.insert(position - 1, element)
print("Array after insertion:", a)

/*
Output:
 Enter element: 25
Enter position: 3
Array after insertion: [10, 20, 25, 30, 40, 50]
*/