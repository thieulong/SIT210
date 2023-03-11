from PyQt5.QtWidgets import *
from PyQt5.QtGui import * 
import sys
import time
from text_to_morse import text_to_morse
from flash_LED import morse_flash

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)
        title = "Led Control"
        self.setWindowTitle(title)
        self.setGeometry(200, 200, 500, 300)

        prompt = QLabel('Enter a message to convert to Morse code', self)
        prompt.setFont(QFont('Arial', 16))
        layout.addWidget(prompt, 0, 0, 1, 1)

        self.message_box = QLineEdit(self)
        self.message_box.setMinimumHeight(50)
        layout.addWidget(self.message_box, 1, 0, 1, 1)

        self.morse_msg = QLabel('Morse code:', self)
        self.morse_msg.setFont(QFont('Arial', 14))
        layout.addWidget(self.morse_msg, 2, 0, 1, 1)

        submit_button = QPushButton('Confirm', self)
        submit_button.clicked.connect(self.confirm)
        submit_button.resize(submit_button.sizeHint())
        submit_button.setMinimumHeight(50)
        layout.addWidget(submit_button, 3, 0)

        exit_button = QPushButton('Exit', self)
        exit_button.clicked.connect(self.exit)
        exit_button.resize(exit_button.sizeHint())
        exit_button.setMinimumHeight(50)
        layout.addWidget(exit_button, 4, 0, 1, 1)

    def confirm(self):
        input_text = self.message_box.text()
        morse_code = text_to_morse(input_text)
        self.morse_msg.setText("Morse code: {}".format(morse_code))
        morse_flash(morse_code)

    def exit(self):
        QApplication.quit()



app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())


