#!/usr/bin/python3
"""Export API data to CSV"""

import csv
import requests
import sys

def export_tasks_to_csv(user_id):
    # Construct user URL
    url_user = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    
    # Fetch user data
    user_res = requests.get(url_user)
    user_data = user_res.json()
    user_name = user_data.get('username')
    
    # Fetch tasks data
    task_res = requests.get(f'{url_user}/todos')
    tasks = task_res.json()
    
    # Write data to CSV
    with open(f'{user_id}.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        # Write header
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        # Write tasks
        for task in tasks:
            csv_writer.writerow([user_id, user_name, task["completed"], task["title"]])

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py USER_ID")
        sys.exit(1)
    
    user_id = sys.argv[1]
    export_tasks_to_csv(user_id)
