#!/usr/bin/python3
"""
    Gather data from jsonplaceholder API.
"""


if __name__ == "__main__":
    import requests
    import sys

    userId = int(sys.argv[1])
    baseURL = "https://jsonplaceholder.typicode.com"

    # Fetch The user and its todos.
    user = None
    todos = []
    total = 0

    res = requests.get("{}/users/{}".format(baseURL, userId))
    if res.status_code == 200:
        user = res.json()

        res = requests.get("{}/todos?userId={}".format(baseURL, userId))
        if res.status_code == 200:
            todos = res.json()
            total = len(todos)
            todos = list(filter(lambda todo: todo.get('completed'), todos))

    if user is not None:
        fmt = "Employee {} is done with tasks({}/{}):"
        print(fmt.format(user.get('name'), len(todos), total))
        for todo in todos:
            print("\t {}".format(todo.get('title')))
