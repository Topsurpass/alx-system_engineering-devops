#!/usr/bin/python3
"""
A Python script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress.
Extend the Python script to export data in the JSON format.
"""
import json
import requests
from sys import argv


if __name__ == "__main__":

    emp_id = argv[1]
    user_url = 'https://jsonplaceholder.typicode.com/users'
    todos_url = 'https://jsonplaceholder.typicode.com/todos'
    filename = "{}.json".format(emp_id)

    """store the json output"""
    u = requests.get(user_url)
    t = requests.get(todos_url)

    """Convert json to dictionary"""
    user_dic = u.json()
    todo_dic = t.json()

    """Since the username will be the same for an id, get the 1st username"""
    for user in user_dic:
        if user.get("id") == int(emp_id):
            USERNAME = user.get("username")
            break

    """Get both the title, status and username in a dictionary"""
    TASK_VALUE = []
    for todo in todo_dic:
        if todo.get("userId") == int(emp_id):
            TASK_VALUE.append(
                    {"task": todo.get("title"),
                        "completed": todo.get("completed"),
                        "username": USERNAME})

    TASK_KEY = {emp_id: TASK_VALUE}

    """Write to json file"""
    with open(filename, mode="w", encoding="utf-8") as wr_file:
        """dump to a file"""
        json.dump(TASK_KEY, wr_file)
