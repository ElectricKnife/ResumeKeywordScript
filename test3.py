from selenium import webdriver
import time
import pyautogui
import re
import keyboard

driver = webdriver.Chrome(executable_path=r'C:\webdrivers\chromedriver.exe')
driver.get('http://coursehero.com/')

input("Input to start: ")

for i in range(100):
    print(".")

# do everthing you need to until you're logged in and ready

while True:
    
    if keyboard.is_pressed("p"):
        input("Program paused. Enter to continue ")
        
    src = driver.page_source
    text_found = re.search(r'created from', src)

    time.sleep(0.75)

    try:
        no_new_ques = driver.find_element_by_xpath("//div[contains(@class,'h5 mt-3')]").text # prevents script from trying to skip next opportunity after questions end in a category
    except:
        no_new_ques = "hello"
    
    try:
        bonus_ques = driver.find_element_by_xpath("//span[contains(@class,'font-weight-500')]").text
    except:
        bonus_ques = "hi"
        
    if bonus_ques == "BONUS QUESTION":
        while True:
            try:
                bonus_price = driver.find_element_by_xpath("//span[contains(@class,'total-price-difficulty-bonus')]").text
                bonus_price = bonus_price[1:] # cuts out $ sign at front
                print("Bonus price is $" + str(bonus_price))
                break
            except:
                continue
    else:
        try:
            bonus_price = driver.find_element_by_xpath("//span[contains(@class,'total-price-no-bonus')]").text
            bonus_price = bonus_price[1:]
        except:
            bonus_price = 2.00
        print("No bonus")

    if bonus_price == 2.00:
        time.sleep(2) # extra delay to try again in case 2.00 was a result of it not being loaded in yet (not sure if this works...)
        try:
            bonus_price = driver.find_element_by_xpath("//span[contains(@class,'total-price-difficulty-bonus')]").text
            bonus_price = bonus_price[1:]
        except:
            bonus_price = 2.00

    if (float(bonus_price) >= 6.00 and text_found == None) or (float(bonus_price) >= 9.00 and text_found != None): # change lower price limits as needed.
            # move for scroll clicking
            pyautogui.moveTo(4466,1857)
            pyautogui.moveTo(4466,1857) # intentional second one to get it on second monitor
            for i in range(5):
                pyautogui.click()
                time.sleep(0.02)

            # reset mouse to console
            pyautogui.moveTo(650,1352)
            pyautogui.click()

            while True:
                answer_ques = input("Answer? ")
                if(answer_ques != 'n' and answer_ques != 'y'):
                    print("Enter y or n. ")
                else:
                    break
            
            if answer_ques == 'n':
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
                while True:
                    try:
                        element = driver.find_element_by_xpath("//button[text()='Submit']")
                        break
                    except:
                        continue
                driver.execute_script("arguments[0].click();", element)
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
            #else:
                #print("Enter y or n: ")
    elif no_new_ques != "There are no new questions in your queue.":
            print("Going to skip this since bonus_price is " + str(bonus_price) + " and text_found is " + str(text_found))
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
            while True:
                try:
                    element = driver.find_element_by_xpath("//button[text()='Submit']")
                    break
                except:
                    continue

            if keyboard.is_pressed("p"):
                input("Program paused. Enter to continue and submit ")
            
            driver.execute_script("arguments[0].click();", element)
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
        input("End of line. Enter to continue. ")
    print("-----")

