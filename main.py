from selenium import webdriver
from time import sleep
from datetime import datetime

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


file = open("log.txt","w")

option= webdriver.ChromeOptions()

option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=option)

def set_driver():
    driver.get('http://www.saucedemo.com/')
    driver.maximize_window()
    file.write("driiver is Get \n")

def insert_login():
    user_name = driver.find_element(By.XPATH,'//input[@id="user-name"]')
    login = "standard_user"
    user_name.send_keys(login)
    file.write("Success write login\n")

    user_pass=driver.find_element(By.XPATH,'//input[@id="password"]')
    password = "secret_sauce"
    user_pass.send_keys(password)
    file.write("Success write password\n")

#    sleep(3)

    log_btn=driver.find_element(By.XPATH,'//input[@id="login-button"]')
    log_btn.click()
    file.write("Success login_button click\n")

def login_with_enter():
    user_name = driver.find_element(By.XPATH,'//input[@id="user-name"]')
    login = "standard_user"
    user_name.send_keys(login)
    file.write("Success write login\n")

    user_pass=driver.find_element(By.XPATH,'//input[@id="password"]')
    password = "secret_sauce"
    user_pass.send_keys(password)
    file.write("Success write password\n")

    user_pass.send_keys(Keys.ENTER)
    file.write("Success Enter login\n")

def test_login_redirect():
    correct_url = "https://www.saucedemo.com/inventory.html"
    get_url = driver.current_url

    assert correct_url==get_url, "test_login_redirect is Failed"
    file.write("test_login_redirect is OK\n")

def test_content_after_login_is_correct():
    correct_text= "Products"
    current_text = driver.find_element(By.XPATH,'//*[@id="header_container"]/div[2]/span')

#Добавляется только дата
#    driver.save_screenshot(f"sc_real_login\\scr_test_content_after_login_is_correct_{date.today()}.png")
#Добавляется дата и время
    driver.save_screenshot(f"sc_real_login\\scr_test_content_"
                           f"_login_cor_{datetime.now().strftime('%H_%M_%S-%Y_%m_%d')}.png")

    assert correct_text==current_text.text, "test_content_after_login_is_correct is Failed"
    file.write("test_content_after_login_is_correct is OK\n")

#Сброс логина
def logout():
    menu_button = driver.find_element(By.XPATH,'//*[@id="react-burger-menu-btn"]')
    menu_button.click()
    sleep(1)
    logout_button= driver.find_element(By.XPATH,'//*[@id="logout_sidebar_link"]')
    logout_button.click()
    file.write("Success logout \n")

def test_logout_redirect():
    correct_url = "https://www.saucedemo.com/"
    get_url = driver.current_url

    assert correct_url==get_url, "test_logout_redirect is Failed"
    file.write("test_logout_redirect is OK\n")

def test_content_after_logout_is_correct():
    correct_text= "Accepted usernames are:"
    current_text = driver.find_element(By.XPATH,'//*[@id="login_credentials"]/h4')

    assert correct_text==current_text.text, "test_content_after_logout_is_correct is Failed"
    file.write("test_content_after_logout_is_correct is OK\n")

def select_jacket_is_correct():
    jacket_button = driver.find_element(By.XPATH,'//*[@id="add-to-cart-sauce-labs-fleece-jacket"]')
    jacket_button.click()
    file.write("Success jacket_button click \n")

def select_onesie_is_correct():
    onesie_button = driver.find_element(By.XPATH,'//*[@id="add-to-cart-sauce-labs-onesie"]')
    onesie_button.click()
    file.write("Success onesie_button click \n")

def select_light_is_correct():
    light_button = driver.find_element(By.XPATH,'//*[@id="add-to-cart-sauce-labs-bike-light"]')
    light_button.click()
    file.write("Success light_button click \n")

def container_click():
    container = driver.find_element(By.XPATH,'//*[@id="shopping_cart_container"]/a')
    container.click()
    file.write("Container click is OK \n")

def test_container_redirect():
    correct_url = "https://www.saucedemo.com/cart.html"
    get_url = driver.current_url

    assert correct_url==get_url, "test_container_redirect is Failed"
    file.write("test_container_redirect is OK\n")

def test_content_after_container_is_correct():
    correct_text= "Your Cart"
    current_text = driver.find_element(By.XPATH,'//*[@id="header_container"]/div[2]/span')

    assert correct_text==current_text.text, "test_content_after_container_is_correct is Failed"
    file.write("test_content_after_container_is_correct is OK\n")

def del_light_is_correct():
    remove_button = driver.find_element(By.XPATH,'//*[@id="remove-sauce-labs-bike-light"]')
    remove_button.click()
    file.write("del_light_is_correct is OK\n")

def continue_click():
    cont_button = driver.find_element(By.XPATH,'//*[@id="continue-shopping"]')
    cont_button.click()
    file.write("continue_click is OK\n")

def checkout_click():
    checkout_button= driver.find_element(By.XPATH,'//*[@id="checkout"]')
    checkout_button.click()
    file.write("checkout_click is correct \n")

def test_checkout_redirect():
    correct_url = "https://www.saucedemo.com/checkout-step-one.html"
    get_url = driver.current_url

    assert correct_url==get_url, "test_checkout_redirect is Failed"
    file.write("test_checkout_redirect is OK\n")

def test_content_after_checkout_is_correct():
    correct_text= "Checkout: Your Information"
    current_text = driver.find_element(By.XPATH,'//*[@id="header_container"]/div[2]/span')

    assert correct_text==current_text.text, "test_content_after_checkout_is_correct is Failed"
    file.write("test_content_after_checkout_is_correct is OK\n")

def cancel_click():
    cancel_button = driver.find_element(By.XPATH,'//*[@id="cancel"]')
    cancel_button.click()
    file.write("cancel_click is correct \n")

def  insert_name():
    first_name = driver.find_element(By.XPATH,'//*[@id="first-name"]')
    my_first_name = "Stan"
    first_name.send_keys(my_first_name)
    file.write("Success write First name\n")

    last_name=driver.find_element(By.XPATH,'//*[@id="last-name"]')
    my_last_name = "Dorofeev"
    last_name.send_keys(my_last_name)
    file.write("Success write Last name\n")

    postal_code = driver.find_element(By.XPATH,'//*[@id="postal-code"]')
    my_postal_code = "Nizhniy Novgorod"
    postal_code.send_keys(my_postal_code)
    file.write("Success write Postal code\n")

def continue_order_click():
    continue_button = driver.find_element(By.XPATH,'//*[@id="continue"]')
    continue_button.click()
    file.write("continue_order_button is correct \n")

def test_continue_order_redirect():
    correct_url = "https://www.saucedemo.com/checkout-step-two.html"
    get_url = driver.current_url
    assert correct_url==get_url, "test_checkout_redirect is Failed"
    file.write("test_continue_order_redirect is OK\n")

def test_content_after_cont_order_is_correct():
    correct_text= "Checkout: Overview"
    current_text = driver.find_element(By.XPATH,'//*[@id="header_container"]/div[2]/span')
    assert correct_text==current_text.text, "test_content_after_cont_order_is_correct is Failed"
    file.write("test_content_after_cont_order_is_correct is OK\n")

def finish_click():
    finish_button = driver.find_element(By.XPATH,'//*[@id="finish"]')
    finish_button.click()
    file.write("finish_button_click is correct \n")

def  test_finish_redirect():
    correct_url = "https://www.saucedemo.com/checkout-complete.html"
    get_url = driver.current_url
    assert  correct_url==get_url, "test_finish_redirect is Failed"
    file.write("test_finish_redirect is Ok \n")

def test_content_after_finish_is_correct():
    correct_text = "Checkout: Complete!"
    current_text = driver.find_element(By.XPATH,'//*[@id="header_container"]/div[2]/span')
    assert correct_text==current_text.text, "test_content_after_finish_is_correct is Failed"
    file.write("test_content_after_finish_is_correct is Ok \n")

def back_home_button_click():
    back_home_button = driver.find_element(By.XPATH,'//*[@id="back-to-products"]')
    back_home_button.click()
    file.write("back_home_button_click is correct \n")

def set_login():
    insert_login()
    #    login_with_enter()
    test_login_redirect()
    test_content_after_login_is_correct()
    file.write("         set_login was passed")

def set_logout():
    logout()
    test_logout_redirect()
    test_content_after_logout_is_correct()
    file.write("         set_logout was passed")

def select_goods():
    select_jacket_is_correct()
    select_onesie_is_correct()
    select_light_is_correct()
    file.write("         select_goods was passed")

def set_container():
    container_click()
    test_container_redirect()
    test_content_after_container_is_correct()
    file.write("         set_container was passed")

def set_checkout():
    checkout_click()
    test_checkout_redirect()
    test_content_after_checkout_is_correct()
    file.write("         set_checkout was passed")

def set_order():
    continue_order_click()
    test_continue_order_redirect()
    test_content_after_cont_order_is_correct()
    file.write("         set_order was passed")

def set_finish():
    finish_click()
    test_finish_redirect()
    test_content_after_finish_is_correct()
    file.write("         set_finish was passed")

def set_back_home():
    back_home_button_click()
    test_login_redirect()
    test_content_after_login_is_correct()
    file.write("         set_back_home was passed")

#Main block
try:
    set_driver()
 #ввод логина и пароля
    set_login()
 #сброс логина и пароля
    set_logout()
 # повторный ввод логина и пароля
    insert_login()
#выбор трех товаров
    select_goods()
#нажать кнопку корзина
    set_container()
#удаление  товара фонарь
    del_light_is_correct()
#Возврат на страницу выбора товаров
    continue_click()
    test_login_redirect()
    test_content_after_login_is_correct()
#Выбор фонарика
    select_light_is_correct()
#нажать кнопку корзина
    container_click()
#оформление заказа
    set_checkout()
 #на странице оформления нажать кнопку Cancel
 #   cancel_click() пока не нужно

# заполнение полей
    insert_name()
#нажатие кнопки Continue
    set_order()

#Нажатие кнопки  Finish
    set_finish()
 #Нажатие кнопки back_home
    set_back_home()

finally:
    file.close()