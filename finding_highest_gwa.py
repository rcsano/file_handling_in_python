# Open the student's record file
myFile = open("studentsrecord.txt", "r") # Reading

# Loop process line and find to maximum GWA
for line in myFile:
    # Use split assuming the format 'Name,GWA'
    data = line.strip().split(",")

# Output the result
print(data)

# Close the opened file
myFile.close()