#importing modules and the user interface I created
import os.path, time
from datetime import *




#sets the source and destination paths for moving the files
source= "/Users/Brittany Barnett/Desktop/WorkingFiles"

destination= "/Users/Brittany Barnett/Desktop/DestinationFiles"

#Creates a list of files from the specified directory
all_files=os.listdir(source)
import os.path,  time

#iterates through the list of files to retrieve the creation and modification times
for i in all_files:
        path=(source+i)
        creation_time= os.path.getctime (path)
        print(creation_time)
        mod_time=os.path.getmtime(path)
        print(mod_time)

#Captures a time exactly 24 hours prior to when the program is ran to compare with file creation times
import datetime
current_time= datetime.datetime.now()
cut_time= current_time - datetime.timedelta ( hours=24)
print(cut_time)

#Iterates through our list of files and creates a timestamp of the creation and modification times
for i in all_files:
        timestamp_creation= datetime.datetime.fromtimestamp(creation_time)
        timestamp_mod=datetime.datetime.fromtimestamp(mod_time)
        print(timestamp_creation)
        print(timestamp_mod)

#Moves all files if the creation or modification time is within the last 24 hours.
import shutil
for i in all_files:
        if cut_time <= (timestamp_creation) or (timestamp_mod):
                shutil.move(source+i, destination)
                print (source+i)
                
        
