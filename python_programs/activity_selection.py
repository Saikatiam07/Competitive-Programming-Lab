start = [1, 3, 0, 5, 8, 5]
finish = [2, 4, 6, 7, 9, 9]
activities = []
for i in range(len(start)):
    activities.append((start[i], finish[i]))
activities.sort(key=lambda x: x[1])
selected = []
last_finish = -1
for activity in activities:
    if activity[0] >= last_finish:
        selected.append(activity)
        last_finish = activity[1]
print("Selected activities:", selected)
print("Maximum activities:", len(selected))

#output:
# Selected activities: [(1, 2), (3, 4), (5, 6), (8, 9)]
# Maximum activities: 4