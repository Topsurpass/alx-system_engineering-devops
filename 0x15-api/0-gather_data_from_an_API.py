#!/usr/bin/python3
"""
A Python script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress.
"""

import requests
from sys import argv


if __name__ == "__main__":

    emp_id = argv[1]
    user_url = 'https://jsonplaceholder.typicode.com/users'
    todos_url = 'https://jsonplaceholder.typicode.com/todos'

    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    TASK_TITLE = []

    """store the json output"""
    u = requests.get(user_url)
    t = requests.get(todos_url)

    """Convert json to dictionary"""
    user_dic = u.json()
    todo_dic = t.json()

    for todo in todo_dic:
        if todo.get("userId") == int(emp_id):
            TOTAL_NUMBER_OF_TASKS += 1
            if todo.get("completed"):
                TASK_TITLE.append(todo.get("title"))
                NUMBER_OF_DONE_TASKS += 1

    for user in user_dic:
        if user.get("id") == int(emp_id):
            EMPLOYEE_NAME = user.get("name")
            break

    output = "Employee {} is done with tasks({}/{}):".format(
                    EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS)
    print(output)
    for title in TASK_TITLE:
        print("\t{}".format(title))
