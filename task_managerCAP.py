'''This is now Capstone Project 2 with a copy from Capstone Project 1'''

#=====importing libraries===========
'''This is the section where you will import libraries'''
from asyncio import tasks
import datetime
from datetime import date, datetime
import _strptime

# use the self-closing method with a text file called user.txt as well as the "r" function to read the data
# request user for their username and password
# request user to confirm their password and add to the user.txt file
def reg_user():
    print()
    with open("userCAP.txt", "a+") as f:

            request_of_username = input("Enter a valid username: ")
            print(username_list)

            if not username in username_list:
                print("true")

                request_of_password = input("Enter a valid password: ")
                password_confirm = input("Confirm your new password: ")
            
                while request_of_password != password_confirm:
                    password_confirm = input("Your passwords do not match. Try again\nConfirm Password: ")
            
                f.write("\n")
                f.write(request_of_username)
                f.write(", ")
                f.write(request_of_password)
            else:
                print("Wrong user. Please enter correct username. ")

# use a self-closing method with a text file called tasks.txt as well as the "r" function to read the data
# allow the user to add info of whom the task is assigned to, title of task, descrition of task, due date, current date
# using the 'a' modifier then print it out in an easy to read format
# have to indicate the a 'No' on whether the task has been completed or not
def add_task():
    if menu == 'a':
        with open("tasksCAP.txt", "a+") as f:
            assign_username = input("Enter the username of whom the task is assigned to: ")
            title_of_task = input("Enter the title of the assigned task: ")
            description_of_task = input("Enter the description of the assigned task: ")
            due_date = input("Enter the due date, i.e. dd/mm/yyyy: ")
            current_date = input("Enter the current date, i.e. dd/mm/yyyy: ")
            date = (f"{assign_username}, {title_of_task}, {description_of_task}, {due_date}, {current_date}, No\n")
            f.write(date)


# use a self-closing method with a text file called tasks.txt as well as the "r" function to read the data
# print out the information in an easy to read format using a for loop
# user will select option 'va' to view all their tasks
def view_all():
    with open("tasksCAP.txt", "r") as f:
        date = f.readlines()
        for task_manager in date:

            task_manager = task_manager.split(", ")
            assign_username = task_manager[0]
            title_of_task = task_manager[1]
            description_of_task = task_manager[2]
            due_date = task_manager[3]
            current_date = task_manager[4]
            output = f"\nassign username: {assign_username}\n"\
                        f"title of task: {title_of_task}\n"\
                        f"description of task: {description_of_task}\n"\
                        f"due date: {due_date}\n"\
                        f"current date: {current_date}\n"
            print(output)


# use a self-closing method with a text file called tasks.txt as well as the "r" function to read the data
# checking if the username of the person logged in is the same person as the username that is read from the text file
# user will select option 'vm' to view all their tasks that are assigned to the user
def view_mine():
    """
    The function allows the user to view all the tasks assigned to them, select a task to edit, and then
    edit the task.
    """
    with open("tasksCAP.txt", "r") as f:
        date = f.readlines()
        list_of_all_tasks = []
        for line_no, line in enumerate(date, 1):  # returns an object that contains a counter as a key
            line = line.split(", ")   
            list_of_all_tasks.append(line)
            line_username = line[0]
            if username == line_username:
                print(line_no, line)
            
# allow the user to select from the menu to either edit the task and/or mark the task as complete                
        menu = int(input("Select the task you want to edit by number or enter -1 to return to main menu: ")) - 1  

        if menu == -1:
            print("Going back to main menu!")

        else:

            option = input("MC - Mark as complete\nED - edit the task: ").upper()
            selected_task = list_of_all_tasks[menu]
            if option == "ED":
                edit_option = input("CU - change user assigned to task\nCD - Change due date\nSelection: ").upper()

                # allow user to be able to change to a new user
                if edit_option == "CU":
                    new_user = input("New User Assigned: ")
                    selected_task[0] = new_user
                    list_of_all_tasks[menu] = selected_task
                    print(selected_task)
                    print(list_of_all_tasks)

                # allow user to change the due date
                elif edit_option == "CD":
                    new_due_date = input("New due date: ")
                    selected_task[4] = new_due_date
                    list_of_all_tasks[menu]= selected_task
                    print(selected_task)
                    print(list_of_all_tasks)

                else:
                    print("You have selected an invalid option. Please try again.")

            # allow user to mark task as complete or not
            elif option == "MC": 
                completed_task = input("Has the task been completed? ")
                selected_task[5] = completed_task.replace("No", "Yes")
                selected_task = completed_task
                list_of_all_tasks[menu] = selected_task
                print(selected_task)
                print(list_of_all_tasks)    
            else:
                print("You have selected an invalid option. Please try again.")

            with open("tasksCAP.txt", "w") as write_file:

                for line in list_of_all_tasks:
                    write_file.writelines(", ".join(line))

def generate_reports():
    tasks_completed = 0
    tasks_incomplete = 0
    total_tasks = 0
    current_date_string = datetime.today()
    with open("tasksCAP.txt", "r") as f:
        contents = f.readlines()
        f.seek(0)
        for line in f:
            line = line.split(", ")
            total_tasks = total_tasks + 1
            
            if line[-1].strip("\n") == "Yes":
                tasks_completed += 1
            elif line[-1].strip("\n") == "No":
                tasks_incomplete += 1
            # print(line[4])
            today = date.today()
            new_assigned_date = today.strftime("%d %b %Y")
            # print(f"This is the new due date: {new_assigned_date}")

            incomplete_task_percentage = (tasks_completed / total_tasks)*100
            overdue_task_percentage = (tasks_incomplete / total_tasks)*100

            output = f"This is the total number of tasks: {total_tasks}\nThis is the total tasks completed:" \
                     f"{tasks_completed}\nThis is the total tasks that are incomplete: {tasks_incomplete}\n"\
                     f"This is the incomplete task percentage: {incomplete_task_percentage}\nThis is the overdue task percentage:" \
                     f"{overdue_task_percentage}\n"

    with open("task_overviewCAP.txt", "w") as f:
        f.write(output)

    with open("userCAP.txt", 'r+') as c: 
        with open("tasksCAP.txt", "r") as f:
            user_content = c.readlines()
            len(user_content)
            # print(user_content)
            output= f"Total number of users registered is {len(user_content)}\nThis is the total number of tasks:" \
                        f"{len(contents)}\n" 

            for line in user_content:
                user = line.split(", ")[0]
                tasks_assigned = 0
                percentage_tasks_complete = 0
                percentage_tasks_incomplete = 0
                overdue_task_percentage = 0
                current_date_string = datetime.today()
                # print(f"The current date is: {current_date_string}")

                for line in contents:
                    line = line.split(", ")
                    if line[0] == user:

                        tasks_assigned += 1

                        if line[-1].strip("\n") == "Yes":
                            percentage_tasks_complete += 1

                        else:
                            percentage_tasks_incomplete += 1

                overdue_task_percentage = len(user_content) / len(user_content) * 100

                output += f"\t\t{user}:\nNumber of tasks assigned to user: {tasks_assigned}\nPercentage of total number "\
                        f"of tasks assigned to user: {percentage_tasks_complete}\nPercentage of tasks that are incomplete:"\
                        f"{percentage_tasks_incomplete}\nThe overdue task percentage: {overdue_task_percentage}\n"

            with open("user_overviewCAP.txt", "w") as write_user:
                write_user.write(output)

# display the statistics of the tasks in the text files
def display_statistics():
    with open("task_overviewCAP.txt", "r") as f:
        for line in f:
            print(line)
    with open("user_overviewCAP.txt", "r") as f:
        for line in f:
            print(line)

                    
username_list = []
password_list = []

with open("userCAP.txt", "r") as f:
    for line in f:
                line = line.replace("\n", "")   # replace the new line with space between the "line" of code
                line_list = line.split(", ")

                username = line_list[0]
                password = line_list[1]

                username_list.append(username)  # be able to add in new usernames
                password_list.append(password)  # be able to add in new passwords
       
    
while True:
# ask user for input of their username and password
# print out whether they have typed in the correct username/password or not
# using a while loop to validate the user's information 
    
    username = input("What is your username? ")
    if username in username_list:
        print("Correct username")
        password = input("What is your password? ")

        user_index = username_list.index(username)

        if password == password_list[username_list.index(username)]:
            print("Correct password")
            # allow user to type in their username/password as many times until correct information is presented
            break
        else:
            print("Incorrect password")

    else:
        print("Incorrect username")


while True:
    # presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    menu = input("\n"'''Select one of the following Options below:
    r - Registering a user
    a - Adding a task
    va - View all tasks
    vm - view my task
    gr - generate reports
    ds - display statistics  
    e - Exit
    : ''').lower()

# calling the functions from the main menu
    if menu == "r" and username == "admin":
        reg_user()

    elif menu == "a":
        add_task()

    elif menu == "va":
        view_all()

    elif menu == "vm":
        view_mine()

    elif menu == "gr":
        generate_reports()

    elif menu == "ds":
        display_statistics()
    
    elif menu == "e":
        print("Thank you for using the program.")
        break
    else:
        print("Going back to main menu.")


