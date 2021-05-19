#importing modules
from tkinter import *
from tkinter import filedialog


root=Tk()
root.title("File Transfer Interface")



#creating button to specify source folder
def browse_button():
    global folder_path
    source_filename=filedialog.askdirectory()
    folder_path.set(source_filename)
    print(source_filename)
    return source_filename

#creates a label and button to find the source folder the user would like to move files from
folder_path = StringVar()
instruction_label1 = Label(root,  text="Please select the source folder:")
instruction_label1.grid(row=0, column=0)
lbl1 = Label( root, textvariable=folder_path)
lbl1.grid(row=0, column=1)
button2=Button(text="Browse", command=browse_button).grid(row=0, column=2)


#creates a button to specify destination folder
def browse_button2():
    global folder_path2
    destination_filename=filedialog.askdirectory()
    folder_path2.set(destination_filename)
    print(destination_filename)
    return destination_filename

#creates a label and a button to find the destination folder the user would like to place the files in
folder_path2= StringVar()
instruction_label2= Label(root, text="Please select the destination folder:")
instruction_label2.grid(row=1, column=0)
lbl2= Label(root, textvariable=folder_path2)
lbl2.grid(row=1, column=1)

button3=Button(text="Browse", command=browse_button2).grid(row=1, column=2)

#Creates a button to move the files from the source folder to the destination folder

button4= Button(text= "Select to move recent files",  command= move()).grid(row=7, column=3)

                                


root.mainloop()
