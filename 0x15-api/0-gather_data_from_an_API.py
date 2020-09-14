#!/usr/bin/python3
"""module 0-gather_data_from_an_API
    with the function todoUserProgress"""
import requests
import sys


def todoUserProgress(user_id: int) -> None:
    """show information about user TODO list progress."""
    URL = "https://jsonplaceholder.typicode.com"
    endpoint_user = "{}/users/{}".format(URL, user_id)
    endpoint_tasks = "{}/todos?userId={}".format(URL, user_id)

    user_request = requests.get(endpoint_user)
    user_response = user_request.json()
    EMPLOYEE_NAME = user_response.get("name")

    task_request = requests.get(endpoint_tasks)
    task_response = task_request.json()

    DONE_TASKS = [
        task for task in task_response if task.get("completed", None)
    ]
    TASK_TITLE = [title.get('title') for title in DONE_TASKS]
    NUMBER_OF_DONE_TASKS = len(DONE_TASKS)
    TOTAL_NUMBER_OF_TASKS = len(task_response)

    print(
        "Employee {} is done with tasks({}/{}):".format(
            EMPLOYEE_NAME,
            NUMBER_OF_DONE_TASKS,
            TOTAL_NUMBER_OF_TASKS
        )
    )
    for title in TASK_TITLE:
        print(f"\t {title}")


if __name__ == "__main__":
    user_id = int(sys.argv[1])
    todoUserProgress(user_id)
