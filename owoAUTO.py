import pyautogui
import time

print('cliquer sur la zone de texte')
time.sleep(3)
print('Start !')

for x in range(10):
    time.sleep(0.5)
    pyautogui.write("owohunt")
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.write("owobattle")
    pyautogui.press('enter')
    time.sleep(15)
    print(f'il reste {str(10-x)} tours')
pyautogui.write("owozoo")
pyautogui.press('enter')
pyautogui.write("owoinv")
pyautogui.press('enter')
print('End !')