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
        employeeName = data.get('name')

    todoUrl = url + "/todos"

    with urllib.request.urlopen(todoUrl) as response:
        data = json.loads(response.read().decode())
        tasks = data
        done = 0
        done_tasks = []

        for task in tasks:
            if task.get('completed'):
                done_tasks.append(task)
                done += 1

        print("Employee {} is done with tasks({}/{}):"
              .format(employeeName, done, len(tasks)))

        for task in done_tasks:
            print("\t {}".format(task.get('title')))
