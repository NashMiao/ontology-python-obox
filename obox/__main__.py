#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

import git
import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        description='An DApp template project management tool based on Ontology blockchain.')
    parser.add_argument('--unbox', type=str, help='Downloads a OBox， a pre-built Ontology DApp project.')
    args = parser.parse_args()
    return args


def clone(repo: str):
    repo_url = ['git@github.com:wdx7266/ontology-', 'template', '.git']
    repo_url[1] = repo
    repo_to_path = os.path.join(os.getcwd(), repo)
    print('Downloading...')
    try:
        git.Repo.clone_from(url=''.join(repo_url), to_path=repo_to_path, depth=1)
    except git.GitCommandError as e:
        read_error = 'Could not read from remote repository.'
        read_error_handle = 'Please make sure you network state, and the repository exists.'
        exist_error = 'already exists and is not an empty directory.'
        exist_error_handle = 'Please check your directory.'
        if read_error in str(e.args[2]):
            print(''.join([read_error, '\n', read_error_handle]))
        elif exist_error in str(e.args[2]):
            print(''.join([repo, ' ', exist_error, '\n', exist_error_handle]))
        else:
            print(e.args[2])


def run():
    args = parse_args()
    print(args)
    # clone(args.unbox)


if __name__ == '__main__':
    run()
