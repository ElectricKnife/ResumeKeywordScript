from selenium import webdriver
import time
import pyautogui
import re

driver = webdriver.Chrome(executable_path=r'C:\webdrivers\chromedriver.exe')
driver.get('http://coursehero.com/')

input("Input to start: ")

# do everthing you need to until you're logged in and ready

while True:
    src = driver.page_source
    text_found = re.search(r'created from', src)
    if text_found:
            while True:
                try:
                    element = driver.find_element_by_xpath("//button[text()='Skip']")
                    break
                except:
                    continue
            driver.execute_script("arguments[0].click();", element)
            time.sleep(0.5)
            # move mouse to position and click checkbox
            pyautogui.moveTo(3120,1370)
            pyautogui.click()
            #time.sleep(0.1)
            while True:
                try:
                    element = driver.find_element_by_xpath("//button[text()='Submit']")
                    break
                except:
                    continue
            driver.execute_script("arguments[0].click();", element)
            #time.sleep(0.5)
            while True:
                try:
                    element = driver.find_element_by_xpath("//button[text()='Next question']")
                    break
                except:
                    continue
            driver.execute_script("arguments[0].click();", element)
            time.sleep(2)
            # reset mouse to console
            pyautogui.moveTo(650,1352)
            pyautogui.click()
    else:
        # move for scroll clicking

        pyautogui.moveTo(4466,1857)
        pyautogui.moveTo(4466,1857) # intentional second one to get it on second monitor
        for i in range(5):
            pyautogui.click()
            time.sleep(0.02)

        # reset mouse to console
        pyautogui.moveTo(650,1352)
        pyautogui.click()

        answer_ques = input("Answer? ")
        if answer_ques == 'n':
            element = driver.find_element_by_xpath("//button[text()='Skip']")
            driver.execute_script("arguments[0].click();", element)
            time.sleep(0.5)
            # move mouse to position and click checkbox
            pyautogui.moveTo(3120,1370)
            pyautogui.click()
            #time.sleep(0.1)
            while True:
                try:
                    element = driver.find_element_by_xpath("//button[text()='Submit']")
                    break
                except:
                    continue
            driver.execute_script("arguments[0].click();", element)
            #time.sleep(0.5)
            while True:
                try:
                    element = driver.find_element_by_xpath("//button[text()='Next question']")
                    break
                except:
                    continue
            driver.execute_script("arguments[0].click();", element)
            time.sleep(2)

        elif answer_ques == 'y':
            input("Enter to continue: ")
        else:
            print("Enter y or n: ")
