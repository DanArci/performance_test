'''This file contains modules for data input and output.'''


# This function is responsible for receiving user input and verifying the data
# type, as well as sending a customizable error message in case of conflict.
def user_input(msg, type, errorMsg):
    running = True
    while running:
        try:
            if type == "int":
                number = int(input(msg))
                if number <= 0:
                    print("Please enter a number greater than 0")
                    continue
                running = False
                return number
            elif type == "float":
                number = float(input(msg))
                if number <= 0:
                    print("Please enter a number greater than 0.")
                    continue
                running = False
                return number
            elif type == "word" or type == "phrase":
                word = str(input(msg))
                if type == "word" and word.isalpha():
                    running = False
                    return word
                elif type == "phrase":
                    return word
                else:
                    raise ValueError
        except ValueError:
            print(errorMsg)
            continue

# This function is responsible for adding the new student to the student list.
def add_student():
    # Declaration of required list
    students = []

    #Data entry
    name = user_input('Enter the name of the student: ', 'word','Punctuation marks, spaces, or numbers are not allowed. Please re-enter the name of the student: ').upper()
    first_surname = user_input('Enter the first surname of the student: ', 'word','Punctuation marks, spaces, or numbers are not allowed. Please re-enter the student first surname: ').upper()
    second_surname = user_input('Enter the second surname of the student: ', 'word','Punctuation marks, spaces, or numbers are not allowed. Please re-enter the student second surname: ').upper()
    id = user_input('Enter the ID of the student: ', 'int','Special characters, spaces, or letters are not allowed. Please re-enter the student ID: ')
    age = user_input(f'Add the age of the student {name} {first_surname} {second_surname}: ', 'int','No symbols, spaces, or letters are allowed. Please re-enter the age of the student: ')
    course = user_input('Enter the course the student is taking: ', 'word','Punctuation marks, spaces, or numbers are not allowed. Please re-enter the name of the student: ').upper()
    status = user_input('Enter the status of the student\n1. Active\n2. Inactive\n','int', 'Please choose a valid option (1)(2):')
    
    #Data append and return
    student = {'name': name, 'full_name': f'{name} {first_surname} {second_surname}','id': id, 'age': age, 'course': course, 'status': status}
    students.append(student.copy())
    print('\nSaved successfully')
    return students

# This function is responsible for showing the current student list to the user.
def show_inventory(students):
    print('-'*110)
    for i in range(len(students)):
        status = get_status(students,i)
        print(
            f"Name of the student: {students[i]['full_name']} | ID: {students[i]['id']} | Age: {students[i]['age']} | Course: {students[i]['course']} | Status: {status}")
    print('-'*110)

# This function is responsible for searching for a student by the ID received by the user and displaying their data.
def search_student(students, name):
    print('-'*110)
    for i in range(len(students)):
        names = list(students[i].values())
        if names[0] == name:
            status = get_status(students,i)
            print(
                f"Name of the student: {students[i]['full_name']} | ID: {students[i]['id']} | Age: {students[i]['age']} | Course: {students[i]['course']} | Status: {status}")
    print('-'*110)

# This function is responsible for updating the data of a student. It asks you if you want to update the student's name or not.
def update_student(students, student_id,):

    # Loop that iterates through the list of students and compares the given ID with those in the list.
    for i in range(len(students)):
        ids = list(students[i].values())

        # Conditional statement that compares the IDs. If it finds a match, then it updates the data.
        if int(ids[2]) == student_id:
            
            # This if statement is responsible for updating the student's name if the user requests it; if the user does not request it, it is not updated. 
            option = user_input('Do you want to update the students name?\n1. Yes\n2. No\n','int','Please enter a valid option; (1)(2)')
            if option == 1:
                students[i]['name'] = user_input('Enter the updated name of the student: ', 'word','Punctuation marks, spaces, or numbers are not allowed. Please re-enter the name of the student: ').upper()
                first_surname = user_input('Enter the updated first surname of the student: ', 'word','Punctuation marks, spaces, or numbers are not allowed. Please re-enter the student first surname: ').upper()
                second_surname = user_input('Enter the updated second surname of the student: ', 'word','Punctuation marks, spaces, or numbers are not allowed. Please re-enter the student second surname: ').upper()
                students[i]['full_name'] = f"{students[i]['name']} {first_surname} {second_surname}"
            students[i]['id'] = user_input('Enter the students updated ID: ', 'int','Special characters, spaces, or letters are not allowed. Please re-enter the student ID: ')
            students[i]['age'] = user_input(f"Add the updated age of the student {students[i]['full_name']}: ", 'int','No symbols, spaces, or letters are allowed. Please re-enter the age of the student: ')
            students[i]['course'] = user_input('Enter the updated course the student is taking: ', 'word','Punctuation marks, spaces, or numbers are not allowed. Please re-enter the name of the student: ').upper()
            students[i]['status'] = user_input('Enter the updated status of the student\n1. Active\n2. Inactive\n','int', 'Please choose a valid option (1)(2):')
            print(students[i])
            print('\nSaved successfully')
            return students
        else:
            return students

# This function is responsible for removing a student
def remove_student(students, id):
    for i in range(len(students)):
        ids = list(students[i].values())
        if ids[2] == id:
            students.pop(i)
            return students

# This function is responsible for translating the student's status number (1 or 2) to a string value (Active or Inactive).
def get_status(students,index):
    if students[index]['status'] == '1':
        status = 'Active'
    elif students[index]['status'] == '2':
        status = 'Inactive'
    else:
        status = 'Uknown'
    return status