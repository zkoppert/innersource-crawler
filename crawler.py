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
        if repo is not None:
            # Get the repo topics as type dict and print them nicely

            #TODO: handle rate limiting
            try:
                repo_topic = repo.topics()
            except:
                print('skipping 404')
            else:
                if 'inner-source' in repo_topic.names:
                    print('{0}'.format(repo))
                    f.write(repo.name + '\n')
    f.close()