from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Config import Chrome_path
from ChoosingActivity import choose_activity
from requests.exceptions import ConnectionError
import time

if __name__ == "__main__":
	#Starts chrome :
	options = webdriver.ChromeOptions()
	options.add_argument(Chrome_path)
	while(True):
		try:
			driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
			break
		except (ConnectionError) as e:
			print(e)
			time.sleep(1)

	choose_activity(driver)

