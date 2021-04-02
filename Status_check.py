import time
from datetime import datetime
from playsound import playsound
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from Error_Handling import click_function
from Updaters import status_txt_update, status_whatsapp_updates


def status_check(driver):
    flag = 0
    online_time = 0
    typing_check = 1

    driver.get('http://web.whatsapp.com')

    name = input('Enter the name of user : ')

    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    click_function(user)
    while True:
        i = 0
        try:
            status = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/header/div[2]/div[2]/span").text
            i = 1
        except (NoSuchElementException, StaleElementReferenceException):
            status = 'offline'
            if flag == 1:
                status_txt_update(status, online_time)
                typing_check = 0
            flag = 0
            i = 0

        if i == 1:
            if flag != 1 and status == 'online':
                online_time = datetime.now()
                status_txt_update(status, online_time)
                playsound('online_notify.mp3')
                typing_check = 0
                flag = 1
            if status == 'typing…':
                if typing_check == 0:
                    typing_check = 1
                    status_whatsapp_updates("typing…", driver, name)
                    status_txt_update(status, online_time)
                    playsound('meow.mp3')
            print('onlineee')
        print(status)
        time.sleep(1)

