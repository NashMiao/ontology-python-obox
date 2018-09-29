#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import git

from obox.exception.obox_exception import OBoxError, OBoxException


class Box:
    @staticmethod
    def git_clone(repo_url):
        repo_to_path = os.path.join(os.getcwd())
        print('Downloading...')
        try:
            git.Repo.clone_from(url=''.join(repo_url), to_path=repo_to_path, depth=1)
        except git.GitCommandError as e:
            read_error = 'Could not read from remote repository.'
            read_error_handle = 'Please make sure you network state, and the repository exists.'
            exist_error = 'already exists and is not an empty directory.'
            if read_error in str(e.args[2]):
                print(''.join([read_error, '\n', read_error_handle]))
            elif exist_error in str(e.args[2]):
                print('Error: Something already exists at the destination.')
            else:
                print(e.args[2])

    @staticmethod
    def init():
        repo_url = ['https://github.com/wdx7266/obox-init-default.git']
        Box.git_clone(repo_url)
        print('Unpacking...')
        
        print('Setting up...')

        print('Unbox successful. Enjoy it!')

    @staticmethod
    def get_repo_url(box_name: str):
        if re.match(r'^([a-zA-Z0-9-])+$', box_name):
            repo_url = ['https://github.com:wdx7266/ontology-', 'template', '.git']
        elif re.match(r'^([a-zA-Z0-9-])+/([a-zA-Z0-9-])+$', box_name) is None:
            repo_url = ['https://github.com/', 'template', '.git']
        else:
            raise OBoxException(OBoxError.invalid_box_name)
        return repo_url
