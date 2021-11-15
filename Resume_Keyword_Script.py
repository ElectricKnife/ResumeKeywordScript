import pyautogui
import time
import os

for i in range(100):
    print('.')

category = input("Biotech:1, Hardware:2, Medical:3, Robotics:4, Robotics/Medical:5 -- Input value: ")

parent_dir = "C:/Users/faroo/Documents/Work/"

while True:
    if int(category) in range(6):
        if category == '1':
            directory = "Biotech"
        elif category == '2':
            directory = "Hardware"
        elif category == '3':
            directory = "Medical"
        elif category == '4':
            directory = "Robotics"
        elif category == '5':
            directory = "Robotics_Medical"
        break
    else:
        print("Enter valid classification number.")
        category = input("Biotech:1, Hardware:2, Medical:3, Robotics:4, Robotics/Medical:5 -- Input value: ")

company_name = input("Company name?: ")

path = os.path.join(parent_dir, directory, company_name)
os.mkdir(path)
print(path)

    #need to make it open this new direcotyr and save resume inside it

while True:
        
    #click on shell input area
    pyautogui.click(976,1351)

    wti = input("Keyword to insert into resume?: ")

    wtr = input("Word in resume to replace?: ")

    #need to click on word doc area
    pyautogui.click(2488,468)
      
    pyautogui.hotkey('ctrl','h')

    time.sleep(0.2)

    pyautogui.typewrite(wtr)

    pyautogui.press('tab')

    pyautogui.typewrite(wti)

    #click replace twice to replace that string
    pyautogui.click(1654,813)

    time.sleep(0.5)
    
    pyautogui.click(1654,813)

    time.sleep(0.1)

    #click OK
    pyautogui.click(1287,778)
