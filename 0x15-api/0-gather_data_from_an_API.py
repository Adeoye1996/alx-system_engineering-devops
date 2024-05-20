#!/usr/bin/python3
'''
Let gather the employee data from API
'''

import requests
import sys

REST_API = "https://jsonplaceholder.typicode.com"

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1].isdigit():
            employee_id = int(sys.argv[1])
            user_response = requests.get(
                f'{REST_API}/users/{employee_id}'
            )
            todos_response = requests.get(f'{REST_API}/todos')

            if (
                user_response.status_code == 200 and
                todos_response.status_code == 200
            ):
                user_data = user_response.json()
                todos_data = todos_response.json()

                employee_name = user_data.get('name')
                tasks = [task for task in todos_data if task.get('userId') == employee_id]
                 completed_tasks = [task for task in tasks if task.get('completed')]
                completion_status = f'{len(completed_tasks)}/{len(tasks)}'
                print(f'Employee {employee_name} is done with tasks({completion_status}):')

                for task in completed_tasks:
                    print(f'\t {task.get("title")}')

            else:
                print('Error fetching data from API.')
        else:
            print('Please provide a valid integer employee ID.')
    else:
        print('Usage: {} <employee_id>'.format(sys.argv[0]))
