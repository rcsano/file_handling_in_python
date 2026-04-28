# Added Class
class MathProcessor:
    def __init__(self, input_file):
        # Instance Variables
        self.input_file = input_file
        self.double_file = "double.txt"
        self.triple_file = "triple.txt"

    # Instance Method and file handling (avoid manual closing of files)
    def calculate_results(self):
        with open(self.input_file, "r") as source, \
             open(self.double_file, "w") as double_file, \
             open(self.triple_file, "w") as triple_file:

            # Use a loop and exception handling
            for line in source:
                # Remove whitespace and convert into integer
                try:
                    number = int(line.strip())

                    # Conditional logic
                    if number % 2 == 0:
                        # Square for even
                        double_file.write(f"{number ** 2}\n")
                    else:
                        # Cube for odd
                        triple_file.write(f"{number ** 3}\n")
                except ValueError:
                    # Skip invalid lines
                    continue

# Instantiation
processor = MathProcessor("integers.txt")

# Perform action
processor.calculate_results()
