# Add class
class GradeTracker:
    def __init__(self, record_file):
        # Instance variables
        self.record_file = record_file
        self.highest_gwa = 5.0
        self.top_student = ""

# Instance method and file handling (avoid manual closing of file)
    def find_top_performer(self):
        with open(self.record_file, "r") as students_record:

            # Loop process to find maximum GWA and exception handling
            for line in students_record:
                try:
                    # Remove whitespace and use split assuming into name and score
                    name, score = line.strip().split(",")
                    score = float(score)

                    # Conditional logic
                    if score < self.highest_gwa:
                        self.highest_gwa = score
                        self.top_student = name

                except ValueError:
                    # Skip invalid lines
                    continue

        # Output the result
        print(f"Student with the highest GWA: {self.top_student}, {self.highest_gwa}")

# Instantiation
tracker = GradeTracker("students_record.txt")

# Perform action
tracker.find_top_performer()
