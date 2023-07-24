#!/usr/bin/python3
"""
A Python script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress.
Extend Python script to export data in the CSV format.
"""
import csv
import requests
from sys import argv


if __name__ == "__main__":

    emp_id = argv[1]
    user_url = 'https://jsonplaceholder.typicode.com/users'
    todos_url = 'https://jsonplaceholder.typicode.com/todos'
    filename = "{}.csv".format(emp_id)

    TASK_TITLE_STATUS = []

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

    """Get both the status and title in a turple"""
    for todo in todo_dic:
        if todo.get("userId") == int(emp_id):
            TASK_TITLE_STATUS.append(
                    (todo.get("completed"), todo.get("title")))

    """Write to csv file"""
    with open(filename, mode="w", encoding="utf-8") as wr_file:
        """Define column header for scv file"""
        column_header = ["USER_ID", "USERNAME", "TASK_COMPLETE_STATUS",
                         "TASK_TITLE"]
        writer = csv.DictWriter(
                wr_file, fieldnames=column_header, quoting=csv.QUOTE_ALL)

        """Now write each row to file in order of the column header
        specified"""
        for task in TASK_TITLE_STATUS:
            writer.writerow({
                "USER_ID": emp_id,
                "USERNAME": USERNAME,
                "TASK_COMPLETE_STATUS": task[0],
                "TASK_TITLE": task[1]
                })
