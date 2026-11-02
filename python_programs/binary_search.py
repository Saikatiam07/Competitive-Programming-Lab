arr = [90, 80, 70, 60, 50, 40, 30]
target = 60
low = 0
high = len(arr) - 1
result = -1
while low <= high:
    mid = (low + high) // 2
    if arr[mid] == target:
        result = mid
        break
    elif arr[mid] < target:
        high = mid - 1
    else:
        low = mid + 1
print("Element found at index:", result)

#output:
# Element found at index: 3 
