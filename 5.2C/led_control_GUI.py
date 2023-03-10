from PyQt5.QtWidgets import *
import sys

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)
        title = "Led Control"
        self.setWindowTitle(title)
        self.setGeometry(10, 10, 350, 200)

        label = QLabel('Choose a LED to turn on', self)
        layout.addWidget(label, 0, 1)

        radiobutton = QRadioButton("RED")
        radiobutton.setChecked(True)
        radiobutton.color = "RED"
        radiobutton.toggled.connect(self.onClicked)
        layout.addWidget(radiobutton, 1, 1)

        radiobutton = QRadioButton("GREEN")
        radiobutton.color = "GREEN"
        radiobutton.toggled.connect(self.onClicked)
        layout.addWidget(radiobutton, 2, 1)

        radiobutton = QRadioButton("BLUE")
        radiobutton.color = "BLUE"
        radiobutton.toggled.connect(self.onClicked)
        layout.addWidget(radiobutton, 3, 1)

        exit_button = QPushButton('Exit', self)
        exit_button.clicked.connect(QApplication.instance().quit)
        exit_button.resize(exit_button.sizeHint())
        layout.addWidget(exit_button, 4, 2)

    def onClicked(self):
        radioButton = self.sender()
        if radioButton.isChecked():
            print("Current LED on is %s" % (radioButton.color))

app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())