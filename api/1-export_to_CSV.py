#!/usr/bin/python3

import csv
import requests
import sys

employee_id = sys.argv[1]

employee_data = requests.get('https://jsonplaceholder.typicode.com/users/' + employee_id)
employee_data_json = employee_data.json()

employee_name = employee_data_json['name']

todo_data = requests.get('https://jsonplaceholder.typicode.com/todos?userId=' + employee_id)
todo_data_json = todo_data.json()

with open (f'{employee_id}.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
    for task in todo_data_json:
        writer.writerow([employee_id, employee_name, task['completed'], task['title']])

if __name__ == '__main__':
    pass