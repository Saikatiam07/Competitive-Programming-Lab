a = [10, 20, 30, 40, 50]

key = int(input("Enter element to search: "))

low = 0
high = len(a) - 1
found = False

while low <= high:
    mid = (low + high) // 2

    if a[mid] == key:
        print("Element found at position", mid + 1)
        found = True
        break

    elif key < a[mid]:
        high = mid - 1

    else:
        low = mid + 1

if not found:
    print("Element not found")
    
    /*
    Output:
    Enter element to search: 30 
    Element found at position 3
    */
    