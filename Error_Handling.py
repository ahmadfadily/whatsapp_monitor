from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, \
    ElementNotInteractableException
import time

def click_function(user):
	while True:
		try:
			user.click()
			break
		except (NoSuchElementException, StaleElementReferenceException, ElementNotInteractableException) as e:
			print("stuck in exception : " + str(e))
			time.sleep(1)
