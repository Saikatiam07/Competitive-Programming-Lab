arr = [2, 7, 11, 15]
target = 9
seen = {}
for i in range(len(arr)):
    num = arr[i]
    diff = target - num
    if diff in seen:
        print("Indices:", seen[diff], i)
        break
    seen[num] = i
    
    #output:
    # Indices: 0 1  
    