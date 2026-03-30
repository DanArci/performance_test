#Module imports
from files import *
from services import *

#Definition of the database path
route = 'db.csv'

#Main loop
opcion = 1
while opcion != 6:
    opcion = user_input('Choose the option to perform:\n1. Add Student\n2. Show Students\n3. Search Student\n4. Update Student\n5. Remove Student\n6. Exit\n','int','Please select a valid option. (1)(2)(3)(4)(5)')
    if opcion == 1:
        append_csv(add_student(), route, True)
    elif opcion == 2: 
        show_inventory(get_csv(route))
    elif opcion == 3:
        name = user_input('Enter the first name of the student you are searching for:\n','word','Only one word without punctuation marks is accepted.').upper().strip()
        search_student(get_csv(route), name)
    elif opcion == 4: 
        id = user_input('Enter the exact ID of the student you are updating:\n','int','Special characters, spaces, or letters are not allowed.')
        update_csv(update_student(get_csv(route), id),route,True)
    elif opcion == 5:
        id = user_input('Enter the exact ID of the student you are removing:\n','int','Special characters, spaces, or letters are not allowed.')
        update_csv(remove_student(get_csv(route),id),route, True)
    elif opcion == 6:
        print('Closing program...')
    else:
        print("\nPlease select a valid option. (1)(2)(3)(4)(5)(6)")
        opcion = 1

# This loop is responsible for displaying the main menu with the options 
# that will start each module.