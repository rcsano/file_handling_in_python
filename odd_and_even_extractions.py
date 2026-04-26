# Add class
class NumberSorter:
    def __init__(self, input_file):
        # State
        self.input_file = input_file
        self.even_file = "even.txt"
        self.odd_file = "odd.txt"

    # Open source and destination files
    def sort_numbers(self):
        # Behavior
        source = open("numbers.txt", "r")
        even_file = open("self.even_file", "w")
        odd_file = open("self.odd_file", "w")

    # Use a loop
        for line in source:
            # Remove whitespace and convert into integer
            number = int(line.strip())
            # Inserted conditional logic
            if number % 2 == 0:
                even_file.write(f"{number}\n")
            else:
                odd_file.write(f"{number}\n")

        # Close all opened files
        source.close()
        even_file.close()
        odd_file.close()
        print("Sorting successful.")

# Instantiation
sorter = NumberSorter("numbers.txt")
sorter.sort_numbers()