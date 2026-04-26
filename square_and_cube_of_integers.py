# Added Class
class MathProcessor:
    def __init__(self, input_file):
        # Instance Variables
        self.input_file = input_file
        self.double_file = "double.txt"
        self.triple_file = "triple.txt"

    # Instance Method
    def calculate_results(self):
        source = open(self.input_file, "r")
        double_file = open(self.double_file, "w")
        triple_file = open(self.triple_file, "w")

        # Use a loop
        for line in source:
            # Remove whitespace and convert into integer
            number = int(line.strip())

            # Conditional logic
            if number % 2 == 0:
                # Square for even
                double_file.write(f"{number ** 2}\n")
            else:
                # Cube for odd
                triple_file.write(f"{number ** 3}\n")

        # Close all opened files
        source.close()
        double_file.close()
        triple_file.close()

# Instantiation
processor = MathProcessor("integers.txt")

# Perform action
processor.calculate_results()