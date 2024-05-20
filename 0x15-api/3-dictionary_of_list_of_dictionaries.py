#!/usr/bin/python3
'''
Gather employee data from API and export to JSON format.
'''

import json
import requests

REST_API = "https://jsonplaceholder.typicode.com"


def get_all_employee_data():
    all_employee_data = {}
    users_response = requests.get('{}/users'.format(REST_API))

    if users_response.status_code == 200:
        users_data = users_response.json()

        for user in users_data:
            user_id = user.get('id')
            username = user.get('username')

            todos_response = requests.get(
                '{}/todos?userId={}'.format(REST_API, user_id)
            )

            if todos_response.status_code == 200:
                todos_data = todos_response.json()

                task_list = [
                    {
                        'username': username,
                        'task': task['title'],
                        'completed': task['completed']
                    }
                    for task in todos_data
                ]
                all_employee_data[user_id] = task_list

    return all_employee_data


def export_to_json(all_employee_data):
    filename = 'todo_all_employees.json'
    with open(filename, 'w') as jsonfile:
        json.dump(all_employee_data, jsonfile)
    print('Data exported to {}'.format(filename))


if __name__ == '__main__':
    all_employee_data = get_all_employee_data()
    if all_employee_data:
        export_to_json(all_employee_data)
    else:
        print('Error fetching data from API.')
