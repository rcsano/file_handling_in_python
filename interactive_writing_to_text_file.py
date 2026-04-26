# Connect and open file
def write_to_life():
    my_file = open("mylife.txt", "w") #Writing

# Get input and write something
    line = input("Enter line: ")
    my_file.write(line + "\n")

# Close file
    my_file.close()

# Execute
write_to_life()