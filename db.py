# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 13:50:45 2018

@author: RO389222
"""
import pyodbc as db
b=[]
conn_str = (r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                      r'DBQ=C:\PythonProgram\Dashboard\Database\Dashboard.accdb;')
dat = db.connect(conn_str)
cur = dat.cursor()
cur.execute('select EmpName,Issues,Release,Email from Release')
for vals in cur.fetchall():
    print vals
#print b[0]
#cur.execute("insert into Release(EmpName,Issues,Release,Email) values ('New','9','R3','Test.com')")
#cur.commit()