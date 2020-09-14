#!/usr/bin/python3
"""module that returns information about his/her TODO list progress."""
from sys import argv
import requests


def main():
    user_id = argv[1]
    URL = "https://jsonplaceholder.typicode.com"
    ENDPOINT_USER = f"{URL}/users/{user_id}"
    ENDPOINT_TASKS = f"{URL}/todos?userId={user_id}"

    user_request = requests.get(ENDPOINT_USER)
    user_response = user_request.json()
    EMPLOYEE_NAME = user_response.get("name")

    task_request = requests.get(ENDPOINT_TASKS)
    task_response = task_request.json()

    DONE_TASKS = [
        task for task in task_response if task.get("completed", None)
    ]
    TASK_TITLE = [title.get('title') for title in DONE_TASKS]
    NUMBER_OF_DONE_TASKS = len(DONE_TASKS)
    TOTAL_NUMBER_OF_TASKS = len(task_response)

    print(
        (f"Employee {EMPLOYEE_NAME} is done"
         f"with tasks({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")
    )
    for title in TASK_TITLE:
        print(f"\t{title}")


if __name__ == "__main__":
    main()
