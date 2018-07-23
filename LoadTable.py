import sys
import subprocess
import pyodbc as db
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QTableWidget,QTableWidgetItem
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QComboBox,
        QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
        QLabel, QLineEdit, QMenu, QMenuBar, QSpinBox, QTextEdit,
        QVBoxLayout)
from pandas import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from matplotlib import pyplot as plot 
from win32com.client import Dispatch
EmpName=''
Issue=0
Release=''
Email=''
Flg=''
Id=0
str1=''
str2=''
items=[]
a=[]
InsFlg=''
conn_str = (r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                      r'DBQ=C:\PythonProgram\Dashboard\Database\Dashboard.accdb;')
accApp = Dispatch("Access.Application")
dbEngine = accApp.DBEngine
workspace = dbEngine.Workspaces(0)
dbname = r'C:\PythonProgram\Dashboard\Database\Dashboard.accdb'
dbLangGeneral = ';LANGID=0x0409;CP=1252;COUNTRY=0'
try:
    newdb = workspace.CreateDatabase(dbname, dbLangGeneral, 64)
    newdb.Execute("""CREATE TABLE Release (
                      ID autoincrement,
                      EmpName varchar(50),
                      Issues int,
                      Release varchar(50),
                      Email varchar(150));""")
    accApp.DoCmd.CloseDatabase
    accApp.Quit
    cmdCommand = "taskkill /f /im MSaccess.exe"   #specify your cmd command
    process = subprocess.Popen(cmdCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    dat = db.connect(conn_str)
    cur = dat.cursor()
    cur.execute("insert into Release(EmpName,Issues,Release,Email) values ('New','9','R3','Test.com')")
    cur.execute("insert into Release(EmpName,Issues,Release,Email) values ('New2','15','R3','Test.com')")
    cur.commit
except:
    dat = db.connect(conn_str)
    cur = dat.cursor()
class App(QWidget):

    def __init__(self):
        super(App,self).__init__()
        self.title = 'Qt5 Window'
        self.left = 30
        self.top = 50
        self.width = 1300
        self.height = 700
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        #self.textbox = QLineEdit(self)
        #self.textbox.move(20, 20)
        #self.textbox.resize(280,40)
        self.CreateTable()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.layout.addWidget(self.tableWidget) 
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.layout.addWidget(self.toolbar)
        self.layout.addWidget(self.canvas)
        #self.LoadChart()mself
        button = QPushButton('Load Chart',self)
        button.move(450,660) 
        button.clicked.connect(self.LoadChart)
        button = QPushButton('Close Window', self)
        button.move(250,660) 
        button.clicked.connect(self.on_click)
        button = QPushButton('Refresh Data', self)
        button.move(350,660) 
        button.clicked.connect(self.Refresh)
        button = QPushButton('Insert Row', self)
        button.move(150,660) 
        button.clicked.connect(self.Insert)
        button = QPushButton('Save', self)
        button.move(50,660) 
        button.clicked.connect(self.Clk_Save)
        self.show()
    def Refresh(self):
        self.RefreshTable()
    def RefreshTable(self):
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(['EmpName', 'Issue', 'Release', 'Email'])
        cur.execute('select * from Release')
        all_data = cur.fetchall()
        for i ,item in enumerate(all_data):
            Id=QTableWidgetItem(str(item[0]))
            EmpName = QTableWidgetItem(str(item[1]))
            Issue = QTableWidgetItem(str(item[2]))
            Release = QTableWidgetItem(str(item[3]))
            Email = QTableWidgetItem(str(item[4]))
            self.tableWidget.setItem(i, 0, EmpName)
            self.tableWidget.setItem(i, 1, Issue)
            self.tableWidget.setItem(i, 2, Release)
            self.tableWidget.setItem(i, 3, Email)
            self.tableWidget.move(0,0)
        self.tableWidget.cellChanged.connect(self.on_click_Tb)
    def LoadChart(self):
        res= cur.execute('select * from Release')
        all_data = cur.fetchall()
        header=[]
        data=[]
        values=[]
        ax = self.figure.add_subplot(111)
        for head in res.description:
            header.append(head[0])
        for vals in all_data:
            values.append(list(vals))
            data.append(dict(zip(header,vals)))
        stream = DataFrame(data)
        itemlst=[]
        x=[]
        y=[]
        for items in values[0:]:
            x.append(items[2])
            y.append(items[1])
        #ax.xlabel("EmpName")
        #ax.ylabel("Issues")   
        ax.bar(y, x, align = 'center') 
        self.canvas.draw()
    def CreateTable(self):
        self.tableWidget = QTableWidget()
        self.RefreshTable()
    def Insert(self):
        #cur.execute('insert into Release')
        global InsFlg
        InsFlg='Y'
        self.tableWidget.insertRow(0)
        self.tableWidget.doubleClicked.connect(self.on_click_Tb)
    def on_click_Tb(self):
        #textboxValue = self.textbox.text()
        #print textboxValue
        global Flg
        global str1
        global str2
        global Id
        global InsFlg
        Flg='Y'
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            CurRow=currentQTableWidgetItem.row()
            Id=CurRow+1
            Field=currentQTableWidgetItem.column()
            Value = currentQTableWidgetItem.text()
            if(Field==0):
                global EmpName
                EmpName=Value
            elif(Field==1):
                global Issue
                Issue=int(Value)
            elif(Field==2):
                global Release
                Release=Value
            elif(Field==3):
                global Email
                Email=Value
            if InsFlg != 'Y':
                if (EmpName!='' and Issue!='' and Release!='' and Email!=''):
                    str1="update Release set EmpName='"+EmpName+"', Email='"+Email+"', Issues=%d"%Issue+", Relaease='"+Release+"' where ID=%d"%Id
                elif (EmpName != '' and Issue != '' and Release != '' and Email == ''):
                    str1="update Release set EmpName='"+EmpName+"', Issues=%d"%Issue+", Relaease='"+Release+"' where ID=%d"%Id
                elif (EmpName != '' or Issue != '' and Release == '' and Email == ''):
                    str1="update Release set EmpName='"+EmpName+"', Issues=%d"%Issue+" where ID=%d"%Id
                elif (EmpName != '' or Issue == '' and Release == '' and Email == ''):
                    str1="update Release set EmpName='"+EmpName+"' where ID=%d"%Id
            if(InsFlg=='Y'):
                str1="insert into Release(EmpName,Issues,Release,Email) values ('"+EmpName+"',%d"%Issue+",'"+Release+"','"+Email+"')"
    def on_click(self):
        buttonReply = QMessageBox.question(self, 'Alert', "Do you want to close the window?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            cur.commit()
            cur.close()
            self.close()
        else:
            pass
    def Clk_Save(self):
        global Flg
        global str1
        if Flg is 'Y':
            cur.execute(str1)
            cur.commit()
        else:
            pass
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

