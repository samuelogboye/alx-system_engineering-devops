#!/usr/bin/python3
"""
A python script that create an API using the below url
"""
import csv
import json
import sys
import urllib.request

if __name__ == '__main__':
    employeeId = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = baseUrl + "/" + employeeId

    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode())
        userName = data.get('username')

    todoUrl = url + "/todos"
    with urllib.request.urlopen(todoUrl) as response:
        tasks = json.loads(response.read().decode())

    with open('{}.csv'.format(employeeId), mode='w', newline='') as file:
        for task in tasks:
            file.write(
                '"{}","{}","{}","{}"\n'.format(
                    employeeId,
                    userName,
                    task.get('completed'),
                    task.get('title')))
