#!/bin/bash

pkill -f "python3 main.py"
python3 ~/Cleanr/main.py > ~/cleanr.log 2>&1 &disown

