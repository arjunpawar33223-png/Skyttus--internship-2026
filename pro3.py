class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks  # List of marks

    def average_marks(self):
        avg = sum(self.marks) / len(self.marks)
        print(f"{self.name}'s average marks: {avg:.2f}")

# Example
student = Student("Arjun", [80, 90, 70])
student.average_marks()