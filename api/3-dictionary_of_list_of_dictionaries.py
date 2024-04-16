#!/usr/bin/python3
"""
Python script to export data in the JSON format
"""

import json
import requests

# Get request to api for employee data
employee_data = requests.get('https://jsonplaceholder.typicode.com/users')

# Parse data as json
employee_data_json = employee_data.json()

# Create empty all_tasks dictionary
all_tasks = {}

# Iterate over each user in the employee_data_json list
for user in employee_data_json:
    # Extract the user ID and username from the current user
    user_id = str(user['id'])
    user_name = user['username']
    # Get request to api for todo data of current user
    todo_data = requests.get(
         'https://jsonplaceholder.typicode.com/todos?userId=' + user_id)
    # Parse data as json
    todo_data_json = todo_data.json()
    # Task list with provided format
    task_list = [
        {
            'username': user_name,
            'task': task['title'],
            'completed': task['completed']
        } for task in todo_data_json]
    # Adds the task to the all_tasks dictionary
    all_tasks[user_id] = task_list

# Export all_tasks dictionary to a jsonfile named 'todo_all_employees.json'
with open('todo_all_employees.json', 'w') as jsonfile:
    json.dump(all_tasks, jsonfile)

# Check if the script is being run directly as the main program
if __name__ == '__main__':
    # Code inside this block will only run if this script is executed directly
    pass
