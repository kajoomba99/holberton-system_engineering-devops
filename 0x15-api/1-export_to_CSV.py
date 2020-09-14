#!/usr/bin/python3
"""module 1-export_to_CSV
    with the function todoUserProgressToCSV"""
import csv
import requests
import sys


def todoUserProgressToCSV(user_id: int) -> None:
    """export information about user TODO list progress in the CSV format."""
    URL = "https://jsonplaceholder.typicode.com"
    endpoint_user = "{}/users/{}".format(URL, user_id)
    endpoint_tasks = "{}/todos?userId={}".format(URL, user_id)

    user_request = requests.get(endpoint_user)
    user_response = user_request.json()
    username = user_response.get("name")

    task_request = requests.get(endpoint_tasks)
    task_response = task_request.json()

    with open("{}.csv".format(user_id), "w") as csv_file:
        writter = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in task_response:
            writter.writerow([
                user_id,
                username,
                task.get("completed"),
                task.get("title")
            ])


if __name__ == "__main__":
    user_id = int(sys.argv[1])
    todoUserProgressToCSV(user_id)
