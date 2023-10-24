#!/usr/bin/python3
""" Gather data from an API """

import json
import sys
import urllib.request

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users"

    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode())

    employees = {}
    for user in data:
        userId = user.get('id')
        userName = user.get('username')
        new_url = url + "/" + str(userId)

        todoUrl = new_url + "/todos"

        with urllib.request.urlopen(todoUrl) as response:
            tasks = json.loads(response.read().decode())

        employees[userId] = []
        for task in tasks:
            employees[userId].append({
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": userName
            })

    with open('todo_all_employees.json', mode='w') as file:
        json.dump(employees, file)
