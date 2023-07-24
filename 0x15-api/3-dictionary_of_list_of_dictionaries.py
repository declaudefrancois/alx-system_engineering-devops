#!/usr/bin/python3
"""
    Gather data from jsonplaceholder API and Export to JSON.
"""


baseURL = "https://jsonplaceholder.typicode.com"


def get_user_todos(user):
    """
        Returns a list of the all todos of given user's.

        Args:
            user (dict): A user from jsonplaceholder API.

        Returns:
            list: A list of user's todos.
    """
    userTodos = []
    res = requests.get("{}/todos?userId={}".format(baseURL, user.get('id')))
    if res.status_code == 200:
        todos = res.json()
        for todo in todos:
            userTodos.append({
                'task': todo.get('title'), 'completed': todo.get('completed'),
                'username': user.get('username')})
    return userTodos


if __name__ == "__main__":
    import csv
    from json import dumps
    import requests
    import sys

    file_name = "todo_all_employees.json"

    res = requests.get("{}/users".format(baseURL))
    if res.status_code == 200:
        users = res.json()
        all_users_todos = {}
        for user in users:
            all_users_todos[str(user.get('id'))] = get_user_todos(user)
            with open(file_name, 'w') as json_file:
                json_file.write(dumps(all_users_todos))
