import os 
import subprocess
import sys
import json

with open('inters.json', 'r') as json_file:
    data = json.load(json_file)

fichiertxt, *args = sys.argv
def exectute():
    with open('example.txt', 'r') as f:
        lines = f.readlines()
        interpreter = data[lines[0]][0]
        extention = data[lines[0]][1]

exectute()

