#!/usr/bin/python3
'''
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
'''
import csv
from sys import argv
import requests


if __name__ == "__main__":
    _url = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(f"{_url}users/{argv[1]}").json()
    todos_list = requests.get(
            _url + "todos", params={"userId": argv[1]}).json()

    userName = user['username']

    with open("{}.csv".format(argv[1]), "w", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)

        for todo in todos_list:
            writer.writerow(
                    [argv[1], userName, todo['completed'],  todo['title']])
