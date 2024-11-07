from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()  

driver.get("http://127.0.0.1:5501/login/index.html")


test_credentials = [
    {"username": "standard_user", "password": "secret_sauce"},
    {"username": "locked_out_user", "password": "sauce_secret"},
    {"username": "performance_glitch_user", "password": "secret_sauce"},
    {"username": "invalid_user", "password": "wrong_pass"} ,
    {"username": "demo_user", "password": "demo_pass"},
    {"username": "invalid_user", "password": "wrong_pass"} 
]


for creds in test_credentials:

    driver.find_element(By.ID, "username").clear()
    driver.find_element(By.ID, "password").clear()


    driver.find_element(By.ID, "username").send_keys(creds["username"])
    driver.find_element(By.ID, "password").send_keys(creds["password"])


    driver.find_element(By.ID, "login-btn").click()


    time.sleep(3)

    if driver.current_url.endswith("dashboard.html"):
        print(f"Login successful for: {creds['username']}")
        driver.get("http://127.0.0.1:5501/login/index.html")  
    else:
       
        error_message = driver.find_element(By.ID, "error-message").text
        if error_message == "Invalid Username or Password!":
            print(f"Login failed as expected for: {creds['username']}")
        else:
            print(f"Unexpected result for: {creds['username']}")



driver.quit()
