#!/usr/bin/env python

import github3
import os
from os.path import join, dirname
from dotenv import load_dotenv


if __name__ == '__main__':
 
    # Load env variables from file
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)

    # Auth to GitHub.com
    gh = github3.login(token=os.getenv('GH_TOKEN'))
    
    # Get all repos from organization
    all_repos = gh.repositories()

    # TODO: Gather metadata for each repo

    # TODO: Write each repository to a repos.json file
    f = open("repos.json", "x")
    for repo in all_repos:
        f.write(repo.name + '\n')
        #for topic in repo.topics():
            #if topic == 'inner-source':
            #    f.write(repo.name + '\n')
    f.close()
