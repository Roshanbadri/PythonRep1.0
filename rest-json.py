# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 11:05:30 2018

@author: RO389222
"""

import requests as req

resp = req.get('http://localhost:8080/users/')
if resp.status_code != 200:
    # This means something went wrong.
    #raise ApiError('GET /tasks/ {}'.format(resp.status_code))
    #lst = resp.raw
    #print lst
    #pass
    print "test"
    data= resp.json()
    print resp.encoding
    #for todo_item in resp.json():
        #print('{} {}'.format(todo_item['BuildNumber'], todo_item['Variant']))
     #   print "test"

#task = {"summary": "Take out trash", "description": "" }
#resp = req.post('https://todolist.example.com/tasks/', json=task)
# The equivalent longer version
#resp = requests.post('https://todolist.example.com/tasks/',
 #                    data=json.dumps(task),
  #                   headers={'Content-Type':'application/json'}
if resp.status_code != 201:
    #raise ApiError('POST /tasks/ {}'.format(resp.status_code))
    print "Error",resp.status_code
    #pass
#print('Created task. ID: {}'.format(resp.json()["id"]))