import uuid
import sqlite3
import sys
import os
from datetime import datetime
from qrcode import make
from pyzbar.pyzbar import decode
import numpy
import cv2
data_path=os.path.dirname(sys.argv[0]).replace('/','\\\\')
    #database connection
data = sqlite3.connect('database.db')
data_cur = data.cursor()

def getting_id():
    return [i for i in data_cur.execute("SELECT ID from user_details")]

def QR_genrator(string,file_name):
    make(string).save(f'{file_name}.jpg')

def add_user(name,ph):
    m_date = str(datetime.today().date())    #today date as manufacture date
    y=m_date.split('-')
    e_date=str(int(y[0])+1)+'-'+y[1]+'-'+y[2] #expire date 
    #genrating id or adding in database
    sumbited = False
    while sumbited==False:
        genrated_id = str(uuid.uuid4())
        if tuple(genrated_id) not in getting_id():
            data_cur.execute("INSERT INTO user_details(ID,Name,M_date,E_date,Ph) VALUES(?,?,?,?,?);",(genrated_id,name,m_date,e_date,ph))
            data.commit()
            QR_genrator(genrated_id,ph)
            sumbited=True

def QR_scanner():
    i=0
    cap = cv2.VideoCapture(0)
    decoded=False
    while decoded==False:
        _,img = cap.read()
        for obj in decode(img):
            scanned_data=obj.data.decode('utf-8')
            decoded=True
        cv2.imshow("Qrcode scanner",img)
        cv2.waitKey(1)
        
    if (scanned_data,) in getting_id():
        cv2.destroyWindow('Qrcode scanner')
        user_details_find=[i for i in data_cur.execute(f"SELECT * from user_details WHERE ID = {scanned_data}")]
        
    else:
        cv2.destroyWindow('Qrcode scanner')
        user_details_find=None
        
    return user_details_find
 

if __name__ == '__main__':
    
    print(QR_scanner())
    
