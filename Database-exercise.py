import sqlite3

conn=sqlite3.connect('test2.db')

with conn:
    cur= conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_file(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT,\
        col_fname TEXT)")
    conn.commit()

conn = sqlite3.connect('test2.db')
#adding the tuple of files
fileList = ('information.docx','Hello.txt', 'myImage.png'\
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

# loops through each object in the tuple to find the files that end in .txt
for x in fileList:
    if x.endswith('.txt'):
        with conn:
            cur= conn.cursor()
            cur.execute("INSERT INTO tbl_file(col_fname) VALUES (?)",(x,))
            print(x)

conn.close()
