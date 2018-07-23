# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 15:27:15 2018

@author: RO389222
"""
from win32com.client import Dispatch

dbname = r'C:\PythonProgram\Dashboard\Database\Dashboard2.accdb'
accApp = Dispatch("Access.Application")
dbEngine = accApp.DBEngine
workspace = dbEngine.Workspaces(0)
dbLangGeneral = ';LANGID=0x0409;CP=1252;COUNTRY=0'
newdb = workspace.CreateDatabase(dbname, dbLangGeneral, 64)
accApp.DoCmd.CloseDatabase