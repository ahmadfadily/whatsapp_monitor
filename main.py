from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from webdriver_manager.chrome import ChromeDriverManager
import time
from datetime import datetime
import smtplib
from playsound import playsound

flag = 0
online_time=0
typing_check =1

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('http://web.whatsapp.com')

name = input('Enter the name of user or group : ')
user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

def email_updater():
	sender_email = input('Enter the sender email for the typing update: ')
	rec_email = input('Enter the rec email for the typing update: ')
	password_email = input('Enter the password: ')
	message_email = " Typing !"
	server = smtplib.SMTP('smtp.gmail.com',587)
	server.starttls()
	server.login(sender_email,password_email)
	server.sendmail(sender_email, rec_email, message_email)



def status_whatsapp_updates(message):
	user = driver.find_element_by_xpath('//span[@title = "{}"]'.format("Status_updates"))
	user.click()
	driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(message)
	driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button/span').click()
	time.sleep(1)
	user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
	user.click()

def status_txt_update(message):
	f=open('status.txt','a')
	if message == 'offline' :
		f.write('have been online for '+ str(datetime.now()-online_time)+ ' minutes ')
	f.write(str(datetime.now()))
	f.write(' '+ message + '\n')
	f.close()
	time.sleep(1)

while True:
	i=0
	try:
		#status = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[4]/div[1]/header/div[2]/div[2]/span").text
		#status = driver.find_element_by_class_name('YmixP fKfSX').text
		status = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/header/div[2]/div[2]/span").text
		i=1
	except (NoSuchElementException, StaleElementReferenceException):
		status = 'offline'
		if flag == 1:
			status_txt_update(status)
			typing_check =0
		flag=0
		i=0

	if i==1:
		if flag != 1 and status == 'online':
			online_time = datetime.now()
			status_txt_update(status)
			typing_check = 0
			flag = 1
		if status == 'typing…':
			if typing_check == 0:
				typing_check = 1
				status_whatsapp_updates("typing…")
				status_txt_update(status)
				playsound('meow.mp3')
		print('onlineee')
	print(status)
	time.sleep(3)


#msg_box = driver.find_element_by_class_name('input-container')

#for i in range(count):
#    msg_box.send_keys(msg)
#    driver.find_element_by_class_name('compose-btn-send').click()
