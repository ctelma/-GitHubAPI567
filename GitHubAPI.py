'''
Created on September 20, 2018
@author: Caroline Telma
GitHubAPI.py program to pull repos and number of commits per repository for a user
I pledge my honor that I have abided by the Stevens Honor System.
'''

import requests
import json

def RepositoryNames(user_id):

    r = requests.get('https://api.github.com/users/' + user_id + '/repos')
    repos = []
    repo_data = json.loads(r.text)

    for info in repo_data:
        try:
            repos += [info.get('name')]
        except (AttributeError):
            print('Error: unable to find repos for this user')
            return []
    return repos


def CommitNumber(user_id, RepositoryName):

    r = requests.get('https://api.github.com/repos/' + user_id + '/' + RepositoryName + '/commits')
    commitData = json.loads(r.text)
    return len(commitData)


if __name__ == "__main__":
    username = input("Enter Github username: ")
    print("User: " + username)

    repos = RepositoryNames(username)

    if len(repos) > 0:
        for r in repos:
            print("Repo: " + r + " Number of Commits: " + str(CommitNumber(username, r)))
