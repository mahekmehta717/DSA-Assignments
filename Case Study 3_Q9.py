attendance = [11, 12, 13, 14, 15]

# 1. Display the attendance list
print("Attendance List:")
for roll in attendance:
    print(roll, end=" → ")

# 2. Delete Roll Number 15
attendance.remove(15)

# 3. Display the updated list
print("\n\nUpdated Attendance List:")
for roll in attendance:
    print(roll, end=" → ")

# 4. Which node's next pointer changes?
print("\n\nNode whose next pointer changes: Roll Number 14")
