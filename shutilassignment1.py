import shutil
import os

#set where the source of the files are
source= '/Users/Brittany Barnett/Desktop/Folder A/'

#set the destination path to folder B
destination = '/Users/Brittany Barnett/Desktop/Folder B/'
files= os.listdir(source)

for i in files:
    #we are saying mobe the files represented by 'i' to their new destination
    shutil.move(source+i, destination)
