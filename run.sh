#!/bin/bash
cd ~/projects/markdown-solutions/
source venv/bin/activate
pbpaste > inputs/temp.md
python markdown-converter.py
pbcopy < outputs/temp.html

