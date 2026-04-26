# Connect and open file
def write_to_life():
    my_life = open("mylife.txt", "w") #Writing

    # While loop
    while True:
        # Get input and write something
        line = input("Enter line: ")
        my_life.write(line + "\n")

        # Added yes or no question
        choice = input("Would you like to write another line? (y/n): ")

        # Break loop if no
        if choice == "n":
            break

    # Close the file only if the loop if finished
    my_life.close()

# Execute
write_to_life()