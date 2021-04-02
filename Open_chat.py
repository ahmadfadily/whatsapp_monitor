from Error_Handling import click_function


def open_chat(driver):
    number = input('please enter the number with the country calling code : ')
    driver.get('http://wa.me/' + number)
    user = driver.find_element_by_class_name("_whatsapp_www__block_action")
    click_function(user)
    user= driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[2]/div/div/a")
    click_function(user)
