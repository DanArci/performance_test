# CSV module import
import csv

# Function to save the CSV using Append mode. It creates the file with its headers if they do not already exist. It contains simple error
# handling and permissions management.
def append_csv(students, route, include_header=True):
    import os
    file_exists = os.path.isfile(route)
    
    try:
        if students == []:
            print('The students list is empty')
        
        with open(route, 'a', newline='') as f:
            writer = csv.writer(f, delimiter=',')

            if not file_exists and include_header:
                writer.writerow(['name', 'full_name', 'id', 'age', 'course', 'status'])
            
            for student in students:
                writer.writerow([student['name'], student['full_name'], student['id'], student['age'], student['course'],student['status']])
                    
    except PermissionError:
        print('You do not have permissions for this file.')
        return
    except Exception as e:
        print(f'Error saving file: {e}')
        return
    print(f'Inventory stored in: {route}')

# This function is responsible for updating the student list.
def update_csv(students, route, include_header):

    try:
        with open(route, 'w', newline='') as f:
            writer = csv.writer(f, delimiter=',')

            if include_header:
                writer.writerow(['name', 'full_name', 'id', 'age', 'course', 'status'])

            if students == None:
                print('The list has been emptied.')
                return

            for student in students:
                writer.writerow([student['name'], student['full_name'], student['id'], student['age'], student['course'],student['status']])
    
    except PermissionError:
        print('You do not have permissions for this file.')
        return
    except Exception as e:
        print(f'Error saving file: {e}')
    print(f'List of students stored in: {route}')          

# This function is responsible for obtaining the list of students from the CSV file
# and converting it into a Python list that is used in the other modules.
def get_csv(route):

    try:
        import os
        file_exists = os.path.isfile(route)
        
        if not file_exists:
            raise FileNotFoundError
        
        with open(route, 'r', newline='') as f:
            reader = csv.reader(f, delimiter=',')
            next(reader)
            db = list(reader)
            students = []

            # A loop that converts each value in the database from a "Lists within a list"
            # format to a "dictionaries within a list" format.
            for i in range(len(db)):
                student = {
                    'name': db[i][0],
                    'full_name': db[i][1], 
                    'id': db[i][2],
                    'age': db[i][3], 
                    'course': db[i][4], 
                    'status': db[i][5]
                }
                students.append(student)
            return(students)

    except Exception as e:
        print(e)
        return
        