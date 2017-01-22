# rename_files.py

import os


def rename_files():
    #step 1: find file names 
    file_list = os.listdir(r"/Users/HenryYu/Google Drive/Data Analyst Nanocourse/Python/Lesson 1/prank")
    print( file_list)

    saved_path = os.getcwd()
    print("Current Working Directory is " + saved_path)
    os.chdir(r"/Users/HenryYu/Google Drive/Data Analyst Nanocourse/Python/Lesson 1/prank")
    #step 2: rename files

    #start with a for loop
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789"))
        
rename_files()
