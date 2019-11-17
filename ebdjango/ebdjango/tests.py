from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
class AccountTestCase(LiveServerTestCase):

    def setUp(self):
        options = Options()
        options.headless = True
        #options.add_argument('--headless')
        """options.add_argument("--no-sandbox")
        options.add_argument("disable-infobars")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-dev-shm-usage")"""     
        self.selenium = webdriver.Firefox(options=options, executable_path=r'usr/bin/geckodriver.exe')
        super(AccountTestCase, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(AccountTestCase, self).tearDown()

    def test_register(self):
        selenium = self.selenium
        #Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/login/?next=/')
        #find the form element
        username = selenium.find_element_by_name('username')
        password = selenium.find_element_by_name('password')

        submit = selenium.find_element_by_id('login-button')

        #Fill the form with data
        username.send_keys('ryan')
        password.send_keys('fantaorange')

        #submitting the form
        submit.send_keys(Keys.RETURN)

        #check the returned result
       # assert 'http://127.0.0.1:8000/' in selenium.current_url