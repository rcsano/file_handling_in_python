# Add class
class LifeDiary:
    def __init__(self, output_file):
        # Instance variable
        self.output_file = output_file

    # Instance method and file handling (avoid manual closing of file)
    def write_to_life(self):
        with open(self.output_file, "w") as diary_file:

            # Use a loop
            while True:
                # Get input and write something
                entry_text = input("Enter line: ")
                diary_file.write(f"{entry_text}\n")

                # Added yes or no question
                choice = input("Would you like to write another line? (y/n): ")

                # Break loop if no
                if choice.lower() == "n":
                    break

        print(f"Entries saved to {self.output_file}")

# Instantiation
diary = LifeDiary("mylife.txt")

# Perform action
diary.write_to_life()
