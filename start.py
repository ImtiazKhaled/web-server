import json
import os

with open('package.json') as file:
    data = json.load(file)
    command = ''
    for i in data["dependencies"]:
        command += 'pip3 install ' + i + " --user\n"
    
os.system(command)
