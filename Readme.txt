------------Alpha Tracker V1.0------------
----------------README--------------------

Welcome to Alpha Tracker v1.2
Python requirements: Python 3.6
To install: Simple place the .py file to the desired directory. Alpha Tracker will use this directory to build its files,
so an empty and specific directory is recommended

This program is designed to help you track your major, your current schedule, as well as your credits and GPA.
Alpha Tracker is designed to be an offline alternative to school-specific academic tracking software, and performs all the major functions that can be found on such platforms

--------First Run Initialization---------
Alpha Tracker detects if you are a new user automatically.
Upon determining first-time user status, the first run initialization begins

->Setting up user account
    Alpha Trakcer will begin by asking for the user to create a username and password. 
    A unique G-Number will be generated for the user.
    This information is saved in a dictionary, and output to a file at the .py file's root directory.

->Building full class schedule  
    Alpha Tracker will ask you to input your entire major's class requirements. IMPORTANT: You will NOT be able to change this later on.
    Be extremely certain you input the information correctly.
    For testing purposes, 10 classes are recommended. 10 classes will fully demonstrate the capabilities of Alpha Tracker
    Classes are held in a dictionary with the following attributes: {class code: [credit, grade, status]}
    For credit, give a single integer value
    For Grade, give the letter grade. ONLY input this if you have finished the course; this is your final grade. If you have not completed the class, input 0.
    For Status, follow the onscreen instructions. A may be used for classes you are current taking and you will take.

->Building Current schedule
    Alpha Tracker will now output your full major courseload
    The current schedule file is built on a dictionary with this format: {class code, [[date], time, grade]}
    If you input the wrong class code (does not exist in full courses), the program will ignore it and throw a message
    For Date, separate the days by commas (tues,wed). Make sure to use format mon,tues,wed,thurs,fri,sat,sun
    For Time, use format 2400. A class at 1:30 PM would be 1330
    For Grade, give a letter grade. It is not necessary to the program and is for your own reference. Type 0 if not. Valid letter grades are: A, A-, B+, B, B-, C+, C, C-, D, F
    Alpha Tracker will save this in a json file to the .py file's directory

->Returning Users
    Alpha Tracker looks for your user-created files.
    If none are found, you will be considered a new user.
    Otherwise, you will be prompted to input your username and password
    If either are invalid, press any key to continue, or q to quit

->Main Menu
    You will now be in the main menu.
    The Main Menu will show your username, G-Number, and your current cumulative GPA. 
    Make your selection of the following menu options: 
        1.Print Schedule
        2.Edit Schedule
        3.GPA Simulator
        4.Grad Date Simulator
        5.Exit
    Pressing 5 will exit the program. 


->Print schedule
    Prints your current schedule, as detailed in the current_courses file

->Grad Simulator
    This will take all of the classes you gave with a status of "C" and tell you how many classes you have completed.
    It will also tell you how many credits in total you need to graduate
    You will be given two options: simulate by semester, and exit to main menu
    Using the semester simulator is easy. You will tell the program how many semesters out of 4 you plan on taking that year.
    It will then loop through each semester, and ask you how many credits you plan on taking that year
    After the loop finishes, it will tell you how many classes you would have left, and how many credits you would need to take to graduate

->GPA Simulator
   The GPA simulator allows you to predict both semester and cumulative GPA in one function.
   Upon opening the GPA simulator menu, you will have a small menu: to run the prediciton or to return to main menu
   The Simulator will access your current_courses list and present the courses you are taking this semester. 
   Input desired letter grades for each class. 
   The simulator will then display the resultant semester GPA and what your cumulative GPA would look like. 
   Returns you to the GPA simulator menu. 
   Press 2 to return to main menu

->Edit schedule
    The edit_schedule menu will display. Select either edit current schedule, close out current_courses, add a class to your current schedule, remove your courses, or exit to main menu.
    1. Edit current schedule:
        Opens the edit current schedule menu
        Displays current schedule.
        From here, you can select changing day, time, grade, or save and exit.
        When editing days, be sure to use format mon,tues,wed,thurs,fri 
        When editing grades, make sure to use format A, A-, B+, B, B-, C+, C, C-, D, F
        Press 4 to save your changes and return to the edit schedule menu
    2. Close out current_courses
        Used for when your semester ends, this handy function allows you to update all of your final grades and empty your current_courses list. 
        You will be asked if you truly want to close out the file. Typing N will return you to the edit schedule menu
        Typing yes will begin the final grades process. Type in your final letter grades. Be very careful, as these cannot be changed later. 
        The program assigns these classes a status of "C"-Completed. 
        At the end of the process, your current_courses list will be empty. Use the add classes tool to start a new semester. 
    3. Add a class:
        Allows you to add a class to your current_schedule file. Incorrect inputs are handled directly and will return you to the edit schedule menu. 
        Input Class Code, days, time, and grade.
        If the class does not exist in your full_courses list, it will not be added.
    4. Remove a class:
        You will be shown your current schedule
        Type in the class code you want to remove
        Confirm whether or not you wish to remove the class
        Typing Y will remove the class and return you to the main menu.
        If the class code you type in does not exist in the current_courses file, you will receive a prompt and be returned to the edit schedule menu
    5. Exit:
        Returns you to main menu.



