from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'http://updendnow.s3-website-us-east-1.amazonaws.com/signin'


    email_field = (By.ID, 'email')
    password_field = (By.ID, 'password')
    sign_in_button = (By.XPATH, '//*[@id="root"]/div/div/div[2]/form/button/span/span')


    def load(self):
        self.driver.get(self.url)

    def enter_email(self, email):
        self.driver.find_element(*self.email_field).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_sign_in(self):
        self.driver.find_element(*self.sign_in_button).click()
