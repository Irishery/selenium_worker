import os
import random
from time import sleep
import httpx
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver.v2 as uc
from time import sleep
from dotenv import load_dotenv

load_dotenv()

gmail_login = os.getenv('MAIL_LOGIN')
gmail_pass = os.getenv('MAIL_PASS')

coinlist_email = os.getenv('COINLIST_EMAIL')
coinlist_pass = os.getenv('COINLIST_PASS')

options = uc.ChromeOptions()
# options.add_argument('--load-extension=/Users/User1/Desktop/live_stream,/Users/User1/Desktop/ublock')
# options.binary_location = '/home/kir/chromes/google-chrome-beta_current_x86_64/opt/google/chrome-beta/google-chrome-beta'
# options.add_argument('disable-popup-blocking')
# driver = webdriver.Chrome('./chromedriver', options=options)
# driver = uc.Chrome(options=options)

class Worker:
    def __init__(self) -> None:
        options = uc.ChromeOptions()
        options.binary_location = '/home/kir/chromes/google-chrome-beta_current_x86_64/opt/google/chrome-beta/google-chrome-beta'
        # options.headless = True
        self.driver = uc.Chrome(options=options)
        self.driver.set_window_size(1920, 1080)
        self.client = httpx.Client(timeout=None)

    def main_runner(self):
        self.log_in()
        # self.approve_new_device()
        sleep(20)
    
    def log_in(self):
        self.driver.get("https://coinlist.co/")


        log_in_btn = self.driver.find_element(By.CSS_SELECTOR, 'div.u-displayInlineBlock:nth-child(1) > a:nth-child(1)')
        log_in_btn.click()

        while True:
            try:
                email = self.driver.find_element(By.CSS_SELECTOR, '#user_email')
                password = self.driver.find_element(By.CSS_SELECTOR, '#user_password')
                email.click()
                break
            except Exception as e:
                print(e)


        print(coinlist_email)
        self.human_type(email, coinlist_email)

        password.click()
        self.human_type(password, coinlist_pass)

        log_in = self.driver.find_element(By.CSS_SELECTOR, '#new_user > div > div:nth-child(5) > input')
        log_in.click()
        sleep

        if self.check_recaptcha():
            print('CAPTCHA')
            while self.check_recaptcha():
                sleep(10)
        print('end captcha')
        sleep(20)
        self.approve_new_device()
    
    def human_type(self, element, text) -> None:
        for char in text:
            sleep(0.3)
            element.send_keys(char)
    
    def check_recaptcha(self) -> bool: 
        delay = 3
        try:
            captcha = WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'challenge-modal')))
            print(captcha.is_displayed())
            return True
        except Exception as e:
            print(e)
            return False
    
    def ping(self, data):
        r = self.client.request(
            "get", "http://127.0.0.1:5000/api/selenium/post_data",
            params={'data_from_worker': data},
            headers={'content-type': 'application/json'}
        )
    
    def approve_new_device(self):
        while True:
            try:
                self.driver.execute_script("window.open();")# Switch to the new window and open URL B
                self.driver.switch_to.window(self.driver.window_handles[1])
                break
            except IndexError:
                continue

        self.driver.get('https://e.mail.ru/')

        # log_in = self.driver.find_element(By.XPATH, '/html/body/div[1]/nav/div[3]/div/div[2]/ul/li[8]/a')
        # log_in.click()

        delay = 10 # seconds
        while True:
            try:
                email = WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div/div/div/div/form/div[2]/div[2]/div[1]/div/div/div/div/div/div[1]/div/input')))
                break
            except TimeoutException:
                print("Page is loading")

        email.click()
        while True:
            try:
                self.human_type(email, gmail_login)
                break
            except Exception as e:
                print(e)

        go_to_pass = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div/div/div/div/form/div[2]/div[2]/div[3]/div/div/div[1]/button')
        go_to_pass.click()
        while True:
            try:
                password = WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div/div/div/div/form/div[2]/div/div[2]/div/div/div/div/div/input')))
                break
            except TimeoutException:
                print("Page is loading")

        while True:
            try:
                self.human_type(password, gmail_pass)
                break
            except Exception as e:
                print(e)
        sleep(3)

        enter = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div/div/div/div/form/div[2]/div/div[3]/div/div/div[1]/div/button')
        enter.click()

        while True:
            try:
                search = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div[1]/div[1]/div/div[1]/span/div[4]/div/div[1]/div')
                break
            except Exception as e:
                print("Page is loading")
        
        search.click()
        sleep(3)

        while True:
            try:
                search_input = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div[1]/div[1]/div/div[1]/span/div[4]/div/div[3]/div/div/span/span/div/input')
                break
            except Exception as e:
                search.click()
                print('Page is loading')
        
        sleep(3)

        while True:
            try:
                self.human_type(search_input, 'coinlist')
                break
            except Exception as e:
                print('Page is loading')
        sleep(3)

        while True:
            try:
                search_btn = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div[1]/div[1]/div/div[1]/span/div[4]/div/div[3]/div/span[2]')
                break
            except Exception as e:
                print('Page is loading')
        search_btn.click()

        while True:
            try:
                approve_letter = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div[1]/div[1]/div/div[2]/span/div[2]/div/div/div/div/div[1]/div/div/div/div[1]/div/div/a[1]/div[4]/div/div[1]')
                break
            except Exception as e:
                print("Page is loading")

        approve_letter.click()

        while True:
            try:
                approve_link = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div[1]/div[1]/div/div[2]/span/div[2]/div/div/div/div/div/div/div[2]/div[1]/div[3]/div[2]/div/div/div/div/div/div/div/div/div/div/table/tbody/tr/td/div/table[1]/tbody/tr/td/div[2]/div/div[7]/a')
                break
            except Exception as e:
                print('Page is loading')
        approve_link.click()

        sleep(15)
        
        self.ping('pong')

        # while True:
        #     try:
        #         account_btn = self.driver.find_element(By.CSS_SELECTOR, 'body > div.u-height100.layouts-shared-market > div > div.js-sidebar.layouts-shared-market__sidebar > div > div.layouts-shared-market-sidebar__open > div.u-displayInlineBlock.layouts-shared-market-sidebar__icon > a')
        #         break
        #     except Exception as e:
        #         print(e)
        
        # account_btn.click()
        

        # while True:
        #     try:
        #         personal_info = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[1]/div/div/div/div[2]/a')
        #         break
        #     except Exception as e:
        #         print(e)

        # personal_info.click()

        # input()
