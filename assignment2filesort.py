#importing modules and the user interface I created
import os.path, time
from datetime import *
import datetime
import shutil



def CheckFiles():
        #grabs the path from the sourceEntry widget
        source = sourceEntry.get()
        #grabs the path from the destEntry widget
        destination= destEntry.get()
        #Creates a list of files from the specified directory
        all_files=os.listdir(source)

        #iterates through the list of files
        for i in all_files:
                path=(source + '/' +i)

                #gets the modification time of the file
                mod_time=os.path.getmtime(path)

                #converts the mod_time to a proper datetime variable
                modification_time = datetime.datetime.fromtimestamp(mod_time)

                #gets the time 24 hours ago
                twentyFour = datetime.now() - datetime.timedelta(hours = 24)

                #if the modification was within the last 24 hours, move the files
                if modification_time > twentyFour:
                        shutil.move(source + '/' + i, destination)                
        
