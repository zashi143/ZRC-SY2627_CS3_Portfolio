class AssignmentSubmission:
    def __init__(self, student_name, student_id, assignment_title, due_date):
        self.student_name = student_name
        self.student_id = student_id
        self._assignment_title = assignment_title
        self._due_date = due_date
        self.__is_submitted = False
        self.__grade = 0.00
        self.___submitted_files = [""]

    def __validate_grade(self, grade):
        if isinstance(grade, (int, float)) and 0 <= grade <= 100:
            return True
        else:
            raise ValueError("Grade must be a number between 0 and 100.")

    def __check_submission_status(self):
        return self.__is_submitted

    def __is_duplicate(self): 
        if self.___submitted_files is None:
            return False        
        if len(self.___submitted_files) != len(set(self.___submitted_files)):
            return True

    def add_file(self, file_name):
        if self.___submitted_files is None:
            self.___submitted_files = []
        if file_name not in self.___submitted_files:
            self.___submitted_files.append(file_name)
        

    def remove_file(self, file_name):
        if self.___submitted_files is None or file_name not in self.___submitted_files:
            raise ValueError("File not found in submitted files.")
        self.___submitted_files.remove(file_name)

    def assign_grade(self, grade):
        if self.__validate_grade(grade):
            self.__grade = float(grade)

    def get_grade(self):
        return self.__grade

    def view_files(self):
        return self.___submitted_files

    def get_status_report(self):
        status = "Submitted" 
        if self.__check_submission_status(): 
            status = "Submitted"
        else:
            status = "Not Submitted"
        return f"Student: {self.student_name}, ID: {self.student_id}, Assignment: {self._assignment_title}, Due Date: {self._due_date}, Status: {status}, Grade: {self.__grade}"

student1 = AssignmentSubmission("Alex Gonzaga", "pshs-1090-x", "CS-101", "2026-10-01")
student2 = AssignmentSubmission("Adelle", "pshs-1920-x", "CS-103", "2026-10-01")

print("---INITIALIZING DROPBOX FOR STUDENTS---")
student1 = AssignmentSubmission(student_name="Alex Gonzaga", student_id="pshs-1090-x", assignment_title="CS-101", due_date="2026-10-01")
student2 = AssignmentSubmission(student_name="Adelle", student_id="pshs-1920-x", assignment_title="CS-103", due_date="2026-10-01")
student3 = AssignmentSubmission(student_name="Juan dela Cruz", student_id="pshs-1033-x", assignment_title="CS-101", due_date="2026-10-01")
student4 = AssignmentSubmission(student_name="Maria Santos", student_id="pshs-1044-x", assignment_title="CS-101", due_date="2026-10-01")
student5 = AssignmentSubmission(student_name="Jose Reyes", student_id="pshs-1055-x", assignment_title="CS-101", due_date="2026-10-01")
print()

print("---TEST SCENARIO 1: Multiple Files via List---")
student1.add_file("main.py")
student1.add_file("report.pdf")
student1.assign_grade(95)
print(f"Alex's Files: {student1.view_files()}\n")

print("---TEST SCENARIO 2: Removing Files from List---")
student2.add_file("wrong_homework.docx")
student2.remove_file("wrong_homework.docx")
student2.add_file("correct_project.py")
student2.assign_grade(88)
print(f"Adelle's Files: {student2.view_files()}\n")

print("---TEST SCENARIO 3:Preventing Duplicate Files---")
student3.add_file("script.py")
student3.add_file("script.py")
print(f"Juan's Files: {student3.view_files()}\n")

print("--- TEST SCENARIO 4: Removing file after being graded ---")
student4.add_file("exam_answers.pdf")
student4.assign_grade(75)
student4.remove_file("exam_answers.pdf")
print()

print("--- TEST SCENARIO 5: Empty List Handling ---")
student5.add_file("draft.txt")
student5.remove_file("draft.txt")
student5.assign_grade(100)
print()

print("--- FINAL SYSTEM REPORT ---")
print(student1.get_status_report())
print(student2.get_status_report())
print(student3.get_status_report())
print(student4.get_status_report())
print(student5.get_status_report()) 
