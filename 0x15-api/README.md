This is a readme file for 0x15-api
Requirements
General
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/python3
Libraries imported in your Python files must be organized in alphabetical order
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the pycodestyle (version 2.8.*)
All your files must be executable
The length of your files will be tested using wc
All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
You must use get to access to dictionary value by key (it won’t throw an exception if the key doesn’t exist in the dictionary)
Your code should not be executed when imported (by using if __name__ == "__main__":)
Tasks
0. Gather data from an API
mandatory
Write a Python script that, using this REST API, for a given employee ID, returns information about his/her TODO list progress.

Requirements:

You must use urllib or requests module
The script must accept an integer as a parameter, which is the employee ID
The script must display on the standard output the employee TODO list progress in this exact format:
First line: Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
EMPLOYEE_NAME: name of the employee
NUMBER_OF_DONE_TASKS: number of completed tasks
TOTAL_NUMBER_OF_TASKS: total number of tasks, which is the sum of completed and non-completed tasks
Second and N next lines display the title of completed tasks: TASK_TITLE (with 1 tabulation and 1 space before the TASK_TITLE)
