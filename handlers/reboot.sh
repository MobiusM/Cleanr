#!/bin/bash

pkill -f "main.py"
git checkout master > ~/cleanr.log
git pull origin master >> ~/cleanr.log
python3 ~/Cleanr/main.py >> ~/cleanr.log 2>&1 &disown

