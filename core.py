import json
import os
import random
def AddInfo(*args):
    if(CheckFile(args[0]) == False):
        with open('data/'+args[0], "w") as write_file:
                json.dump(args[1], write_file,indent = 4)
                write_file.close()
    else:
        with open('data/'+args[0],'r+') as file:
            # First we load existing data into a dict.
            file_data = json.load(file)
            # Join new_dat3a with file_data
            file_data["data"].append(args[1])
            # Sets file's current position at offset.
            file.seek(0)
            # convert back to json.
            json.dump(file_data, file, indent = 4)
            file.close()
def EditarData(*args):
    with open('data/'+args[0], "w") as write_file:
        json.dump(args[1], write_file,indent = 4)
        write_file.close()
def LoadInfo(fileName):
    if(CheckFile(fileName) == True):
        with open('data/'+fileName, "r") as read_file:
            dicc = json.load(read_file)
        return dicc

def CheckFile(fileName):
    try:
        with open('data/'+fileName, 'r') as f:
            return True
    except FileNotFoundError as e:
        return False
    except IOError as e:
        return False
def RandomId():
    id=random.randint(1,999)