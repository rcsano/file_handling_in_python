# Add class
class NumberSorter:
    def __init__(self, input_file):
        # Instance variables
        self.input_file = input_file
        self.even_file = "even.txt"
        self.odd_file = "odd.txt"

    # Instance method and file handling (avoid manual closing of files)
    def sort_numbers(self):
            with open(self.input_file, "r") as source, \
                 open(self.even_file, "w") as even_file, \
                 open(self.odd_file, "w") as odd_file:

                # Use a loop and exception handling
                for line in source:
                    # Remove whitespace and convert into integer
                    try:
                        number = int(line.strip())

                        # Inserted conditional logic
                        if number % 2 == 0:
                            even_file.write(f"{number}\n")
                        else:
                            odd_file.write(f"{number}\n")

                    except ValueError:
                        # Skip invalid lines
                        continue

            print("Sorting successful.")

# Instantiation
sorter = NumberSorter("numbers.txt")

# Perform action
sorter.sort_numbers()