import sys
import pyodbc as db
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QTableWidget,QTableWidgetItem
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QComboBox,
        QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
        QLabel, QLineEdit, QMenu, QMenuBar, QSpinBox, QTextEdit,
        QVBoxLayout)
items=[]
a=[]
conn_str = (r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                      r'DBQ=C:\PythonProgram\Dashboard\Database\Dashboard3.accdb;')
dat = db.connect(conn_str)
cur = dat.cursor()
class App(QWidget):

    def __init__(self):
        super(App,self).__init__()
        self.title = 'Qt5 Window'
        self.left = 30
        self.top = 50
        self.width = 640
        self.height = 480
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        #self.textbox = QLineEdit(self)
        #self.textbox.move(20, 20)
        #self.textbox.resize(280,40)
        self.CreateTable()
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget) 
        self.setLayout(self.layout)
        button = QPushButton('Close Window', self)
        button.setToolTip('This is an example button')
        button.move(250,300) 
        button.clicked.connect(self.on_click)
        button = QPushButton('Refresh Data', self)
        button.move(350,300) 
        button.clicked.connect(self.Refresh)
        button = QPushButton('Insert Row', self)
        button.move(150,300) 
        button.clicked.connect(self.Insert)
        button = QPushButton('Save', self)
        button.move(50,300) 
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
        #self.tableWidget.doubleClicked.connect(self.on_click_Tb)
        self.tableWidget.cellChanged.connect(self.on_click_Tb)
        
    def CreateTable(self):
        self.tableWidget = QTableWidget()
        self.RefreshTable()
    def Insert(self):
        #cur.execute('insert into Release')
        self.tableWidget.insertRow(0)
        self.tableWidget.doubleClicked.connect(self.on_click_Tb)
    def on_click_Tb(self):
        #textboxValue = self.textbox.text()
        #print textboxValue
        #print 
        Flg='Y'
        print Flg
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            CurRow=currentQTableWidgetItem.row()
            Id=CurRow+1
            Field=currentQTableWidgetItem.column()
            Value = currentQTableWidgetItem.text()
            if(Field==0):
                EmpName=Value
                print EmpName
            elif(Field==1):
                Issue=Value
            elif(Field==2):
                Release=Value
            elif(Field==3):
                Email=Value
           # if (EmpName!='' or Issue!='' or Release!='' or Email!=''):
             #   str1= 'update Release set EmpName='+EmpName+', Issue='+Issue+', Release='+Release+', Email='+Email+'where ID='+Id
            #   print str1
           # elif (EmpName != '' or Issue != '' or Release != '' and Email == ''):
             #   str1= 'update Release set EmpName='+EmpName+', Issue='+Issue+', Release='+Release+'where ID='+Id
              #  print str1
            #elif (EmpName != '' or Issue != '' and Release == '' and Email == ''):
               # str1= 'update Release set EmpName='+EmpName+', Issue='+Issue+'where ID='+Id
                #print str1
                
    def on_click(self):
        buttonReply = QMessageBox.question(self, 'Alert', "Do you want to close the window?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        print(int(buttonReply))
        if buttonReply == QMessageBox.Yes:
            print('Yes ')
            self.close()
        else:
            print('No ')
    def Clk_Save(self):
        pass
        #print 'Clicked'
        #str1='update Release set EmpName='+EmpName+', Issue='+Issue+', Release='+Release+', Email='+Email+'where ID='+Id
       # print str1
       # if Flg is 'Y':
          #  print 'Flg'
          #  print str1
          #  cur.execute(str1)
          #  cur.commit()
       # else:
          #  print Flg
if __name__ == '__main__':
    EmpName='';Issue='';Release='';Email='';Flg='';Id='';str1=''
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

