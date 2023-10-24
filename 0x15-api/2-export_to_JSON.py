#!/usr/bin/python3
""" Gather data from an API """

import json
import sys
import urllib.request

if __name__ == "__main__":
    employeeId = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = baseUrl + "/" + employeeId

    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode())
        employeeName = data.get('username')

    todoUrl = url + "/todos"

    with urllib.request.urlopen(todoUrl) as response:
        data = json.loads(response.read().decode())
        tasks = data

    with open('{}.json'.format(employeeId), mode='w') as file:
        json.dump(
            {
                employeeId: [
                    {
                        "task": task.get('title'),
                        "completed": task.get('completed'),
                        "username": employeeName
                    } for task in tasks
                ]
            },
            file)
