#importing modules
from tkinter import *
from tkinter import filedialog
import os
import datetime
import shutil


root=Tk()
root.title("File Transfer Interface")
root.geometry("500x500")

def CheckFiles():
    #grabs the path from the sourceEntry widget
    source = sourceEntry.get()
    #grabs the path from the destEntry widget
    destination = destEntry.get()
    #Creates a list of files from the specified directory
    all_files=os.listdir(source)

    #iterates through the list of files
    for i in all_files:
        path=(source + '/' + i)

        #gets the modification time of the file
        mod_time=os.path.getmtime(path)

        #converts the mod_time to a proper datetime variable
        modification_time = datetime.datetime.fromtimestamp(mod_time)
       
        #gets the time 24 hours ago
        twentyFour = datetime.datetime.now() - datetime.timedelta(hours = 24)

        #if the modification was within the last 24 hours, move the files
        if modification_time > twentyFour:
            shutil.move(source + '/' + i, destination)


#creating button to specify source folder
def browse_button():
    source_filename=filedialog.askdirectory()
    sourceEntry.delete(0, END)
    sourceEntry.insert(0, source_filename)

#creates a label and button to find the source folder the user would like to move files from
instruction_label1 = Label(root,  text="Please select the source folder:")
instruction_label1.grid(row=0, column=0)
lbl1 = Label ( root)
lbl1.grid(row=0,  column=1)
button2=Button(text="Browse", command=browse_button).grid(row=0, column=3)

#Entry widget to hold the source path
sourceEntry= Entry(root)
sourceEntry.grid( row=0, column=2)


#creates a button to specify destination folder
def browse_button2():
   destination_filename=filedialog.askdirectory()
   destEntry.delete(0,  END)
   destEntry.insert(0,destination_filename)

#creates a label and a button to find the destination folder the user would like to place the files in
instruction_label2= Label(root, text="Please select the destination folder:")
instruction_label2.grid(row=1, column=0)
lbl2= Label(root)
lbl2.grid(row=1, column=1)
button3=Button(text="Browse", command=browse_button2).grid(row=1, column=3)

#Entry widget to hold the destination path
destEntry= Entry(root)
destEntry.grid( row=1, column=2)

#Creates a button to move the files from the source folder to the destination folder

button4= Button(text= "Select to move recent files",  command= lambda:CheckFiles()).grid(row=7, column=3)

                                


root.mainloop()
