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

    userId = int(sys.argv[1])
    file_name = "{}.json".format(userId)

    res = requests.get("{}/users/{}".format(baseURL, userId))
    if res.status_code == 200:
        user = res.json()
        users_todos = {}
        users_todos[str(user.get('id'))] = get_user_todos(user)
        with open(file_name, 'w') as json_file:
            json_file.write(dumps(users_todos))
