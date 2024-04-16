#!/usr/bin/python3
"""
Python script to export data in the CSV format
"""

import csv
import requests
import sys

# Get the employee id from command line
employee_id = sys.argv[1]

# Get request to api for employee data
employee_data = requests.get('https://jsonplaceholder.typicode.com/users/' + employee_id)

# Parse data as json
employee_data_json = employee_data.json()

# Get employee name from key name
employee_name = employee_data_json['name']

# Get request to api for todo data
todo_data = requests.get('https://jsonplaceholder.typicode.com/todos?userId=' + employee_id)

# Parse data as json
todo_data_json = todo_data.json()

# Open a csv file with the name based on the employee ID and write the data
with open (f'{employee_id}.csv', 'w') as csvfile:
    # Create a CSV writer object, quoting all fields
    writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
    # Iterate over each task in the todo_data_json list
    for task in todo_data_json:
        writer.writerow([employee_id, employee_name, task['completed'], task['title']])

# Check if the script is being run directly as the main program
if __name__ == '__main__':
      # Code inside this block will only run if this script is executed directly
      pass