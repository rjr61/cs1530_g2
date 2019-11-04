from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class AccountTestCase(LiveServerTestCase):

    def setUp(self):
        self.selenium = webdriver.Firefox()
        super(AccountTestCase, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(AccountTestCase, self).tearDown()

    def test_register(self):
        selenium = self.selenium
        #Opening the link we want to test
        selenium.get('http://ebdjango-dev2222.us-east-1.elasticbeanstalk.com/login/?next=/')
        #find the form element
        username = selenium.find_element_by_id('id_username')
        password = selenium.find_element_by_id('id_password')

        submit = selenium.find_element_by_name('login-button')

        #Fill the form with data
        username.send_keys('ryan')
        password.send_keys('fantaorange')

        #submitting the form
        submit.send_keys(Keys.RETURN)

        #check the returned result
        assert 'http://ebdjango-dev2222.us-east-1.elasticbeanstalk.com/' in selenium.current_url