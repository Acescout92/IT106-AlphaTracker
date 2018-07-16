#-------------------------------------------------------------------------------
# Alpha Tracker 
# Student Names:Bryce H and Ashok S.
# Assignment: project_2.py
# Submission Date: 5/6/2018
# Python Version: 3.6
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines as set forth by the
# instructor and the class syllabus.
#-------------------------------------------------------------------------------
# References: stackoverflow for os.path.isfile method syntax and usage. 
#-------------------------------------------------------------------------------
# Note: (a note to the grader as to any problems or uncompleted aspects of
# of the assignment)
#-------------------------------------------------------------------------------
# Pseudocode:
# Starts here
#Please refer to report.docx; pseudo code was too long for this area.
#-------------------------------------------------------------------------------
# Source Code: Your main module should be written here
#-------------------------------------------------------------------------------


import json
import os
from random import randint
import time

def start_here():
    """Checks the existence of user files, if none exist initializes the new user creation tools"""
    while True:
        if os.path.isfile('current_courses.json') and os.path.isfile('full_courses.json'):
            user = retrieve_user()
            if check_login(user):
                main_menu(user)
            else:
                print("Failed to log in. Exiting Program.")
                exit()
    #First time run initialization
        else:
            user = create_login()
            #path = 'C:\\Users\\bryce\\documents\\IT106' #Hardcoded placeholder. Must change to dump files to .py files directory.
            #path +="\\userfile.json"
            with open('userfile.json', 'w') as user_file:
                json.dump(user, user_file)
            first_run(user)
            continue

def main_menu(user): #WORK TO BE CONTINUED FROM HERE
    """Presents the main menu choice tree"""
    gpa = gpa_calculator()
    clear_screen()
    while True:
        for val in user.values():
            print("\nWelcome "+str(val[0])+", G-Number: " + str(val[2])+" GPA: "+str(gpa)+ "!")
        try:
            main = int(input("Please select from the following:\n1.Class Schedule\n2.Edit Class Schedule\n3.GPA Simulator\n4.Grad Date Simulator\n5.Exit\n"))
            if main == 1:
                print_schedule()      
            elif main == 2: 
                edit_schedule()    
            elif main == 3:
                gpa_menu(gpa)
            elif main == 4:
                grad_simulator(user)
            elif main == 5:
                exit()
            else:
                print("Invalid selection. Please try again\n") 
                continue
        except ValueError:
            print("Invalid selection. Please try again")
            continue
        
def create_login():
    """Generates a dictionary for a new user's profile, assigns user a G-Number"""
    user = {}
    username = input("We see that you are a new user! Please create a username!\n")
    password = input("Please input your password \n")
    clear_screen()
    print("Username accepted. Now generating g-number:\n")
    g_num = randint(00000000,99999999)
    print("Your new G-Number is: G", g_num)
    user[username] = [username, password, g_num, 0.0]
    return user #Return type: dictionary

def first_run(user):
    """Creates dictionaries: full_list and current_load containing class information"""
    print("Hello, and welcome to My Tracker v.01 alpha")
    print("Thank you. Beginning initial set up. Please be patient")
    full_list = collect_courses() #full_list contains the entirety of the classes for the major
    with open('full_courses.json', 'w') as full_courses_file:
        json.dump(full_list, full_courses_file)

    print("Thank you. Now, we will build your current class load.")
    with open('current_courses.json', 'w') as current_classes:
        json.dump(current_load(full_list), current_classes) #using full list, create current class schedule

def collect_courses():
    """Collects all classes required for the major, their credits, and grade status"""
    clear_screen()
    full_courses = {}
    input("First, We need to build a list of every class required for your major, and their respective credit values.")
    while True:
        clear_screen()
        print(full_courses)
        class_code = input("Please input course code. i.e: IT106\n If you are finished, press q to quit\n")
        if class_code == 'q':
            break
        elif class_code.upper() in full_courses.keys():
            print("You have already input this class. Please try again")
            continue
        class_code = class_code.upper()
        try:
            credit_hours = int(input("input the credit value for course: "+class_code+"\n"))
            grade = input("If you have already finished " + class_code+", please give your final letter grade. Otherwise type 0\n")
            status = input("Please give the status of this class: A-Actively Taking D-Dropped W-Withdrawn C-Completed\n")
            if status.upper() == 'A' or status.upper() == 'D' or status.upper() == 'W' or status.upper() == 'C': # changed this, OR can't be used after a single == like it was before
                full_courses[class_code] = [credit_hours, grade, status]
            else:
                input("Invalid selection")
                continue
        except ValueError:
            input("Invalid entry. ")
            continue
    return full_courses
    
def current_load(full_list):
    """Creates a dictionary with your current class schedule"""
    days_list = ['mon', 'tues', 'wed', 'thurs', 'fri','sat','sun']
    valid_grades= ["A", "A-","B+","B","B-","C+","C","C-","D","F",'0']

    clear_screen()
    current_schedule = {}
    print("Here are all of the classes you have input thus far: ", full_list.keys())
    input("Now, we will begin to build you current course schedule. Press any key to continue")
    
    class_code = input("Input class code, or type 'q' to quit: ")
    while class_code!= 'q':
        print(current_schedule)
        try:
            if class_code == 'q':
                break
            elif class_code.upper() not in full_list.keys():
                print("This class does not exist in your full list. Please try again:")
                class_code = input("Input class code, or type 'q' to quit: ")
                continue
            elif class_code.upper() in current_schedule:
                print("You have already entered the information for this class. Please try again ")
                continue
            else:
                class_code = class_code.upper()
                day = input("What days does "+class_code+" take place on? Separate by comma and use format:\nmon\ntues\nwed\nthurs\nfri\nsat\nsun ").split(',')
                for val in day:
                    if val not in days_list:
                        print("Invalid option")
                        continue
                start_time = int(input("Using format 2400, what time does "+class_code+" begin?\n"))
                end_time = int(input("Using format 2400, what time does "+class_code+" end?\n"))
                grade = input("What letter grade do you currently have? If no grade, input 0 ")
                if grade not in valid_grades:
                    print("Invalid input")
                    continue
                current_schedule[class_code] = [day, start_time, end_time, grade]
                class_code = input("Input class code, or type 'q' to quit: ")
        except ValueError:
            input("Invalid input. Press any key to continue ")
            continue
    return current_schedule

def retrieve_user():
    """Obtains user_file dictionary"""
    while True:
        try:
            with open('userfile.json', 'r') as opened_file:
                user = json.load(opened_file)
            return user
        except IOError:
            print("User File not found!")
            create_login()
            continue

def check_login(user):
    """Confirms user credentials"""
    clear_screen()
    while True:
        check_username = input("Please input your username\n")
        if check_username in user.keys():
            check_password = input("Please input your password\n")
            if check_password == user[check_username][1]:
                return True
            else:
                error = input("Password mismatch. Try again? type n to quit, or any key to continue \n")
                if error != 'n':
                    continue 
                else:
                    return False
        else:
            error = input("No username match! type n to quit or any key to continue \n")
            if error != 'n':
                continue 
            else:
                return False

def print_schedule():
    """Prints a simple schedule, using a list holding the days of the week"""
    clear_screen()
    print("====Current Schedule====")
    days = ['sun', 'mon', 'tues', 'wed', 'thurs', 'fri', 'sat']
    with open('current_courses.json', 'r') as current_file:
        schedule = json.load(current_file)
        for day in days:
            for val, val2 in schedule.items():
                if day in val2[0]:
                    print(day, val, str(val2[1])+'-'+str(val2[2])+" Presumed Grade: "+ val2[3])
    return 0

def grad_simulator(user):
    """Uses the full_courses file to determine how many credits left you have until graduation"""
    while True:
        total_credits = 0
        c_classes = 0
        completed_credits = []
        with open('full_courses.json', 'r') as full_courses:
            schedule = json.load(full_courses)
            for val in schedule.values():
                total_credits+=val[0]
                if val[2] == 'C':
                    c_classes+=1
                    completed_credits.append(val[0])
            print("Your major requires a total of: "+str(total_credits)+" credits to graduate. You have completed: " +str(c_classes)+" classes, or "+ str(sum(completed_credits)) + " credits")
            try:
                menu = int(input("\n1.Simulate by Semester\n2.Quit\n"))
                while menu != 2:
                    if menu == 1:
                        sem_sim(total_credits,c_classes,completed_credits)
                        menu = int(input("\n1.Simulate by Semester\n2.Quit\n"))
                break
            except ValueError:
                input("Incorrect input. Press any key to try again")
                continue
    return 0

def sem_sim(total_credits, c_classes, completed_credits): #REQUIRES MORE WORK
    """Uses input semester simulations to predict how many years and credits remaining until graduation"""
    clear_screen()
    while True:
        clear_screen()
        by_semester = []
        credits_remaining = total_credits - sum(completed_credits)
        print("Let's start by getting some information about your semester load. ")
        print("In a year, a student may take 4 semesters: Spring, Summer, Fall, Winter. ")
        try:
            semesters_count = int(input("How many semesters will you be taking this year? "))
            for val in range(semesters_count):
                credits = int(input("How many credits are you taking in semester: " +str(val+1)+"?"))
                by_semester.append(credits)
            print("Ok! Here's what your projected credit spread looks like for the year: \n", by_semester)
            projected_credit_impact = credits_remaining - sum(by_semester)
            classes_left = projected_credit_impact  / 3
            print("If you follow your current plan, you will have: "+str(projected_credit_impact)+" credits remaining, which roughly translates to "+str(round(classes_left,2))+" classes remaining ")
            input("Press any key to continue")
            break
        except ValueError:
            input("Invalid input. Press any key to continue")
            continue

    return 0

def gpa_calculator():
    """Gets the most recent grades from full_courses and returns cumulative GPA. To be printed on Main Menu"""
    gpa = 0.0
    grade_array = []
    credit_array = []
    grade_converter = {"A": 4.00, "A-":3.67, "B+": 3.33, "B": 3.00, "B-": 2.67, "C+": 2.33, "C": 2.00, "C-": 1.67, "D": 1.00, "F": 0.0}
    with open('full_courses.json', 'r') as fp:
        full_courses = json.load(fp)
        for val in full_courses.values():
            if val[2] == 'C':
                credit_array.append(val[0])
                for i, val2 in grade_converter.items():
                    if val[1] == i:
                        grade_array.append(val2)
        final_array = [val*val1 for val,val1 in zip(grade_array, credit_array)]
        gpa = round(sum(final_array)/sum(credit_array),2)
        print("GPA CALCULATED AS: "+str(gpa))
        return gpa

def gpa_menu(gpa):
    """Uses the current schedule to simulate potential GPA changes. Simulates both semester and cumulative GPA"""
    clear_screen()
    valid_grades= ["A", "A-","B+","B","B-","C+","C","C-","D","F",]
    print("===GPA Simulator===")
    while True:
        menu = int(input("Please select from the following options:\n1.Simulate Semester GPA & Cumulative GPA\n2.Exit and Return to Main Menu"))
        if menu == 1:
            grade_array = []
            with open('current_courses.json', 'r') as fp:
                current_courses = json.load(fp)
            with open('full_courses.json', 'r') as full_file:
                full_courses = json.load(full_file)
            full_credits = [y[0] for x,y in full_courses.items() if y[2]=='C'] #Holds the total credit values of all completed classes
            predicted_credits = [y[0] for x,y in full_courses.items() if x in current_courses.keys()] #Holds the credit values of the predicted classes from the current_courses list
            print("These are you current classes:\n")
            for val, val2 in current_courses.items():
                print(val)
            for val in current_courses.keys():
                grade = input("Input predicted letter grade for class: "+str(val)+" ")
                if grade not in valid_grades:
                    print("Invalid input")
                    break
                else:
                    credit_value = grade_conversion(grade)
                    grade_array.append(credit_value)
                    total = [val2*val3 for val2,val3 in zip(predicted_credits, grade_array)] #Takes the credits and grade values for the predicted classes and multiplies them together. Creates and array of true GPA-affective values
                    sem_gpa = round(sum(total)/sum(predicted_credits),2) #Builds predicted GPA
                    predicted_gpa_val = sum(predicted_credits)*sem_gpa #Multiplies total predictive credits with the predicted semester GPA
                    current_gpa_val = sum(full_credits)*gpa #Multiplies total earned credits with current GPA
                    cum_gpa = round((current_gpa_val + predicted_gpa_val)/(sum(full_credits)+sum(predicted_credits)),2) #PUTS ALL OF IT TOGETHER WOOOOO
                    print("Predicted GPA for the end of the semester is: " + str(sem_gpa)+". Your cumulative GPA would be: "+str(cum_gpa)) #all of that for this one line why god. 
        elif menu == 2:
            print("exiting...")
            break
            
    return 0

def grade_conversion(grade):
    """Accepts str value grade and converts the letter grade to a credit value"""
    grade_converter = {"A": 4.00, "A-":3.67, "B+": 3.33, "B": 3.00, "B-": 2.67, "C+": 2.33, "C": 2.00, "C-": 1.67, "D": 1.00, "F": 0.0}
    while True:
        for val, val2 in grade_converter.items():
            if grade == val:
                return val2
                

def edit_schedule():
    """Presents the edit_schedule menu, and handles editing the current_courses file."""
    days_list = ['mon', 'tues', 'wed','thurs', 'fri', 'sat', 'sun']
    valid_grades= ["A", "A-","B+","B","B-","C+","C","C-","D","F","0"]
    clear_screen()
    with open('full_courses.json', 'r') as f_file:
        full_courses = json.load(f_file)
    with open('current_courses.json', 'r') as s_file:
        current_courses = json.load(s_file)
    while True:
        try:
            print("====Course Editing Menu====")
            menu = int(input("1.Edit Class Schedule\n2.Close out current_classes\n3.Add Class to current schedule\n4.Remove courses\n5.Exit"))
            if menu == 1:
                edit_current_schedule(current_courses, full_courses)
            elif menu ==2:
                choice = input("Are you sure you want to close out your schedule? This will wipe out your current_courses file (Y/N) ")
                if choice.upper() == "Y":
                    for val,val2 in current_courses.items():
                        grade = input("Enter final letter grade for class: "+val)
                        full_courses[val][1] = grade
                        full_courses[val][2] = "C"
                    with open('full_courses.json', 'w') as fp:
                        json.dump(full_courses, fp)                           
                    fp = open('current_courses.json', 'w')
                    fp.close()
                    print("Current_courses file wiped")
                    continue
                elif choice.upper() == 'N':
                    continue
            elif menu == 3:
                class_code = input("Input class code, i.e IT106 ")
                if class_code not in full_courses.keys():
                    print("Class does not exist ")
                    continue
                else:
                    days = input("Using format mon, tues, wed, thurs, fri, sat, sun, input class days. Separate by comma").split(',')
                    for val in days:
                        if val not in days_list:
                            clear_screen()
                            print("WARNING: Invalid option")
                            days = "0"
                            continue
                    
                    start_time = int(input("Using format 2400, input start time: "))
                    end_time = int(input("Using format 2400, input end time: "))
                    grade = input("Input letter grade for this class. If no grade, input 0: ")
                    if grade not in valid_grades:
                        grade = "0"
                        print("Invalid option")
                        continue
                    else:
                        current_courses[class_code.upper()] = [days,start_time,end_time,grade.upper()]
                    with open('current_courses.json', 'w') as fp:
                        json.dump(current_courses, fp)
                        continue
            elif menu == 4:
                print("Here are the courses of your semester: ")
                for val in current_courses:
                    print(val)
                course_code = input("Which class do you want to delete? ")
                if course_code not in current_courses.keys():
                    print("Invalid Entry")
                    continue
                else:
                    choice = input("Are you sure you want to delete: " +course_code+"?(Y/N) ")
                    if choice.upper() == "Y":
                        del current_courses[course_code]
                        with open('current_courses.json', 'w')as fp:
                            json.dump(current_courses, fp)
                        continue
                    else:
                        continue
            elif menu == 5:
                break
        except ValueError:
            print("Invalid input, try again")
            continue
    return 0

def edit_current_schedule(current_courses, full_courses):
    """Presents the menu to edit the specifics of your current schedule"""

    days_list = ['mon', 'tues', 'wed','thurs', 'fri', 'sat', 'sun']
    valid_grades= ["A", "A-","B+","B","B-","C+","C","C-","D","F"]

    clear_screen()
    while True:
        try:
            print("Here are your current classes")
            for val in current_courses:
                print(val)
            choice = int(input("Please select which one you'd like to edit:\n1.Days\n2.Time\n3.Grade\n4.Save and Quit "))
            if choice !=4:
                class_code = input("Which class? ")
                if choice == 1:
                    days = input("Please input days using style: mon,tues,wed,thurs,fri,sat,sun. Separate by comma ").split(',')
                    for val in days:
                        if val not in days_list:
                            print("Invalid option")
                            days = current_courses[class_code][0]
                            current_courses[class_code][0] = days
                        else:
                            current_courses[class_code][0] = days
                elif choice == 2:
                    start_time = int(input("Using format 2400, input start time: "))
                    end_time = int(input("Using format 2400, input end time: "))
                    current_courses[class_code][1] = start_time
                    current_courses[class_code][2] = end_time
                    continue
                elif choice == 3:
                    grade = input("Update current letter grade: ")
                    if grade not in valid_grades:
                        print("Invalid input")
                        grade = current_courses[class_code][3]
                        current_courses[class_code][3] = grade.upper()
                        full_courses[class_code][1] = grade.upper()
                    else:
                        current_courses[class_code][3] = grade.upper()
                        full_courses[class_code][1] = grade.upper()
                        continue
            else:
                with open('current_courses.json', 'w') as fp:
                    json.dump(current_courses, fp)
                with open('full_courses.json', 'w') as f_file:
                    json.dump(full_courses, f_file)
                break
        except ValueError:
            print("Invalid input.")
            continue
    return 0
    
def clear_screen():
    """Useful clear screen function"""
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")
start_here()
