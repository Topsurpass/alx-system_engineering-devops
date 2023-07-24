#!/usr/bin/python3
"""
A Python script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress.
Extend the Python script to export data in the JSON format.
"""
import json
import requests


if __name__ == "__main__":

    user_url = 'https://jsonplaceholder.typicode.com/users'
    todos_url = 'https://jsonplaceholder.typicode.com/todos'
    filename = "todo_all_employees.json"

    """store the json output"""
    u = requests.get(user_url)
    t = requests.get(todos_url)

    """Convert json to dictionary"""
    user_dic = u.json()
    todo_dic = t.json()

    """Get all user id and username in a turple"""
    all_user = []
    for user in user_dic:
        all_user.append((user.get("id"), user.get("username")))

    """Get all todo user_id, title, and status in a turple"""
    all_todo = []
    for todo in todo_dic:
        all_todo.append((todo.get("userId"),
                        todo.get("title"), todo.get("completed")))

    overall_todo = dict()
    for usr in all_user:
        obj = []
        for td in all_todo:
            if usr[0] == td[0]:
                obj.append(
                        {"username": usr[1],
                            "task": td[1],
                            "completed": td[2]})
        overall_todo[str(usr[0])] = obj

    """Write to json file"""
    with open(filename, mode="w", encoding="utf-8") as wr_file:
        """dump to a file"""
        json.dump(overall_todo, wr_file)
