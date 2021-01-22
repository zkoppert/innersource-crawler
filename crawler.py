#!/usr/bin/env python

import json
import os
from os.path import dirname, join

import github3
from dotenv import load_dotenv

if __name__ == "__main__":

    # Load env variables from file
    dotenv_path = join(dirname(__file__), ".env")
    load_dotenv(dotenv_path)

    # Auth to GitHub.com
    gh = github3.login(token=os.getenv("GH_TOKEN"))

    # Set the topic
    topic = os.getenv("TOPIC")
    organization = os.getenv("ORGANIZATION")
    
    # Get all repos from organization
    search_string = "org:" + organization + " topic:" + topic
    all_repos = gh.search_repositories(search_string)
    repo_list = []

    for repo in all_repos:
        if repo is not None:
            # TODO: #7 For each resulting project add a key _InnerSourceMetadata
            print("{0}".format(repo.repository))
            full_repository = repo.repository.refresh()
            # Add stuff here about innersource.json data before appending to list
            repo_list.append(repo.as_dict())

    # Write each repository to a repos.json file
    with open("repos.json", "w") as f:
        json.dump(repo_list, f, indent=4)
