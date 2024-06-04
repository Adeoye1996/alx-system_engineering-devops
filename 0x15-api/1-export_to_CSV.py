#!/usr/bin/python3
'''
Let gather the employee data from API
'''

import csv
import requests
import sys

REST_API = "https://jsonplaceholder.typicode.com"


def get_employee_data(employee_id):
    user_response = requests.get(
        '{}/users/{}'.format(REST_API, employee_id)
    )
    todos_response = requests.get(
        '{}/todos'.format(REST_API)
    )

    if user_response.status_code == 200 and todos_response.status_code == 200:
        user_data = user_response.json()
        todos_data = todos_response.json()
        return user_data, todos_data
    return None, None


def export_to_csv(employee_id, employee_name, tasks):
    filename = '{}.csv'.format(employee_id)
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = [
            'USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE'
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for task in tasks:
            writer.writerow({
                'USER_ID': employee_id,
                'USERNAME': employee_name,
                'TASK_COMPLETED_STATUS': task['completed'],
                'TASK_TITLE': task['title']
            })
    print('Data exported to {}'.format(filename))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1].isdigit():
            employee_id = int(sys.argv[1])
            user_data, todos_data = get_employee_data(employee_id)

            if user_data and todos_data:
                employee_name = user_data.get('name')
                tasks = [
                    task for task in todos_data
                    if task.get('userId') == employee_id
                ]
                export_to_csv(employee_id, employee_name, tasks)
            else:
                print('Error fetching data from API.')
        else:
            print('Please provide a valid integer employee ID.')
    else:
        print('Usage: {} <employee_id>'.format(sys.argv[0]))
