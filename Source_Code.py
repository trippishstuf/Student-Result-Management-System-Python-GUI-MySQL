from tkinter import *
from PIL import ImageTk, Image
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost", user="root", password="Aarushi1505", database="student")
mycursor = mydb.cursor()

def main():
    root.destroy()
    choice = int(input("\nEnter the choice entered in GUI: "))
    print("\n")

    if(choice == 1):
        print("1. Create a new student record with valid data")
        print("2. Display an existing student record")
        print("3. Update an existing student record with new data")
        print("4. Delete an existing student record")
        c = int(input("\nEnter your choice: "))
        if(c == 1):
            roll_no = int(input("Roll no:"))
            name = input("Enter the name:")
            q1 = "insert into marks(Roll_no,Name) values({},'{}')".format(
                roll_no, name)
            mycursor.execute(q1)
            mydb.commit()
            print("New student record has been created")

        elif(c == 2):
            roll_no = int(input("Roll no:"))
            print("The required student records are: ")
            q1 = "select* from marks where Roll_No=1"
            mycursor.execute(q1)
            for record in mycursor:
                print(record)
        elif(c == 3):
            print("1. change Name")
            print("2. change Roll No")
            c = int(input("Enter your choice: "))
            if(c == 1):
                roll_no = int(input("Enter Roll no:"))
                name = input("Enter New Name: ")
                q1 = "update marks set Name='aka' where Roll_No=1"
                mycursor.execute(q1)

            elif(c == 2):
                oroll_no = int(input("Enter Old Roll no:"))
                Nroll_no = int(input("Enter New Roll no:"))
                name = input("Enter Name: ")
                q1 = "update marks set Roll_No=8 where Roll_No=1 and Name='krish'"
                mycursor.execute(q1)

            print("Record has been updated")
        elif(c == 4):
            roll_no = int(input("Roll no:"))
            q1 = "delete from marks where Roll_No=1"
            mycursor.execute(q1)

            print("The student record has been deleted")

    elif(choice == 2):
        print("1. Create a new course record with valid data")
        print("2. Display an existing course record")
        print("3. Update an existing course record with new data")
        print("4. Delete an existing course record")
        c = int(input("\nEnter your choice: "))

        if(c == 1):
            course = input("Enter course name ")
            #
            q1 = "create table history (Roll_No int, Name varchar(50))"
            mycursor.execute(q1)
            print("Insert data")
            roll_no = int(input("Roll no:"))
            name = input("Enter the name:")
            q1 = "insert into Accounts (Roll_No, Name) values ({},'{}')".format(
                roll_no, name)
            mycursor.execute(q1)
            mydb.commit()
            print("New student record has been created")

        elif(c == 2):
            course = input("Enter course name: ")
            print("The required course detailsa are: ")
            q1 = "select* from English"
            mycursor.execute(q1)
            for record in mycursor:
                print(record)
        elif(c == 3):
            print("1. change students Name enroled in the course")
            print("2. change Roll No of a student in a course")
            c = int(input("Enter your choice: "))
            course = input("Enter the course name: ")
            if(c == 1):
                roll_no = int(input("Enter Roll no:"))
                name = input("Enter New Name: ")
                q1 = "update English set Name='prayush' where Roll_N0=1"
                mycursor.execute(q1)
            elif(c == 2):
                oroll_no = int(input("Enter Old Roll no:"))
                Nroll_no = int(input("Enter New Roll no:"))
                name = input("Enter Name: ")
                q1 = "update English set Roll_N0=1 where Roll_N0=1 and Name='aarushi'"
                mycursor.execute(q1)

            print("Record has been updated")
        elif(c == 4):
            course = input("Enter course name")
            q1 = "delete from English"
            mycursor.execute(q1)
            print("The students record has been deleted")

    elif(choice == 3):
        print("1. Create a new exam record with valid data")
        print("2. Read an existing exam record")
        print("3. Update an existing exam record with new data")
        print("4. Delete an existing exam record")
        c = int(input("\nEnter your choice: "))

        if(c == 1):
            q1 = "create table Exam (course_code int,Subject varchar(50), Max_marks int, Min_marks int)"
            mycursor.execute(q1)
            print("Insert data")
            course_code = int(input("Enter course code:"))
            sub = input("Enter sub name: ")
            Max_marks = input("Enter maximum marks achived in that course: ")
            Min_marks = input("Enter minimum marks achived in that course: ")
            q1 = "insert into Exam (course_code,Subject , Max_marks , Min_marks) values ({},'{}',{},{})".format(
                course_code, sub, Max_marks, Min_marks)
            mycursor.execute(q1)
            mydb.commit()
            print("New exam record has been created")

        elif(c == 2):
            print("The required exam detailsa are: ")
            q1 = "select* from Exam"
            mycursor.execute(q1)
            for record in mycursor:
                print(record)
        elif(c == 3):
            print("1. change the Name of the subject: ")
            print("2. change maximum marks achived in the sub: ")
            print("3. change minimum marks achived in the sub: ")
            c = int(input("Enter your choice: "))
            if(c == 1):
                course_code = int(input("Enter course code:"))
                course_name = input("Enter Old course name:")
                name = input("Enter New course name: ")
                q1 = "update Exam set Subject='English' where course_code=101"
                mycursor.execute(q1)

            elif(c == 2):
                course_code = int(input("Enter course code:"))
                name = input("Enter course name: ")
                marks = input("Enter max marks: ")
                q1 = "update Exam set Max_marks=80 where course_code=101"
                mycursor.execute(q1)

            elif(c == 3):
                course_code = int(input("Enter course code:"))
                name = input("Enter course name: ")
                marks = input("Enter min marks: ")
                q1 = "update Exam set Min_marks=20 where course_code=101"
                mycursor.execute(q1)
            print("Record has been updated")

        elif(c == 4):
            q1 = "delete from exam"
            mycursor.execute(q1)
            print("Record has been deleted")

    elif(choice == 4):
        roll_no = int(input("Roll no:"))
        name = input("Enter the name:")
        course_name = input("Enter course name: ")
        c = list(course_name)
        for i in c:
            q1 = "insert into computer (Roll_N0 ,Name) values({},'{}')".format(
                roll_no, name)
            mycursor.execute(q1)
            mydb.commit()
        print("Course(s) has been assigned")

    elif(choice == 5):
        course_name = input("Enter the course name:")
        c = list(course_name)
        for i in c:
            q1 = "update marks set English = 0 "
            mycursor.execute(q1)
        print("The exam have been succesfully assigned to the course")

    elif(choice == 6):
        print("1. Enter scores for a student's exam")
        print("2. Update scores for a student's exam")
        print("3. Delete scores for a student's exam")
        c = int(input("\nEnter your choice: "))
        if(c == 1):
            roll_no = int(input("Roll no:"))
            name = input("Enter the name:")
            s1 = int(input("Enter score of English: "))
            s2 = int(input("Enter score of Maths: "))
            s3 = int(input("Enter score of Science: "))
            s4 = int(input("Enter score of Computer: "))
            q1 = "insert into marks (Roll_No,Name,English,Maths,Science,Computer)values({},'{}',{},{},{},{})".format(
                roll_no, name, s1, s2, s3, s4)
            mycursor.execute(q1)
            mydb.commit()
            print("Score has been saved")

        elif(c == 2):
            roll_no = int(input("Roll no:"))
            sub = input("Enter the sub name: ")
            s1 = int(input("Enter score of that sub: "))
            q1 = "update marks set English=90 where Roll_No=1"
            mycursor.execute(q1)
            print("The marks has been updated")
        elif(c == 3):
            roll_no = int(input("Roll no:"))
            sub = input("Enter the sub name: ")
            q1 = "update marks set English=0 where Roll_No=1"
            mycursor.execute(q1)

            print("The student' score record has been deleted")

    elif(choice == 7):
        print("1. Display individual student's result")
        print("2. Display overall result")
        print("3. Display course-wise result")

        c = int(input("\nEnter your choice: "))

        if(c == 1):
            roll_no = int(input("Roll no:"))
            name = input("Enter the name:")
            student1 = Result(roll_no, name)
            student1.Individual_report_card()

        elif(c == 2):
            student1 = Result(1, 'krish')  # default parameters
            student1.overall_report_card()

        elif(c == 3):
            student1 = Result(1, 'krish')  # default parameters
            student1.coursewise_report_card()
    elif(choice == 8):
        exit(0)

    else:
        print("Invalid input")
    

class Result:
    def _init_(self,roll_number, name):
      
        self.roll_number = roll_number
        self.name = name

    def main(self):
        main()

    def Individual_report_card(self):
        print("-----------------------------------------------------------------------------------------------------------------------------------------\n")
        print("\t\t\t\t\t\t || INDIVIDUAL STUDENT RESULT TABLE ||\n")
        print("-----------------------------------------------------------------------------------------------------------------------------------------")
        print("NAME: ", self.name)
        print("Roll Number: ", self.roll_number, '\n')

        print("\nMarks in each subject\n")

        query = " select* from krish"
        mycursor.execute(query)
        for record in mycursor:
            print(record)

        print("\nTotal_marks:")
        query = "select Total_marks from marks where Roll_No=1"
        mycursor.execute(query)

        for record in mycursor:
            print(record)

        print("\nPercentage(%): ")
        query = "select Percentage from marks where Roll_No=1"
        mycursor.execute(query)

        for record in mycursor:
            print(record)

    def overall_report_card(self):

        print("-----------------------------------------------------------------------------------------------------------------------------------------\n")
        print("\t\t\t\t\t\t || OVERALL STUDENT RESULT TABLE ||\n")
        print("-----------------------------------------------------------------------------------------------------------------------------------------")

        mycursor.execute("select* from marks")
        for record in mycursor:
            print(record)

        print("\nAverage marks:")
        mycursor.execute("select avg(Total_marks) from marks")
        for record in mycursor:
            print(record)

        print("\nOverall % marks: ")
        mycursor.execute("select avg(Total_marks) from marks")
        for record in mycursor:
            print(record)

    def coursewise_report_card(self):

        print("-----------------------------------------------------------------------------------------------------------------------------------------\n")
        print("\t\t\t\t\t\t || COURSEWISE STUDENT RESULT TABLE ||\n")
        print("-----------------------------------------------------------------------------------------------------------------------------------------")

        course_name = input("Enter course name whose info you want to find: ")

        print("The exam score of the course", course_name, "is")
        mycursor.execute("select Roll_No,Name,English from marks ")
        for record in mycursor:
            print(record)

        print("Total number of students in", course_name, "course")
        mycursor.execute("select count(English) from marks")
        for record in mycursor:
            print(record)

        print("Then avg marks of the course ", course_name, "is: ")
        mycursor.execute("select avg(English) from marks")
        for record in mycursor:
            print(record)

        print("Then % marks of the course ", course_name, "is: ")
        mycursor.execute("select avg(English) from marks")
        for record in mycursor:
            print(record)

class Student:
    def _init_(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")
        title=Label(self.root, text="Student Result Management System",bd=10,font=("BOOK ANTIQUA",40,"bold"),bg="blue",fg="white")
        title.pack(side=TOP,fill=X)
        global img
        path = r"C:\Users\aarus\OneDrive\Desktop\code\python_codes\logo2.jpg"
        img = ImageTk.PhotoImage(Image.open(path))
        data=StringVar()
        Manage_Frame=Frame(self.root, bd=4, relief=RIDGE)
        Manage_Frame.place(x=10,y=100,width=1250,height=760)
        frame = Frame(Manage_Frame, width=600, height=400)
        frame.pack()
        frame.place(anchor=E, relx=0.5, rely=0.5)
        img = ImageTk.PhotoImage(Image.open("logo2.jpg"))
        m_title=Label(Manage_Frame, text="Manage Students",fg="black",font=("times new roman",30,"bold"))
        m_title.grid(row=0,columnspan=2,padx=500,pady=20)
        lbl_name=Label(Manage_Frame,text="1.Student Record",fg="black",font=("times new roman",10,"bold"))
        lbl_name.grid(row=1,column=0,pady=10,padx=20,sticky='w')
        lbl_roll=Label(Manage_Frame,text="2.Course Record",fg="black",font=("times new roman",10,"bold"))
        lbl_roll.grid(row=2,column=0,pady=10,padx=20,sticky='w')
        panel = Label(root, image=img)
        panel.pack(side="right", fill="both")
        
        
        lbl_delete=Label(Manage_Frame,text="3.Exam Record",fg="black",font=("times new roman",10,"bold"))
        lbl_delete.grid(row=3,column=0,pady=10,padx=20,sticky='w')
        lbl_update=Label(Manage_Frame,text="4.Assign course(s) to student",fg="black",font=("times new roman",10,"bold"))
        lbl_update.grid(row=4,column=0,pady=10,padx=20,sticky='w')
        lbl_assigneexam=Label(Manage_Frame, text="5.Assign exam(s) to student",fg="black",font=("times new roman",10,"bold"))
        lbl_assigneexam.grid(row=5,column=0,pady=10,padx=20,sticky='w')
        lbl_editexam=Label(Manage_Frame, text="6.Edit student's exam course",fg="black",font=("times new roman",10,"bold"))
        lbl_editexam.grid(row=6,column=0,pady=10,padx=20,sticky='w')
        lbl_result=Label(Manage_Frame, text="7.Student(s) Result",fg="black",font=("times new roman",10,"bold"))
        lbl_result.grid(row=7,column=0,pady=10,padx=20,sticky='w')
        lbl_exit=Label(Manage_Frame, text="8.Exit",fg="black",font=("times new roman",10,"bold"))
        lbl_exit.grid(row=8,column=0,pady=10,padx=20,sticky='w')
        lbl_choice=Label(Manage_Frame,text="Enter your choice[1/2/3/4/5/6/7/8]",fg="black",font=("times new roman",10,"bold"))
        lbl_choice.grid(row=9,column=0,pady=10,padx=20,sticky='w')
        txt_roll=Entry(Manage_Frame,textvariable=data,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
        txt_roll.grid(row=10,column=0,pady=10,padx=10,sticky='w')
        btn_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE)
        btn_Frame.place(x=10,y=500,width=430)
        Submitbtn = Button(btn_Frame, text="Submit", width=10,command=lambda: Result.main(txt_roll.get()))
        Submitbtn.grid(row=0, column=0, padx=10, pady=10)

        
        
root=Tk()
ob=Student(root)
root.mainloop()
