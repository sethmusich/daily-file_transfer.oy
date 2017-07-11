import shutil
import datetime
import time
import os
import time
import tkinter 
from tkinter import *
from tkinter import ttk
import sqlite3


root = Tk()

frame=ttk.Frame(root)
frame.pack()
frame.config(relief=RIDGE)
ttk.LabelFrame(root,height=30, width=250, text="Navigate With the Options Below:").pack()


#function for listing files to be moved


button = ttk.Button(root, text='Files created >24 hours ago')
button.pack()

folderA = '/Users/sethmusich/Desktop/daily_file_transfer/a'
source=os.listdir(folderA)

def folder_a():
    for file in source:
        print(file)

button.config(command=folder_a)





#function for listing files that have been moved


button = ttk.Button(root, text='Files created <24 hours ago')
button.pack()

folderB = '/Users/sethmusich/Desktop/daily_file_transfer/b'
sourceB=os.listdir(folderB)

def folder_b():
    for file in sourceB:
        print(file)

button.config(command=folder_b)




#sql functions


with sqlite3.connect('daily_transfer.db') as db:
    c = db.cursor()
    now = datetime.datetime.now
    c.executescript("CREATE TABLE IF NOT EXISTS Transfer_Times (Transfer TEXT); ")
    db.commit()    





#function for manually moving files

button=ttk.Button(root,text='Move Files created <24 Hours Ago')
button.pack()

sourcepath='/Users/sethmusich/Desktop/daily_file_transfer/a'
source=os.listdir(sourcepath)
destinationpath='/Users/sethmusich/Desktop/daily_file_transfer/b'



def callback():
    now = time.time()
    for files in os.listdir(sourcepath):
        src_name = os.path.join(sourcepath,files)
        dst_name = os.path.join(destinationpath,files)
        modified_time = os.path.getmtime(src_name)
        elapsed_time = now - modified_time
        if elapsed_time < 86400:
            shutil.move(src_name,dst_name)
            print(files)
            Tk.update(root)
            
    now = datetime.datetime.now()
    c.execute('INSERT INTO Transfer_Times VALUES(?)',(now.strftime('%Y-%m-%d %H:%M'),))                     
    db.commit()   



#c.execute('SELECT * FROM Transfer_Times ORDER BY Transfer Times DESC Limit 1')
c.execute('SELECT * FROM Transfer_Times ORDER BY Transfer DESC')
#c.execute('SELECT * FROM Transfer_Times DESC Limit 1')
Mod_time = c.fetchone()

label = ttk.Label(root, text="Your most recent migration:")
label.pack()
label = ttk.Label(root, text=Mod_time)
label.pack()

    
button.config(command=callback)






















    



