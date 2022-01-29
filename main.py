import datetime

import serial
import time
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser = serial.Serial('COM4',9600, timeout=100)
line = ser.readline()


chrome_driver_path = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://weather.com/es-AR/tiempo/hoy/l/-34.59,-60.95?par=google")
driver.implicitly_wait(0.5)

es = driver.find_elements(By.CLASS_NAME, "WeatherDetailsListItem--wxData--2s6HT")
print(es[2].text)



while 1:
    line = ser.readline()
    line = line.decode('utf-8')
    driver.refresh()
    driver.implicitly_wait(1)
    time.sleep(5)
    es = driver.find_elements(By.CLASS_NAME, "WeatherDetailsListItem--wxData--2s6HT")
    if line[0:2] == 'H:':
        f = open('data.txt','a')
        h = es[2].text
        data = datetime.datetime.now().strftime('%d/%m/%Y-%H:%M') + ' H: ' + line[3:5] + ' ' + 'T: ' + line[12:14] + ' Online: ' + h +'\n'
        f.write(data)
        print(data)
        f.close()

    time.sleep(270) #270