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
    # todos_list = requests.get(_url + "todos").json()
    # print(users[1])

    with open("todo_all_employees.json", mode="w") as file:

        json.dump({
            user.get("id"): [{
                "task": todo["title"],
                "completed": todo["completed"],
                "username": user["username"]
            } for todo in requests.get(
                _url + "todos", params={"userId": user["id"]}).json()]
            for user in users}, file)
