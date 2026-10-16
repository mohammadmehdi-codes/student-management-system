class Student():
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display_info(self):
        print(f"1. Name: {self.name}")
        print(f"2. Roll No.: {self.roll_no}")
        print(f"3. Marks: {self.marks}")
        print("4. Grade:",self.cal_grade())
        
    def cal_grade(self):
        if self.marks >= 90 and self.marks <= 100:
            return "A"
        elif self.marks >= 75 and self.marks < 90:
            return "B"
        elif self.marks >= 60 and self.marks < 75:
            return "C"
        elif self.marks >= 40 and self.marks < 60:
            return "D"
        elif self.marks < 40 and self.marks >= 0:
            return "Fail ❌"
        else:
            return "Invalid marks."
                 
s_list = []

def add_student():
    user_name = input("Enter student name: ").strip()
    words = user_name.split()
    if words:  
        if all (word.isalpha() for word in words):
            try:
                user_roll_no = int(input("Enter the student's roll number: "))
                for x in s_list:
                    if x.roll_no == user_roll_no:
                        print("This roll number is already assigned. Please choose another one.")
                        return
                user_marks = float(input("Enter the student's marks: "))
                if user_marks > 100 or user_marks < 0:
                    print("Invalid marks entered.")
                    return
            except ValueError:
                print("Invalid input.")
                return
            s_list.append(Student(user_name,user_roll_no,user_marks))
            print("✅ Student added successfully.")
        else:
            print("Invalid input.")
    else:
        print("Empty entries are not allowed.")
def view_student():
        if not s_list:
            print("No records found.")
        else:
            for x in s_list:
                x.display_info()

def search_student():
    try:
        r = int(input("Enter the roll number: "))
    except ValueError:
        print("Invalid roll number.")
        return
    for x in s_list:
        if r == x.roll_no:
            print("✅ Student found! Here are the details:")
            x.display_info()
            break
    else:
        print("Student not found.")  

def update_marks():
    try:
        r = int(input("Enter the roll number: "))
    except ValueError:
        print("Invalid roll number. ❌")
        return
    for x in s_list:
        if r == x.roll_no:  
            try:
                new_mark = float(input("Enter the new marks:"))
            except ValueError:
                print("Invalid entry.")
                return
            if new_mark > 100 or new_mark < 0:
                print("Invalid marks entered.")
                return
            x.marks = new_mark
            print("Marks updated successfully. ✅")
            x.display_info()
            break
    else:
        print("Student not found.")  

def remove_student():
    try:
        r = int(input("Enter the roll number: "))
    except ValueError:
        print("Invalid roll number.")
        return
    for x in s_list:
        if r == x.roll_no:
            s_list.remove(x)
            print("Student removed successfully. ✅")
            break
    else:
        print("Student not found.")                      
    
while True:
    print("***** Student Management System *****")
    print("1. Add Student")   
    print("2. View All Students") 
    print("3. Search Student")  
    print("4. Update Marks")  
    print("5. Delete Student")  
    print("6. Exit")

    try:
        user = int(input("Choose an option from 1 to 6: "))
    except ValueError:
        print("Invalid input.")
        continue
    if user == 1:
        add_student()

    elif user == 2:
        view_student()

    elif user == 3:
        search_student()

    elif user == 4:
        update_marks()

    elif user == 5:
        remove_student()

    elif user == 6:
        print("Thank you, and goodbye!")
        break
    else:
        print("Please choose an option between 1 and 6.")