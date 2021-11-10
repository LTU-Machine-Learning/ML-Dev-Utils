#!/bin/bash

mkdir -p /home/vscode/workspace/tmp
nohup /usr/bin/python -u /home/vscode/workspace/src/check/check_background_run.py > tmp/check_background_run.log &
