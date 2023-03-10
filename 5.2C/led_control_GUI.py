from PyQt5.QtWidgets import *
import sys
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False)

blue_led = 2
green_led = 3
red_led = 4

GPIO.setup(blue_led, GPIO.OUT)
GPIO.setup(green_led, GPIO.OUT)
GPIO.setup(red_led, GPIO.OUT)

GPIO.output(red_led, GPIO.LOW)
GPIO.output(green_led, GPIO.LOW)
GPIO.output(blue_led, GPIO.LOW)

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)
        title = "Led Control"
        self.setWindowTitle(title)
        self.setGeometry(200, 200, 350, 200)

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
        exit_button.clicked.connect(self.closeEvent)
        exit_button.resize(exit_button.sizeHint())
        layout.addWidget(exit_button, 4, 2)

    def closeEvent(self, event):
        
        # Confirm window close
        reply = QMessageBox.question(self, 'Warning',
            "Close application will turn off all LEDs", QMessageBox.Yes |
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            GPIO.output(red_led, GPIO.LOW)
            GPIO.output(green_led, GPIO.LOW)
            GPIO.output(blue_led, GPIO.LOW)
            event.accept()
        else:
            event.ignore()

    def onClicked(self):
        radioButton = self.sender()
        if radioButton.isChecked():
            if radioButton.color == "RED":
                GPIO.output(red_led, GPIO.HIGH)
                GPIO.output(green_led, GPIO.LOW)
                GPIO.output(blue_led, GPIO.LOW)
                print("RED light is on")
            if radioButton.color == "GREEN":
                GPIO.output(red_led, GPIO.LOW)
                GPIO.output(green_led, GPIO.HIGH)
                GPIO.output(blue_led, GPIO.LOW)
                print("GREEN light is on")
            if radioButton.color == "BLUE":
                GPIO.output(red_led, GPIO.LOW)
                GPIO.output(green_led, GPIO.LOW)
                GPIO.output(blue_led, GPIO.HIGH)
                print("BLUE light is on")

app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())
