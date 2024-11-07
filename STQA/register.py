

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("http://127.0.0.1:5501/login/register.html")


test_registrations = [
    {"username": "Aditya123", "email": "valid@example.com", "password": "Password123", "confirm_password": "Password123"},#Valid
    {"username": "so", "email": "short@example.com", "password": "pass1234", "confirm_password": "pass1234"},  # Invalid username
    {"username": "validuser123", "email": "invalid_email", "password": "Password123", "confirm_password": "Password123"},  # Invalid email
    {"username": "validuser123", "email": "valid2@example.com", "password": "short", "confirm_password": "short"},  # Invalid password
    {"username": "validuser123", "email": "valid3@example.com", "password": "Password123", "confirm_password": "Password12"}  # Mismatched passwords
]

for reg in test_registrations:
    driver.find_element(By.ID, "username").clear()
    driver.find_element(By.ID, "email").clear()
    driver.find_element(By.ID, "password").clear()
    driver.find_element(By.ID, "confirm-password").clear()

    driver.find_element(By.ID, "username").send_keys(reg["username"])
    driver.find_element(By.ID, "email").send_keys(reg["email"])
    driver.find_element(By.ID, "password").send_keys(reg["password"])
    driver.find_element(By.ID, "confirm-password").send_keys(reg["confirm_password"])

    driver.find_element(By.ID, "register-btn").click()


    time.sleep(2) 

    try:

        success_message = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.ID, "success-message"))
        )
        print(f"Registration successful for: {reg['username']}")
    except Exception as e:
   
        error_messages = driver.find_elements(By.CLASS_NAME, "error")
        if error_messages:
            print(f"Registration failed for: {reg['username']}. Errors: {[error.text for error in error_messages]}")
        else:
            print(f"Registration failed for: {reg['username']}.  error messages .")

driver.quit()
