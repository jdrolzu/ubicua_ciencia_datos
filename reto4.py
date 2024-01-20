'''
Topic: Student's grades management system

Description: Develope a python app that let students manage their grades. 
In order to achieve this, you must implement an adequate data structure for storing each student's data, including the following info:

    Id
    Name
    Email
    Phone number
    Birth date
    Grade 1
    Grade 2
    Grade 3
    Grade 4 
    
    You can choose a python dictionary as your data structure, use the student's id as your key for each entry within the dictionary.

Requirements:

Create a menu function that prints the following numeric options and then recieves the user's choice from console. 
Each option must execute its correspondent function to carry out the following indicated tasks:

    Add: let the user type in all the data of a new student. You can add multiple students.

    Search: Requests user a search criteria (for instance, id or name) to look for a student and display all of his/her information.

    Modify: Same as "Search" option, but let user update a student's grades.

    Cancel Subject: Same as "Search" option, but let confirm the removal of a student.

    Results per student: Looks for a student, computes and display:
        Student's final grade.
        Average grade of students's group.
        Print a message showing if the student's final grade is above or under the group's average.
        Print a message  showing if the student approved or failed the subject.
'''

grades = {}

def menu():
    print('\n*-*-*-*-*-* MENU *-*-*-*-*-*\n')
    print('Type 1, for adding a student. ')
    print('Type 2, for searching a student\'s info. ')
    print('Type 3, for updating student\'s info. ')
    print('Type 4, for removing a student. ')
    print('Type 5, to get student\'s result. ')
    print('Type 6, to exit. ')

def add():
    id = input('\nType the student\'s id: ')
    if not id in grades.keys():
        name = input('Type the student\'s name: ')
        email = input('Type the student\'s email: ')
        phone = input('Type the student\'s phone number: ')
        bdate = input('Type the student\'s bday (dd/mm/yyyy): ')
        grades[id] = {"name":name, "email":email, "phone number":phone, "birth date":bdate}

        try:
            grade1 = float(input('Type the student\'s grade 1: '))
            grades[id]["grade1"] = grade1
        except:
            grades[id]["grade1"] = 0
            
        try:
            grade2 = float(input('Type the student\'s grade 2: '))
            grades[id]["grade2"] = grade2
        except:
            grades[id]["grade2"] = 0

        try:
            grade3 = float(input('Type the student\'s grade 3: '))
            grades[id]["grade3"] = grade3
        except:
            grades[id]["grade3"] = 0

        try:
            grade4 = float(input('Type the student\'s grade 4: '))
            grades[id]["grade4"] = grade4
        except:
            grades[id]["grade4"] = 0
    else:
        print('\nStudent is already registered. \nTo modify his/her info, please choose the option #3 in the main menu')

def search_student():
    id = input('\nType the student\'s id you are looking for: ')
    if not id in grades.keys():
        print('\n~.~.~.~.~ Student not found ~.~.~.~.~')
    else:
        print(f'\n~.~.~.~.~ Information Student {id} ~.~.~.~.~\n')
        for key in grades[id].keys():
            print(f'{key}: {grades[id][key]}')

def submenu_modify():
    print('\nType 3.1, to modify student\'s name. ')
    print('Type 3.2, to modify student\'s email. ')
    print('Type 3.3, to modify student\'s phone number. ')
    print('Type 3.4, to modify student\'s birth date. ')
    print('Type 3.5, to modify student\'s grade 1. ')
    print('Type 3.6, to modify student\'s grade 2. ')
    print('Type 3.7, to modify student\'s grade 3. ')
    print('Type 3.8, to modify student\'s grade 4. ')

def validate_submenu_modify_opt():
    pass

def modify():
    id = input('\nType the student\'s id: ')
    if not id in grades.keys():
        print('\n~.~.~.~.~ Student not found ~.~.~.~.~')
    else:
        print(f'\n~.~.~.~.~ Information Student {id} ~.~.~.~.~\n')
        submenu_modify()
        sub_opt = input('\nType in, one of the above options: ')
        if sub_opt == '3.1':
            new_name = input('\nType student\'s new name: ')
            grades[id]["name"] = new_name
        elif sub_opt == '3.2':
            new_email = input('\nType student\'s new email: ')
            grades[id]["email"] = new_email
        elif sub_opt == '3.3':
            new_phone = input('\nType student\'s new phone: ')
            grades[id]["phone number"] = new_phone
        elif sub_opt == '3.4':
            new_bdate = input('\nType student\'s new birth date: ')
            grades[id]["birth date"] = new_bdate
        elif sub_opt == '3.5':
            new_grade1 = float(input('\nType student\'s new grade 1: '))
            grades[id]["grade1"] = new_grade1
        elif sub_opt == '3.6':
            new_grade2 = float(input('\nType student\'s new grade 2: '))
            grades[id]["grade2"] = new_grade2
        elif sub_opt == '3.7':
            new_grade3 = float(input('\nType student\'s new grade 3: '))
            grades[id]["grade3"] = new_grade3
        elif sub_opt == '3.8':
            new_grade4 = float(input('\nType student\'s new grade 4: '))
            grades[id]["grade4"] = new_grade4
        else:
            print('Check the option')

def remove_student():
    id = input('\nType the student\'s id to remove: ')
    if not id in grades.keys():
        print('\n~.~.~.~.~ Student not found ~.~.~.~.~')
    else:
        del grades[id]

def compute_results():
    id = input('\nType the student\'s id to get results: ')
    if not id in grades.keys():
        print('\n~.~.~.~.~ Student not found ~.~.~.~.~')
    else:
        print('\n~.~.~.~.~ Student Report ~.~.~.~.~')
        avg_grade = round((grades[id]["grade1"] + grades[id]["grade2"] + grades[id]["grade3"] + grades[id]["grade4"])/4, 1)
        print(f'\nStudent with id: {id} has a final average grade of: {avg_grade}')
        if avg_grade >= 3.0:
            print(f'\nStudent with id: {id} approved the course')
        else:
            print(f'\nStudent with id: {id} did not approve the course')
        
        total_grade_group = 0
        for id in grades.keys():
            total_grade_group = total_grade_group + grades[id]["grade1"] + grades[id]["grade2"] + grades[id]["grade3"] + grades[id]["grade4"]
        avg_group = round(total_grade_group/(len(grades)*4),1)
        print(f'\nGroup average grade: {avg_group}')
        
        if avg_grade > avg_group:
            print('\nStudent\'s average grade is above group\'s average grade')
        elif avg_grade == avg_group:
            print('\nStudent\'s average grade is the same as the group\'s average grade')
        else:
            print('\nStudent\'s average grade is below group\'s average grade')

def results():
    compute_results()

while True:
    menu()
    opt = input('Type in, one of the above options: ')
    if opt == '1':
        add()
    elif opt == '2':
        search_student()
    elif opt == '3':
        modify()
    elif opt == '4':
        remove_student()
    elif opt == '5':
        results()
    elif opt == '6':
        break
    else:
        print('\n~.~.~.~.~ Invalid option, try again ~.~.~.~.~')