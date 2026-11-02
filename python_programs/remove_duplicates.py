arr = [1, 2, 3, 2, 4, 1, 5]
seen = set()
result = []
for num in arr:
    if num not in seen:
        result.append(num)
        seen.add(num)
print("List after removing duplicates:", result)

#output:
# List after removing duplicates: [1, 2, 3, 4, 5]   