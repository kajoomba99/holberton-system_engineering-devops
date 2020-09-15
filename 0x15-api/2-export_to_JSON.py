#!/usr/bin/python3
"""module 1-export_to_CSV
    with the function todoUserProgressToCSV"""
import json
import requests
import sys


def todoUserProgressToJSON(user_id):
    """export information about user TODO list progress in the CSV format."""
    URL = "https://jsonplaceholder.typicode.com"
    endpoint_user = "{}/users/{}".format(URL, user_id)
    endpoint_tasks = "{}/todos?userId={}".format(URL, user_id)

    user_request = requests.get(endpoint_user)
    user_response = user_request.json()
    username = user_response.get("username")

    task_request = requests.get(endpoint_tasks)
    task_response = task_request.json()

    progress_dict = {}
    progress_dict[user_id] = []
    for task in task_response:

        title = task.get("title")
        task_status = task.get("completed")

        dict_task = {
            "task": title,
            "completed": task_status,
            "username": username
        }

        progress_dict[user_id].append(dict_task)

    with open("{}.json".format(user_id), "w") as json_file:
        json.dump(progress_dict, json_file)


if __name__ == "__main__":
    user_id = sys.argv[1]
    todoUserProgressToJSON(user_id)
