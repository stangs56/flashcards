from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MainMenu(QWidget):

    def __init__(self):

        super().__init__()

    def create(self):

        #create main window
        #left, top, width, height
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Main Menu')

        stacks = [0, 1, 2] #replace with method getting list of stackIDs

        fullList = QVBoxLayout()

        #layout the list of stacks
        for stack in stacks:
            row = QHBoxLayout()

            row.addStretch(1)
            #image would go here
            label = QLabel(self)
            #Needs to have dynamic pathing
            pixmap = QPixmap('example.jpg')
            resize_pixmap = pixmap.scaled(32, 32)
            label.setPixmap(resize_pixmap)
            row.addWidget(label)

            row.addStretch(5)

            study = QPushButton('Study')
            row.addWidget(study)

            edit = QPushButton('Edit')
            row.addWidget(edit)

            delete = QPushButton('Delete')
            row.addWidget(delete)

            row.addStretch(1)

            fullList.addStretch(1)
            fullList.addLayout(row)

        #add button for new stack
        fullList.addStretch(1)
        row = QHBoxLayout()
        addNew = QPushButton('Add new stack')
        row.addWidget(addNew)
        fullList.addLayout(row)

        #set the layout for the window to the vbox layout
        self.setLayout(fullList)

        self.show()
