class Student:

    def __init__(self, name, surname, ID):
        self.ID = ID
        self.name = name
        self.surname = surname
        self.courses = []


    def addCourse(self, name):
        newCourse = Course(name)
        self.courses.append(newCourse)

    def addAssignment(self, coursename, name, deadline, grade = None):
        for course in self.courses:
            if course.name == coursename:
                course.addAssignment(name, deadline, grade)

    def Grade(self, coursename, assignmentname, grade):
        for course in self.courses:
            if course.name == coursename:
                for assignment in course.assignments:
                    if assignmentname == assignment.name:
                        assignment.Grade(grade)

    def getassignGrade(self, coursename, assignmentname, deadline):
        for course in self.courses:
            if course.name == coursename:
                for assignment in course.assignments:
                    if assignment.name == assignmentname:
                        print(assignment.grade)
                        return assignment.grade

    def getcourseGrade(self, coursename):
        for course in self.courses:
            if course.name == coursename:
                sum = 0
                for assignment in course.assignments:
                    sum = sum + self.getassignGrade(course.name, assignment.name, assignment.deadline)
                grade = sum/len(course.assignments)
                print(grade)
                return(grade)

    def getfullGrade(self):
        sum = 0
        for course in self.courses:
            sum = sum + self.getcourseGrade(course.name)
        grade = sum/len(self.courses)
        print(grade)

class Course:

    def __init__(self, name):
        self.name = name
        self.assignments = []

    def addAssignment(self, name, deadline, grade = None):
        newAssignment = Assignment(name, deadline, grade)
        self.assignments.append(newAssignment)

class Assignment:

    def __init__(self, name, deadline, grade = None):
        self.name = name
        self.deadline = deadline
        self.grade = grade

    def Grade(self, grade):
        self.grade = grade


def main():

    student = Student("Petros", "Petrosyan", "AUA789")
    student.addCourse("ENGS101")
    student.addAssignment("ENGS101", "HW1", "29.10.19")
    student.Grade("ENGS101", "HW1", 95)
    student.getassignGrade("ENGS101", "HW1", "29.10.19")
    student.getcourseGrade("ENGS101")
    student.getfullGrade()

main()

