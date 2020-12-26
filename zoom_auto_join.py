"""
    Automatic Zoom Hosting
    Raymond Hernandez
    December 25, 2020
"""
import os
import cv2
import pyautogui
import time
import schedule
import sys
from gui import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication


# TODO: Make this list imported from a file
meeting_ID = ["test_ID", "82807141026"]
password = ["test_pass", "120628"]
index = 0

class GUI(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(GUI, self).__init__(parent)
        self.setupUi(self)

        self.start_host.clicked.connect(self.start_auto_host)
        self.start_join.clicked.connect(self.start_auto_join)

    def start_auto_host(self):
        self.label_3.setText("Auto-host mode started...")
        new_meetings_schedule()

    def start_auto_join(self):
        self.label_3.setText("Auto-join mode started...")
        join_meetings_schedule()


class AutoZoom:
    def __init__(self, ID=None, passcode=None, duration=None):
        self.duration = duration
        self.meeting_ID = ID
        self.password = passcode

    def start_meeting(self):
        time.sleep(0.2)
        pyautogui.press('esc', interval=0.1)
        time.sleep(0.3)
        pyautogui.press('win', interval=0.5)
        pyautogui.write('zoom')
        time.sleep(1)
        pyautogui.press('enter', interval=0.5)
        time.sleep(1)

        # Press "New Meeting"
        img = cv2.imread(r"button_new_meeting.PNG")
        x, y = pyautogui.locateCenterOnScreen(img, confidence=0.9)
        pyautogui.click(x, y)
        pyautogui.press('enter', interval=10)

        # Press "Participants"
        img = cv2.imread(r"button_participants.PNG")
        x, y = pyautogui.locateCenterOnScreen(img, confidence=0.9)
        pyautogui.click(x, y)
        pyautogui.press('enter', interval=2)

        # Press "More Options"
        img = cv2.imread(r"button_more_options.PNG")
        x, y = pyautogui.locateCenterOnScreen(img, confidence=0.9)
        pyautogui.click(x, y)
        pyautogui.press('enter', interval=2)

        # Press "Disable Waiting Room"
        img = cv2.imread(r"button_waiting_room.PNG")
        x, y = pyautogui.locateCenterOnScreen(img, confidence=0.9)
        pyautogui.click(x, y)
        pyautogui.press('enter', interval=.5)

        # Press "More Options"
        img = cv2.imread(r"button_more_options.PNG")
        x, y = pyautogui.locateCenterOnScreen(img, confidence=0.9)
        pyautogui.click(x, y)
        pyautogui.press('enter', interval=.5)

        # Press "Mute All"
        img = cv2.imread(r"button_mute_all.PNG")
        x, y = pyautogui.locateCenterOnScreen(img, confidence=0.9)
        pyautogui.click(x, y)
        pyautogui.press('enter', interval=.5)

        # Ending the meeting
        time.sleep(self.duration * 60)
        os.system("TASKKILL /F /IM Zoom.exe")
        time.sleep(0.5)

    def join_meeting(self):
        time.sleep(0.2)
        pyautogui.press('esc', interval=0.1)
        time.sleep(0.3)
        pyautogui.press('win', interval=0.5)
        pyautogui.write('zoom')
        time.sleep(1)
        pyautogui.press('enter', interval=0.5)
        time.sleep(1)

        # Press "Join Meeting"
        img = cv2.imread(r"button_join.PNG")
        x, y = pyautogui.locateCenterOnScreen(img, confidence=0.9)
        pyautogui.click(x, y)

        pyautogui.press('enter', interval=2)
        pyautogui.write(self.meeting_ID)
        pyautogui.press('enter', interval=2)

        pyautogui.write(self.password)
        pyautogui.press('enter', interval=2)

        # Ending the meeting
        time.sleep(self.duration * 60)
        os.system("TASKKILL /F /IM Zoom.exe")
        time.sleep(0.5)

def new_meetings_schedule():
    zoom = AutoZoom(duration=200)

    """" Enable this to test """
    zoom.start_meeting()

    """ Real schedule here... """
    schedule.every().tuesday.at("09:00").do(zoom.start_meeting)
    schedule.every().wednesday.at("09:00").do(zoom.start_meeting)
    schedule.every().thursday.at("09:00").do(zoom.start_meeting)
    schedule.every().sunday.at("09:00").do(zoom.start_meeting)

    while True:
        schedule.run_pending()
        time.sleep(1)

def join_meetings_schedule():
    zoom = AutoZoom(ID=meeting_ID[index], passcode=password[index], duration=140)

    """ Enable this to test or when using in GUI """
    zoom.join_meeting()

    """ Real schedule here... """
    schedule.every().friday.at("18:30").do(zoom.join_meeting)
    schedule.every().saturday.at("09:30").do(zoom.join_meeting)
    schedule.every().sunday.at("15:30").do(zoom.join_meeting)

    while True:
        schedule.run_pending()
        time.sleep(1)


def main():
    # new_meetings_schedule()
    join_meetings_schedule()

    # app = QApplication(sys.argv)
    # form = GUI()
    # form.show()
    # app.exec_()


if __name__ == "__main__":
    main()
