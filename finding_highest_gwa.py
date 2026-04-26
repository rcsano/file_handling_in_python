# Add class
class GradeTracker:
    def __init__(self, record_file):
        # Instance Variables
        self.record_file = record_file
        self.highest_gwa = 5.0
        self.top_student = ""

# Instance Method
    def find_top_performer(self):
        students_record = open("students_record.txt", "r") # Reading
        # Loop process line and find to maximum GWA
        for line in students_record:
            # Use split assuming the format 'Name, GWA'
            name, score = line.strip().split(",")
            score = float(score)

            if score < self.highest_gwa:
                self.highest_gwa = score
                self.top_student = name

        # Output the result
        print(f"Student with the highest GWA: {self.top_student}, {self.highest_gwa}")

        # Close the opened file
        students_record.close()

# Instantiation
tracker = GradeTracker("students_record.txt")

# Perform Action
tracker.find_top_performer()
