#importing modules

import webbrowser
import os
from tkinter import *

#creating root
root= Tk()
root.title("Create your custom webpage")
root.geometry("500x500")

Label(root, text="Input text and click submit to create a custom web page").pack()
#creating a user input space and assigning the user input to a variable
v= StringVar()
myInput= Entry(root,textvariable= v).pack()


#Creating a function to create a webpage on submit
def myPage():
    import webbrowser
    import os
    f= open('NewFile22.html','w')
    html_template = "<html><body><h1>"+ (v.get()) +"</h1></body></html>"
    f.write(html_template)
    f.close()

    filename= 'file:///'+os.getcwd()+'/'+'NewFile22.html'

    f=webbrowser.open('NewFile22.html','r')
    print(f.read())

    
    


#Creating a button to create the webpage
CreateButton=Button(root, text="Create your webpage!", command=myPage, font="LUCIDA 15 bold").pack()


if __name__ == "__main__":
    root.mainloop()
