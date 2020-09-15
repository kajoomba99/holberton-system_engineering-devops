#!/usr/bin/python3
"""module 1-export_to_CSV
    with the function todoUserProgressToCSV"""
import json
import requests
import sys


def todoUserProgressToJSON():
    """export information about user TODO list progress in the CSV format."""
    URL = "https://jsonplaceholder.typicode.com"
    endpoint_user = "{}/users".format(URL)
    user_request = requests.get(endpoint_user)
    user_response = user_request.json()

    all_users_progress = {}

    for user in user_response:
        user_id = user.get('id')
        username = user.get("username")

        endpoint_tasks = "{}/todos?userId={}".format(URL, user_id)
        task_request = requests.get(endpoint_tasks)
        task_response = task_request.json()

        all_users_progress[user_id] = []

        for task in task_response:
            title = task.get("title")
            task_status = task.get("completed")

            dict_task = {
                "username": username,
                "task": title,
                "completed": task_status
            }

            all_users_progress[user_id].append(dict_task)

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_users_progress, json_file)


if __name__ == "__main__":
    todoUserProgressToJSON()
