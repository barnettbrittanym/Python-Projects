#Creating the html file in Python
import webbrowser
import os

#To open/create a new html file in write mode
f= open('SummerSale.html', 'w')

#The html code that will go in the file
html_template= """
<html>
    <body>
        <h1>
Stay tuned for our amazing summer sale!
        </h1>
    </body>
</html>
"""
#writing the code into the file
f.write(html_template)
f.close()

filename = 'file:///'+os.getcwd()+'/'+'SummerSale.html'
webbrowser.open_new_tab(filename)
