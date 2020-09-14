#!/usr/bin/python3
"""module that returns information about his/her TODO list progress."""
import requests
import sys


def main():
    user_id = sys.argv[1]
    URL = "https://jsonplaceholder.typicode.com"
    ENDPOINT_USER = "{}/users/{}".format(URL, user_id)
    ENDPOINT_TASKS = "{}/todos?userId={}".format(URL, user_id)

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
        "Employee {} is done with tasks({}/{}):".format(
            EMPLOYEE_NAME,
            NUMBER_OF_DONE_TASKS,
            TOTAL_NUMBER_OF_TASKS
        )
    )
    for title in TASK_TITLE:
        print(f"\t {title}")


if __name__ == "__main__":
    main()
