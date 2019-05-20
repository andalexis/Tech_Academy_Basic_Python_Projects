

import sqlite3

import re


# conn is going to hold our connection
conn = sqlite3.connect('drill.db')

fileList = ('information.docx','Hello.txt','myImage.png',\
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

# find matches within the list of file names
def findMatch():
    for i in fileList:
        if i.endswith('.txt'):
            matches = i
            print(matches)
            insertData(matches)
            

# insert data
def insertData(matches):
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_file(col_dtype) VALUES (?)", \
          (matches,))
    conn.commit()
    



# create database for drill
def createDB():
    conn = sqlite3.connect('drill.db')
    with conn:
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS tbl_file(\
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_dtype TEXT \
            )''')
        conn.commit()
    conn.close()
    findMatch()
    




createDB()





# read through the list and extract the ones that end in txt
# then insert those values into the table

    
