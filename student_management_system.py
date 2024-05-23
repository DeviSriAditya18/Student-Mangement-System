class Student:
    student_dictionary={}
    school_name='XYZ'

    def __init__(self):
        self.roll_no=input("\nEnter the Student Roll Number: ")
        self.name=input("\nEnter the Student Name: ")
        self.phone_number=input("\nEnter the Student Phone Number: ")
        self.address=input("\nEnter the Student Address: ")
        student_class=input("\nEnter the Student Class: ")

        if student_class in StudentClass.classes:
            StudentClass.classes[student_class].studentList.append(self)
        else:
            new_class=StudentClass(student_class)
            new_class.studentList.append(self)
            StudentClass.classes[student_class]=new_class

        self.student_class=StudentClass.classes[student_class]

        print("Student Added Successfully")
        self.getStudent()

    def getStudent(self):
        print("\n---Student Details---\n")
        print("\tRoll Number: ",self.roll_no)
        print("\tName: ",self.name)
        print("\tPhone Number: ",self.phone_number)
        print("\tAddress: ",self.address)
        print("\tClass: ",self.student_class.name)
        print("\tSchool Name: XYZ")

    def updateStudent(self):
        print("\t\tSelect option to update student details\n")
        print("\t\t\t1)To change student name")
        print("\t\t\t1)To change student phone number")
        print("\t\t\t1)To change student address")
        print("\t\t\t1)To change student class")
        option = input("Enter Any of the Above Given Options: ")
        print()

        if option in ['1','2','3','4']:
            if option=='1':
                self.name = input("\t\t\tEnter the student new name: ")
                print("\n\t\tStudent name changed successfully")
            elif option=='2':
                self.phone_number = input("\t\t\tEnter the student new phone number: ")
                print("\n\t\tStudent phone number changed successfully")
            elif option=='3':
                self.address = input("\t\t\tEnter the student new address: ")
                print("\n\t\tStudent address changed successfully")
            else:
                new_class = input("\t\t\tEnter the student new class: ")
                slef.student_class.studentList.remove(self)
                try:
                    self.student_class=StudentClass.classes[new_class]
                    self.student_class.studentList.append(self)
                except:
                    addClass=StudentClass(new_class)
                    self.student_class=addClass
                    addClass.studentList.append(self)

                print("\n\t\tStudent class changed successfully")
        else:
            print("\n\t\t\tYou have chosen wrong option...")

    @classmethod
    def updateSchoolName(cls,new_school_name):
        cls.school_name=new_school_name

    @classmethod
    def getTotalStudentCount(cls):
        return len(cls.student_dictionary)

class StudentClass:
    classes={}
    def __init__(self,name):
        self.name=name
        StudentClass.classes[name]=self
        self.studentList=[]



def main():
    print(f"---Welcome to {Student.school_name} School---\n")
    print("\t1) To Get Student Details")
    print("\t2) To Add New Student")
    print("\t3) To Remove Student")
    print("\t4) To Update Student Details")
    print("\t5) To Update School Name")
    print("\t6) To Get Number of Students in School")
    print("\t7) To Get All Student Details")
    print("\t8) To Get Any Class Student Details")

    option=input("Enter Any of the Above Given Options: ")
    print()

    if option=='1':
        roll_no=input("\nEnter the Student Roll Number: ")
        try:
            Student.student_dictionary[roll_no].getStudent()
        except:
            print("\nYou have entered Wrong Roll Number...")

    elif option=='2':
        new_student=Student()
        Student.student_dictionary[new_student.roll_no]=new_student

    elif option=='3':
        roll_no = input("\nEnter the Student Roll Number: ")
        try:
            student=Student.student_dictionary.pop(roll_no)
            student.student_class.studentList.remove(student)
            print("\t\t",roll_no,"Student Deleted Successfully")
        except:
            print("\t\tNo Student there to delete")

    elif option=='4':
        roll_no=input("\nEnter the Student Roll Number: ")
        print()
        try:
            Student.student_dictionary[roll_no].updateStudent()
        except:
            print("\n\t\tYou have entered the wrong roll number...")
    elif option=='5':
        new_school_name=input("Enter the new school name: ")
        Student.updateSchoolName(new_school_name)
        print("School name changed successfully")

    elif option=='6':
        print("Total number of students in school: ",Student.getTotalStudentCount())
    elif option=='7':
        if Student.student_dictionary:
            print("Total number of students in school: ",Student.getTotalStudentCount())
            print("\nTotal Student list with details-->")
            for sNo,student in enumerate(Student.student_dictionary.values()):
                print("Student-",sNo+1)
                student.getStudent()
                print()
        else:
            print("No Students found")
    elif option=='8':
        try:
            students = StudentClass.classes[input("Enter the class name: ")]
            print("\nStudents of class-", students.name)
            print(f"\nTotal number of students in class {students.name}: {len(students.studentList)}")
            print()
            for sNo, student in enumerate(students.studentList):
                print("Student-", sNo + 1)
                student.getStudent()
                print()
        except:
            print("\nYou entered wrong class name or no students there...")

if __name__ == "__main__":
    option='y'
    while option=='y':
        main()
        option=input("Do u want to continue [y/n]?: ")
        print()

