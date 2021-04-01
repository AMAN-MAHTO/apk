import uuid
import sqlite3
import sys
import os

data_path=os.path.dirname(sys.argv[0]).replace('/','\\\\')
#database connection
data = sqlite3.connect('data_path\\database.db')
data_cur = data.cursor()
print(uuid.uuid4())