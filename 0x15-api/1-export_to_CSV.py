#!/usr/bin/python3

"""
"""
from requests import get
from sys import argv


if __name__ == '__main__':
    USER_ID = argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(USER_ID)
    response = get(url)
    USERNAME = response.json().get('username')

    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(USER_ID)
    response = get(url)
    tasks = response.json()
    with open('{}.csv'.format(USER_ID), 'w') as file:
        for TASK in tasks:
            file.write('"{}","{}","{}","{}"\n'
                       .format(USER_ID, USERNAME, TASK.get('completed'),
                               TASK.get('title')))
