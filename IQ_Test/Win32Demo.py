import win32api
import win32gui
import win32con
import os
import time

IQ_BAT_FILE_NAME = r'IQ.bat'
IQ_BAT_TITLE_NAME = r'ROKU_WIFI'

os.startfile(IQ_BAT_FILE_NAME)
time.sleep(1)
hwnd = win32gui.FindWindow('ConsoleWindowClass', IQ_BAT_TITLE_NAME)
time.sleep(2)
win32gui.ShowWindow(hwnd, False)
time.sleep(10)
win32api.SendMessage(hwnd, win32con.WM_CLOSE)
