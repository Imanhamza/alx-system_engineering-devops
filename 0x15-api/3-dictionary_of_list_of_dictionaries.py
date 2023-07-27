#!/usr/bin/python3
'''
Export Python script to export data in the JSON format.
'''
import json
from sys import argv
import requests


if __name__ == "__main__":
    _url = 'https://jsonplaceholder.typicode.com/'
    users = requests.get(f"{_url}users/").json()
    todos_list = requests.get(_url + "todos").json()
    # print(users[1])

    with open("todo_all_employees.json", mode="w") as file:

        _list = []
        for user, todo in zip(users, todos_list):
            _dict = {
                    "username": user['username'],
                    "task": todo['title'],
                    "completed": todo['completed']}
            _list.append(_dict)
            json.dump({user['id']: _list}, file)
