#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

import re
import git
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='An Ontology development framework.')
    parser.add_argument('--unbox', type=str, help='Downloads a OBox， a pre-built Ontology DApp project.')
    parser.add_argument('--init', type=str, help='Initialize new and empty Ontology DApp project.')
    parser.add_argument('--compile', type=str, help='Compile contract source files.')
    args = parser.parse_args()
    return args


def run():
    args = parse_args()
    print(args.init)
    # clone(args.unbox)


if __name__ == '__main__':
    run()
