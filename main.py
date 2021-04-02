from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Config import Chrome_path
from ChoosingActivity import choose_activity

if __name__ == "__main__":
	#Starts chrome :
	options = webdriver.ChromeOptions()
	options.add_argument(Chrome_path)
	driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
	choose_activity(driver)

