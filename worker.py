import os
import random
from time import sleep
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver.v2 as uc
from time import sleep
from dotenv import load_dotenv

load_dotenv()

gmail_login = os.getenv('GMAIL_LOGIN')
gmail_pass = os.getenv('GMAIL_PASS')

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
        self.driver = uc.Chrome(options=options)
    
    def main_runner(self):
        self.log_in()
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


        if self.check_recaptcha():
            print('CAPTCHA')
            sleep(20)

        self.approve_new_device()
    
    def human_type(self, element, text) -> None:
        for char in text:
            sleep(random.randint(1,2))
            element.send_keys(char)
    
    def check_recaptcha(self) -> bool: 
        delay = 10
        try:
            captcha = WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((By.ID, 'freshworks-frame')))
            return True
        except Exception as e:
            print(e)
            return False
    
    def approve_new_device(self):
        while True:
            try:
                self.driver.execute_script("window.open();")# Switch to the new window and open URL B
                self.driver.switch_to.window(self.driver.window_handles[1])
                break
            except IndexError:
                continue

        self.driver.get('https://www.google.com/intl/ru/gmail/about/')

        log_in = self.driver.find_element(By.CSS_SELECTOR, 'body > header > div > div > div > a.button.button--medium.button--mobile-before-hero-only')
        log_in.click()

        delay = 3 # seconds
        try:
            email = WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((By.ID, 'identifierId')))
            print("Page is ready!")
        except TimeoutException:
            print("Loading took too much time!")

        email.click()

        self.human_type(email, gmail_login)

        go_to_pass = self.driver.find_element(By.CSS_SELECTOR, '#identifierNext > div > button')
        go_to_pass.click()

        try:
            password = WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input')))
            print("Page is ready!")
        except TimeoutException:
            print("Loading took too much time!")

        self.human_type(password, gmail_pass)

        go_to_pass = self.driver.find_element(By.CSS_SELECTOR, '#passwordNext > div > button')
        go_to_pass.click()

        while True:
            try:
                gmail_search = self.driver.find_element(By.CSS_SELECTOR, '#gs_lc50 > input:nth-child(1)')
                print("Page is ready!")
                break
            except Exception as e:
                print("Loading took too much time!")


        self.human_type(gmail_search, 'coinlist')
        search_btn = self.driver.find_element(By.CSS_SELECTOR, '.gb_nf')
        search_btn.click()

        while True:
            try:
                approve_letter = self.driver.find_element(By.CSS_SELECTOR, '#\:nb')
                print("Page is ready!")
                break
            except Exception as e:
                print("Loading took too much time!")

        approve_letter.click()
        
        while True:
            try:
                close_all = self.driver.find_element(By.XPATH, '/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[3]/div/table/tr/td[1]/div[2]/div[1]/div[1]/div/span[1]/div')
                close_all.click()
                break
            except Exception as e:
                print('close all')
                print(e)

        try:
            more_info = self.driver.find_element(By.XPATH, '/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[3]/div/table/tr/td[1]/div[2]/div[2]/div/div[3]/div[last()]/div/div/div/div/div[1]/div[2]/div[3]/div[2]')
            print("Page is ready!")
        except Exception as e:
            print('load more info')
            print("Loading took too much time!")
            raise e
            
        while True:
            try:
                print(more_info.get_attribute('innerHTML'))
                more_info.click()
                break
            except Exception as e:
                print('more info')
                print(e)
        # input()

        approve_link = self.driver.find_element(By.XPATH, '/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[3]/div/table/tr/td[1]/div[2]/div[2]/div/div[3]/div[last()]/div/div/div/div/div[1]/div[2]/div[3]/div[3]/div/div/div[2]/div/table/tbody/tr/td/div/table[1]/tbody/tr/td/div[2]/div/div[7]/a')
        approve_link.click()
        # input()