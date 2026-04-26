# Open the student's record file
myFile = open("students_record.txt", "r") # Reading

highest = 0
best = ""

# Loop process line and find to maximum GWA
for line in myFile:
    # Use split assuming the format 'Name,GWA'
    data = line.strip().split(",")
    # Added float for math comparison
    name = data[0]
    score = float(data[1])

    if score > highest:
        highest_student = name
        highest_gwa = score

# Output the result
print(f"Student with the highest GWA: {highest_student}, {highest_gwa}")

# Close the opened file
myFile.close()
