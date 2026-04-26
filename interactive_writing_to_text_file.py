# Add class
class LifeDiary:
    def __init__(self, output_file):
        # Instance Variable
        self.output_file = output_file

    # Connect and open file
    def write_to_life(self):
        my_life = open("self.output_file", "w") #Writing

        # While loop
        while True:
            # Get input and write something
            line = input("Enter line: ")
            my_life.write(f"{line}\n")

            # Added yes or no question
            choice = input("Would you like to write another line? (y/n): ")
            # Break loop if no
            if choice.lower() == "n":
                break

        # Close the file only if the loop if finished
        my_life.close()

        print(f"Entries saved to {self.output_file}")

# Instantiation
diary = LifeDiary("mylife.txt")
diary.write_to_life()