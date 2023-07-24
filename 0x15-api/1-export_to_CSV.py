#!/usr/bin/python3
"""
    Gather data from jsonplaceholder API and Export to CSV.
"""


if __name__ == "__main__":
    import csv
    import requests
    import sys

    userId = int(sys.argv[1])
    baseURL = "https://jsonplaceholder.typicode.com"
    file_name = "{}.csv".format(userId)

    res = requests.get("{}/users/{}".format(baseURL, userId))
    if res.status_code == 200:
        user = res.json()

        res = requests.get("{}/todos?userId={}".format(baseURL, userId))
        if res.status_code == 200:
            todos = res.json()
            with open(file_name, 'w', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile, quotechar='"',
                                    quoting=csv.QUOTE_ALL)

                for todo in todos:
                    writer.writerow([userId,
                                     user.get('username'),
                                     todo.get('completed'),
                                     todo.get('title')])
