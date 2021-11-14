from selenium import webdriver
import time
import pyautogui
import re
import keyboard

driver = webdriver.Chrome(executable_path=r'C:\webdrivers\chromedriver.exe')
driver.get('https://myjobs.indeed.com/applied?hl=en&co=US&from=_atweb_gnav-homepage')

input("Input to start: ")

for i in range(100):
    print(".")

# do everthing you need to until you're logged in and ready

#while True:
