import smtplib
import time
from datetime import datetime
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException


def email_updater():
	sender_email = input('Enter the sender email for the typing update: ')
	rec_email = input('Enter the rec email for the typing update: ')
	password_email = input('Enter the password: ')
	message_email = " Typing !"
	server = smtplib.SMTP('smtp.gmail.com',587)
	server.starttls()
	server.login(sender_email,password_email)
	server.sendmail(sender_email, rec_email, message_email)



def status_whatsapp_updates(message, driver, name):
	try:
		user = driver.find_element_by_xpath('//span[@title = "{}"]'.format("Status_updates"))
		user.click()
		driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(message)
		driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button/span').click()
		time.sleep(1)
		user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
		user.click()
	except(NoSuchElementException, StaleElementReferenceException):
		return

def status_txt_update(message, online_time):
	f=open('StatusLogFiles/status.txt', 'a')
	if message == 'offline' :
		f.write('have been online for '+ str(datetime.now()-online_time)+ ' minutes ')
	f.write(str(datetime.now()))
	f.write(' '+ message + '\n')
	f.close()
	time.sleep(1)