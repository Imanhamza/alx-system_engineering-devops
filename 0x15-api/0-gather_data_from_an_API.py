#!/usr/bin/python3
'''
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
'''
import requests
from sys import argv


if __name__ == "__main__":
    _url = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(f"{_url}users/{argv[1]}").json()
    todos_list = requests.get(
            _url + "todos", params={"userId": argv[1]}).json()
    # print(len(todos_list))

    completed_tasks = []
    for task in todos_list:
        if task['completed'] is True:
            completed_tasks.append(task)
    # print(len(completed_tasks));

    user_name = user.get("name")
    print("Employee {} is done with tasks ({}/{}):".format(
        user_name, len(completed_tasks), len(todos_list)))

    for task in completed_tasks:
        print("\t", task.get("title"))
