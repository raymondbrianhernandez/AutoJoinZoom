import os

import pyautogui
import schedule
import time

meet_id = input('Enter Meeting ID: ')
password = input('Enter Meeting password: ')
meet_time = input(
    'Enter everyday meeting time in 24hour format (eg: "15:30" for 3:30pm): ')
total_meet = input(
    'How long will the meeting last for ?(Answer in minutes eg:120 for 2 hours): ')

# just for confirmation
total_meet = int(total_meet)
meet_time = str(meet_time)


def zoom_auto_join():
    time.sleep(0.2)

    pyautogui.press('esc', interval=0.1)

    time.sleep(0.3)

    pyautogui.press('win', interval=0.5)
    pyautogui.write('zoom')
    time.sleep(2)
    pyautogui.press('enter', interval=0.5)

    time.sleep(10)

    x, y = pyautogui.locateCenterOnScreen('button.png', confidence=0.9)

    pyautogui.click(x, y)

    pyautogui.press('enter', interval=5)
    pyautogui.write(meet_id)
    pyautogui.press('enter', interval=5)

    pyautogui.write(password)
    pyautogui.press('enter', interval=10)

    print("Session has started and will continue for %s minutes" % total_meet)

    print('Hold (Ctrl+c) to exit the program ')

    # Total time of zoom session
    time.sleep(total_meet * 60)

    # closing Zoom
    os.system("TASKKILL /F /IM Zoom.exe")
    time.sleep(0.5)


# Every day at whatever time the user has entered.
schedule.every().day.at("%s" % meet_time).do(zoom_auto_join())
print("Scheduling everyday at ", meet_time)

# Infinite Loop so that the scheduled task keeps running
while True:

    # Check whether a scheduled task is pending to run or not
    schedule.run_pending()
    time.sleep(1)


if __name__ == "__main__":
    zoom_auto_join()
