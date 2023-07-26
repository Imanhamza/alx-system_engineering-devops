#!/usr/bin/python3
'''
Export Python script to export data in the JSON format.
'''
import json
from sys import argv
import requests


if __name__ == "__main__":
    _url = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(f"{_url}users/{argv[1]}").json()
    todos_list = requests.get(
            _url + "todos", params={"userId": argv[1]}).json()
    # print(todos_list[1])

    filename = argv[1] + ".json"
    username = user['username']
    with open(filename, mode="w") as file:
        for todo in todos_list:
            json.dump({
                argv[1]: [{
                    "task": todo['title'],
                    "completed": todo['completed'],
                    "username": username}]
                }, file)
