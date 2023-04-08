#!/usr/bin/env python

import os
import datetime

path = os.getcwd() # Gets current working directory

# Get a list of files in the current working directory
files = os.listdir()

file_list = [] # Creates an empty list to hold the dictionaries

# Loop through each file and add its information to the list
for file in files:
    # Use os.path module to get information about the file
    path = os.path.abspath(file)
    size = os.path.getsize(file)
    created = os.path.getctime(file)
    modified = os.path.getmtime(file)


    #path = os.path.abspath(file)
    #size = os.path.getsize(file)
    #created = datetime.datetime.fromtimestamp(os.path.getctime(file)).strftime('%Y-%m-%d %H:%M:%S')
    #modified = datetime.datetime.fromtimestamp(os.path.getmtime(file)).strftime('%Y-%m-%d %H:%M:%S')
    
    # Create a dictionary containing the file information
    file_dict = {
        "Filename": file,
        "Path": path,
        "Size in bytes": size,
        "Created": created,
        "Modified": modified
    }
    
    # Add the dictionary to the file_list
    file_list.append(file_dict)


# Print the list of dictionaries
print(*file_list, sep="\n")

