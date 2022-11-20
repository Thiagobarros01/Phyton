import pyautogui
import time
pyautogui.PAUSE = 2



pyautogui.press("win")
pyautogui.press("backspace")
pyautogui.write("meu computador")
pyautogui.press("enter")

pyautogui.click(x=786, y=140)
pyautogui.press("enter")
pyautogui.click(x=418, y=159)
pyautogui.rightClick(x=418, y=159)
pyautogui.click(x=527, y=572)
pyautogui.click(x=97, y=286)
pyautogui.click(x=237, y=424)
pyautogui.press("enter")
pyautogui.rightClick(x=672, y=302)
pyautogui.click(x=740, y=439)


time.sleep(3)
x = pyautogui.position()
print(x)                               
