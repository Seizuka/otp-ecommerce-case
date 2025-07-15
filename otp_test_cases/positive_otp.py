from selenium import webdriver
from otp_object.otp_page import OTPPage
from selenium.webdriver.chrome.service import Service
from utils.gmail_utils import get_otp_from_gmail_imap
import time
import json
import config
import undetected_chromedriver as uc



def run():
    with open('data/transaction_data.json', 'r') as f:
        data = json.load(f)

    service = Service(executable_path="chromedriver.exe")
    driver = uc.Chrome(service=service)
    driver.maximize_window()

    driver.get("https://www.blibli.com/")

    otp_page = OTPPage(driver)
    otp_page.click_btn_login()

    otp_page.fill_login(config.EMAIL)
    otp_page.click_close_pop_up()
    time.sleep(3)

    otp_code = get_otp_from_gmail_imap(config.EMAIL, config.APP_PASSWORD)
    print("OTP Retrieved:", otp_code)

    if otp_code:
        otp_page.fill_otp(otp_code)
    else:
        print("OTP not found.")
    
    time.sleep(10)
    driver.quit()