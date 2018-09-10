#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

import git
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='An DApp template project management tool based on Ontology blockchain.')
    parser.add_argument('--install', '-i', type=str, help='install a DApp template project into local environment.')
    args = parser.parse_args()
    repo_url = ['git@github.com:wdx7266/ontology-', 'template', '.git']
    repo_url[1] = args.install
    repo_to_path = os.path.join(os.getcwd(), args.install)
    new_repo = git.Repo.clone_from(url=''.join(repo_url), to_path=repo_to_path, depth=1)
