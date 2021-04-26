# "pip install sqlite" in terminal
import sqlite3
from datetime import datetime
import tkinter as tk
from tkinter import filedialog
from zipfile import ZipFile

root=tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()
file = str(file_path)
ZipFile('archive.zip', 'w').write(file)

time = datetime.now().strftime("%B %d, %Y %I:%M%p")
connection = sqlite3.connect('DataBase.db')
cursor =connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS uploder (ID INTEGER PRIMARY KEY AUTOINCREMENT , datetime date ,filename VARCHAR );''')
cursor.execute("INSERT INTO uploder (datetime , filename) VALUES (?,?);",(time,file))


connection.commit()
connection.close()
