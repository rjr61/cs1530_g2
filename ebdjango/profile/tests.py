from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
class AccountTestCase(LiveServerTestCase):

    def setUp(self):
        options = Options()
        options.add_argument('--headless')
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-gpu");
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-dev-shm-usage")   
        options.add_argument("--disable-setuid-sandbox")     
        self.selenium = webdriver.Chrome('/usr/bin/chromedriver',chrome_options=options)
        super(AccountTestCase, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(AccountTestCase, self).tearDown()

    def test_register(self):
        selenium = self.selenium
        
        #Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/login/?next=/')
        WebDriverWait(selenium,100000).until(EC.visibility_of_element_located((By.TAG_NAME,'body')))
        #selenium.get('https://www.google.com')
        #find the form element
        selenium.implicitly_wait(20)
        username = selenium.find_element_by_name('username')
        password = selenium.find_element_by_name('password')
        #password = selenium.find_element_by_css_selector("input[name='password'][type='password']")
        #password2 = selenium.find_element_by_id('id_password2')
        submit = selenium.find_element_by_id('login-button')

        
        #Fill the form with data
        #username.clear()
        username.send_keys('ryan')
        #password.clear()
        password.send_keys('fantaorange')
        #password2.send_keys('fantaorange')

        print(str(selenium.current_url))

        #submitting the form
        submit.submit()
        #check the returned result
        assert 'http://127.0.0.1:8000/' == selenium.current_url