# Open source and destination files
input_file = open("numbers.txt", "r") #Reading
even_file = open("even.txt", "w") #Writing
odd_file = open("odd.txt", "w") #Writing

# Use a loop
for line in input_file:
    # Remove whitespace and convert into integer
    number = int(line.strip())
    print(number)

# Close all opened files
input_file.close()
even_file.close()
odd_file.close()