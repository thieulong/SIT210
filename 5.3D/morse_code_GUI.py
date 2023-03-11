from PyQt5.QtWidgets import *
from PyQt5.QtGui import * 
import sys
import time
from text_to_morse import text_to_morse
from flash_LED import morse_flash, LED_off

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)
        title = "Led Control"
        self.setWindowTitle(title)
        self.setGeometry(0, 0, 500, 300)

        prompt = QLabel('Enter a message to convert to Morse code', self)
        prompt.setFont(QFont('Arial', 16))
        layout.addWidget(prompt, 0, 0, 1, 3)

        self.message_box = QLineEdit(self)
        self.message_box.setMinimumHeight(50)
        layout.addWidget(self.message_box, 1, 0, 1, 3)

        self.morse_msg = QLabel('Morse code:', self)
        self.morse_msg.setFont(QFont('Arial', 14))
        layout.addWidget(self.morse_msg, 2, 0, 1, 3)

        submit_button = QPushButton('Confirm', self)
        submit_button.clicked.connect(self.confirm)
        submit_button.resize(submit_button.sizeHint())
        submit_button.setMinimumHeight(50)
        layout.addWidget(submit_button, 3, 0)

        loop_button = QPushButton('Loop', self)
        loop_button.clicked.connect(self.loop)
        loop_button.resize(loop_button.sizeHint())
        loop_button.setMinimumHeight(50)
        layout.addWidget(loop_button, 3, 1)

        stop_button = QPushButton('Stop', self)
        stop_button.clicked.connect(self.stop)
        stop_button.resize(stop_button.sizeHint())
        stop_button.setMinimumHeight(50)
        layout.addWidget(stop_button, 3, 2)

        exit_button = QPushButton('Exit', self)
        exit_button.clicked.connect(self.exit)
        exit_button.resize(exit_button.sizeHint())
        exit_button.setMinimumHeight(50)
        layout.addWidget(exit_button, 4, 0, 1, 3)

    def confirm(self):
        input_text = self.message_box.text()
        morse_code = text_to_morse(input_text)
        msg = "Morse code: {}".format(morse_code)
        self.morse_msg.setText(msg)
        morse_flash(morse_code)

    def loop(self):
        input_text = self.message_box.text()
        morse_code = text_to_morse(input_text)
        msg = "Morse code: {}".format(morse_code)
        self.morse_msg.setText(msg)
        while True:
            morse_flash(morse_code)
            time.sleep(1)

    def stop(self):
        LED_off()

    def exit(self):
        QApplication.quit()



app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())


