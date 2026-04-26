# Open source file integers.txt
def process_integers():
    source = open("integers.txt", "r") #Reading
    double_file = open("double.txt", "w") #Writing
    triple_file = open("triple.txt", "w") #Writing

    # Use a loop
    for line in source:
        # Remove whitespace and convert into integer
        number = int(line.strip())
        # Conditional logic
        if number % 2 == 0:
            double_file.write(str(number ** 2) + "\n") # Square for even
        else:
            triple_file.write(str(number ** 3) + "\n") # Cube for odd

    # Close all opened files
    source.close()
    double_file.close()
    triple_file.close()

# Process
process_integers()