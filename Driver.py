# student name and id:
# SRT111 Assignment 2 Fall 2022
# I vouch that this program contains only lines of code provided by 
#the instructor or written by me and my partner. I did not collaborate 
#with other students, or showed my work to anyone.
def main(): 

    dict={} # Declare dictionary containing the student database
    dict=ReadFile() # Calling ReadFile Function
    #write the contents of your main function here 
    while True: 
        print("********************************************************")
        print("** Welcome to our students’ database system")
        print("** Please choose one of the options below:")
        print("** [a] to add new student record")
        print("** [e] to edit an existing student record")
        print("** [d] to drop a course for an existing student record")
        print("** [i] to get information about a student record")
        print("** [r] to remove an existing student record")
        print("** [q] to quit")
        print("********************************************************")
        choice = input("\nYour choice \u001b[1m")
        print('\u001b[0m', end='')
        # Code for menu
        if choice == "a":#call the function to add a new student in the database.
            dict=Add_new_student(dict)
            FileUpdate(dict)
        elif choice == "e": #call the function to edit the information of an existing student.
            dict=EditInformation(dict)
            FileUpdate(dict)
        elif choice == "d": #call the function to drop a course for an existing student.
            dict=Drop_Courses(dict)
            FileUpdate(dict)
        elif choice == "r":# call the function to remove the record of an existing student.
            dict=Remove_Student(dict)
            FileUpdate(dict)
        elif choice == "i":#call the function to display the information of an existing student.
            DisplayInformation(dict)
        elif choice == "q": 
            break
        else:
            print("Invalid choice, please enter a valid choice!" ) 


#define your functions here.

#   Read Data from File and store in Dictionary
def ReadFile():
    filename="studentsDatabase.dat"
    result ={}
    with open(filename, 'r') as f:
        for line in f:
            line=line.split(":",1)
            line[1]=line[1].split(":",4)
            list=[]
            for i in line[1]:
                if '\n' not in i:
                    list.append(i)
                else:
                    list.append(i.strip())
            result[line[0]]=list            
    return result

#   Display the information of Student by ID    
def DisplayInformation(dict):
    list=[]
    id=input("Please Enter the student Id: \u001b[1m")
    print('\u001b[0m', end='\n')


    if id in dict:
        for i in dict.get(id):
            list.append(i)
        print("ID: ",id)
        print("Name:",list[0])
        print("Semester:",list[1])
        print("Email:",list[2])
        print("Number of Courses:",list[3])
        print("Course Codes:",list[4],'\n')

    elif id not in dict:
        while(True):
            print("Press 1 to enter a new id")
            print("Press 2 to return back to Main Menu")
            choice=input("\nEnter choice: \u001b[1m")
            print('\u001b[0m', end='')
            if choice == "1":
                id=input("Please Enter the student Id: \u001b[1m")
                print('\u001b[0m', end='\n')
                numbers = sum(c.isdigit() for c in id)
                while numbers != 4: # Check on Id
                    id=input("Please Enter correct student Id: \u001b[1m")
                    print('\u001b[0m', end='\n')
                    numbers = sum(c.isdigit() for c in id)
                for i in dict.get(id):
                    list.append(i)
                print("ID: ",id)
                print("Name:",list[0])
                print("Semester:",list[1])
                print("Email:",list[2])
                print("Number of Courses:",list[3])
                print("Course Codes:",list[4],'\n')
                break
            elif choice == "2":
                break
            else:
                print("Wrong input enter choice again\n")

#   Add a new Student in Database 
def Add_new_student(dict):
    list=[]
    id=input("Please Enter student Id: \u001b[1m")
    print('\u001b[0m', end='\n')
    numbers = sum(c.isdigit() for c in id)
    while numbers != 4: # Check on Id
        id=input("Please Enter correct student Id: \u001b[1m")
        print('\u001b[0m', end='\n')
        numbers = sum(c.isdigit() for c in id)
    if id in dict:
        print('Student is already present')
    elif id not in dict:
        name = input("Please enter student name: \u001b[1m")
        print('\u001b[0m', end='')
        res=any(chr.isdigit() for chr in name)

        while str(res) == "True": # Check on Student name
            name = input("Please enter correct student name: \u001b[1m")
            print('\u001b[0m', end='')
            res=any(chr.isdigit() for chr in name)
        
        semester = input("Please enter student semester: \u001b[1m")
        print('\u001b[0m', end='')
        while semester.isnumeric() == False:# check on no of semester
            semester = input("Please enter correct student semester: \u001b[1m")
            print('\u001b[0m', end='')
        email = input("Please enter student email: \u001b[1m")
        print('\u001b[0m', end='')
        courses = input("Please enter number of courses student is taking this semester: \u001b[1m")
        print('\u001b[0m', end='')
        while courses.isnumeric() == False: # check on no of courses
            courses = input("Please enter correct number of courses student is taking this semester: \u001b[1m")
            print('\u001b[0m', end='')
        while int(courses) < 1  or int(courses) > 5: # check on no of courses
            if int(courses) < 1: 
                courses = input(f"Courses are less than 1.Please enter correct no of courses \u001b[1m")
                print('\u001b[0m', end='')
                while courses.isnumeric() == False: # check on no of courses
                    courses = input("Please enter correct number of courses student is taking this semester: \u001b[1m")
                    print('\u001b[0m', end='')
            elif int(courses) > 5:
                courses = input(f"Courses are greater than 5.Please enter correct no of courses \u001b[1m")
                print('\u001b[0m', end='')
                while courses.isnumeric() == False: # check on no of courses
                    courses = input("Please enter correct number of courses student is taking this semester: \u001b[1m")
                    print('\u001b[0m', end='')
        courses_list=[]
        for i in range(int(courses)):
            course_name = input(f"Course code {i+1}: \u001b[1m")
            print('\u001b[0m', end='')
            numbers = sum(c.isdigit() for c in course_name)
            letters = sum(c.isalpha() for c in course_name)
            if numbers== 3 and letters== 3:
                courses_list.append(course_name)
            while numbers!= 3 or letters!= 3: #  Coursesname check 
                print("Incorrect input")
                course_name = input(f"Course code {i+1}: \u001b[1m")
                print('\u001b[0m', end='')
                numbers = sum(c.isdigit() for c in course_name)
                letters = sum(c.isalpha() for c in course_name)
                courses_list.append(course_name)
        list.append(name)
        list.append(email)
        list.append(semester)
        list.append(courses)
        list.append(courses_list)
        dict[id]=list
        print("\u001b[1mRStudent Added successfully")
        print('\u001b[0m', end='\n')
    return dict

#   Remove student record in Database 
def Remove_Student(dict):
    id=input("Please Enter student Id: \u001b[1m")
    print('\u001b[0m', end='\n')
    numbers = sum(c.isdigit() for c in id)
    while numbers != 4: # Check on Id
        id=input("Please Enter correct student Id: \u001b[1m")
        print('\u001b[0m', end='\n')
        numbers = sum(c.isdigit() for c in id)
    if id in dict:
        confirm = input('Do you want to delete record from database. Press Y/N  \u001b[1m')
        print('\u001b[0m', end='\n')
        if confirm == "Y" or confirm == "y":
            dict.pop(id)
            print("\u001b[1mDeleted successfully")
            print('\u001b[0m', end='\n')
        elif confirm == "N" or confirm == "n":
            print("Request Declined")
        else:
            print("Wrong Input")
    elif id not in dict:
        print('Student id doesnot Exist')
    return dict

#   Edit student record in Database
def EditInformation(dict):
    id=input("Please Enter the student Id: \u001b[1m")
    print('\u001b[0m', end='\n')
    numbers = sum(c.isdigit() for c in id)
    while numbers != 4: # Check on Id
        id=input("Please Enter correct student Id: \u001b[1m")
        print('\u001b[0m', end='\n')
        numbers = sum(c.isdigit() for c in id)
    while id not in dict:
        option=input("Press [n] to try a new id or [m] for main menu: ")
        if option == "n":
            id=input("Please Enter the student Id: \u001b[1m")
            print('\u001b[0m', end='\n')
        if option == "m":
            return dict
    if id in dict:
        print("The following is the student information: \n")
        print("Name : ", dict.get(id)[0])
        print("ID : ", id)
        print("Semester : ", dict.get(id)[2])
        print("Email : ", dict.get(id)[1])
        print("Number of courses : ", dict.get(id)[3])
        print("Course codes : ", dict.get(id)[4])
        print("\nWhich field do you want to edit?  [S] for Semester or [E] for Email address : ")
        choice=input("\nEnter choice : \u001b[1m")
        print('\u001b[0m', end='')
        if choice == "e" or choice == "E":    
            inp = input("Enter the new value for email : ")
            dict.get(id)[1] = inp
            print("\u001b[1mRecord updated successfully")
            print('\u001b[0m', end='')
        elif choice == "s" or choice == "S":
            inp = input("Enter the new value for semester: ")
            dict.get(id)[2] = inp
            print("\u001b[1mRecord updated successfully")
            print('\u001b[0m', end='\n')
        return dict

# Update File
def FileUpdate(dict):
    f = open("studentsDatabase.dat", "w")
    for i in dict:
        f.write(i)
        f.write(":")
        f.write(str(dict[i][0]))
        f.write(":")
        f.write(str(dict[i][1]))
        f.write(":")
        f.write(str(dict[i][2]))
        f.write(":")
        f.write(str(dict[i][3]))
        f.write(":")
        f.write(str(dict[i][4]))
        f.write("\n")

#Drop the course of a student  
def Drop_Courses(dict):
    id=input("\nPlease Enter the student Id: \u001b[1m")
    print('\u001b[0m', end='')
    numbers = sum(c.isdigit() for c in id)
    while numbers != 4: # Check on Id
        id=input("Please Enter correct student Id: \u001b[1m")
        print('\u001b[0m', end='\n')
        numbers = sum(c.isdigit() for c in id)
    while id not in dict:
        option=input("Press [n] to try a new id or [m] for main menu: ")
        if option == "n":
            id=input("Please Enter the student Id: \u001b[1m")
            print('\u001b[0m', end='\n')
        if option == "m":
            return dict
    if id in dict:
        print("The following is the student information:")
        print("Name : ", dict.get(id)[0])
        print("ID : ", id)
        print("Semester : ", dict.get(id)[2])
        print("Email : ", dict.get(id)[1])
        print("Number of courses : ", dict.get(id)[3])
        print("Course code : ", dict.get(id)[4])
        
        print("\nWhich course do you want to edit?  Enter the Course code ")
        print("Your registered courses : ", dict.get(id)[4])
        
        string = dict.get(id)[4]
        string = string.replace("[","") #remove this "["
        string = string.replace("]","") #remove this "]"
        string = string.split(",")
        
        choice=input("\nEnter Course code : \u001b[1m")
        print('\u001b[0m', end='')
        while choice not in string:
            choice=input("\nWrong Input.Enter Course code : \u001b[1m")
            print('\u001b[0m', end='')
        if choice in string:
            string.remove(choice)
            new_str = str( string)
            new_str = new_str.replace(" ","") 
            new_str = new_str.replace("'","") 
            print("\u001b[1mCourses updated successfully")
            print('\u001b[0m', end='\n')
            dict.get(id)[4] = new_str
            dict.get(id)[3] = len(string)
        return dict

# Calling the Main Function
main()