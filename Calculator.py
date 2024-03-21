import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QComboBox, QGraphicsEffect

def addition(x,y):
        return x+y

def substraction(x,y):
    return x-y

def division(x,y):
    return x/y

def multiplication(x,y):
    return x*y
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.central_widget= QWidget()
        self.setCentralWidget(self.central_widget)
        layout=QVBoxLayout(self.central_widget)
        self.entry1=QLineEdit()#create a line
        self.entry1.setFixedWidth(120)
        self.entry1.setFixedHeight(120)
        layout.addWidget(self.entry1)#adds the entry to the window
        self.entry2=QLineEdit()
        self.entry2.setFixedWidth(120)
        self.entry2.setFixedHeight(120)
        layout.addWidget(self.entry2)#adds the entry to the window
        
        self.operations=['+','-','*','/']
        self.operation_menu=QComboBox()
        self.operation_menu.addItems(self.operations)
        layout.addWidget(self.operation_menu)
        self.button=QPushButton('EQUALS')
        self.button.clicked.connect(self.calculate)
        layout.addWidget(self.button)
        
        self.label=QLabel()
        layout.addWidget(self.label)
    
        self.change_font(20)
        self.apply_stylesheet()
        
        self.setGeometry(120,120,700,400)


    def apply_stylesheet(self):
        stylesheet="""QMainWindow{ background-color:black}
        QPushButton{background-color:white; color:dark gray;padding:8px 16px;border:none;border-radius:4px;font-size:16px}
        QLineEdit,QComBox,QLabel{ background-color:  pink;border 1px solid green; border-radius:4px;padding 6px 10px:font-size:18px}
        """
        self.setStyleSheet(stylesheet)
        self.entry1.setStyleSheet("""
            QLineEdit {
                background-color: light green;
                border: 1px solid light green; 
            }
        """)
        self.entry2.setStyleSheet("""
            QLineEdit {
                background-color: light green;
                border: 2px solid light green; 
            }
        """)
    
    
    def change_font(self,size):
        font=self.font()
        font.setPointSize(size)
        self.setFont(font)
        self.entry1.setFont(font)
        self.entry2.setFont(font)
        self.operation_menu.setFont(font)
        self.button.setFont(font)
        self.label.setFont(font)
    
    
    def calculate(self):
        x=float(self.entry1.text())
        y=float(self.entry2.text())
        operation=self.operation_menu.currentText()
        if operation=='+':
            result=addition(x,y)
        elif operation=='-':
            result=substraction(x,y)
        elif operation=='*':
            result=multiplication(x,y)
        elif operation=='/':
            result=division(x,y)
        self.label.setText(f"Result: {result}")
        
if __name__=="__main__":
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())