from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class ProjectDetailsPage:
    def __init__(self, driver):
        self.driver = driver


    film_next_button = (By.XPATH, '//*[@id="root"]/div/div[3]/div/div/div[2]/div[2]/div[2]/button[2]')
    drama_button = (By.XPATH, '//*[@id="root"]/div/div[3]/div/div/div[2]/div[2]/div[1]/div/div[1]/div/div/div/button[1]')
    horror_button = (By.XPATH, '//*[@id="root"]/div/div[3]/div/div/div[2]/div[2]/div[1]/div/div[1]/div/div/div/button[2]')
    action_button = (By.XPATH, '//*[@id="root"]/div/div[3]/div/div/div[2]/div[2]/div[1]/div/div[1]/div/div/div/button[3]')
    qualities_next_button = (By.XPATH, '//*[@id="root"]/div/div[3]/div/div/div[2]/div[2]/div[2]/button[2]')
    film_length_button = (By.XPATH,'//*[@id="root"]/div/div[3]/div/div/div[2]/div[2]/div[1]/div/div[1]/div/div/div[1]/button[1]')
    film_hosting_site_web =(By.XPATH,'//*[@id="root"]/div/div[3]/div/div/div[2]/div[2]/div[1]/div/div[1]/div/div/div[2]/button[1]')
    film_hosting_site_youTube=(By.XPATH,'//*[@id="root"]/div/div[3]/div/div/div[2]/div[2]/div[1]/div/div[1]/div/div/div[2]/button[2]')
    film_hosting_site_instagram=(By.XPATH,'//*[@id="root"]/div/div[3]/div/div/div[2]/div[2]/div[1]/div/div[1]/div/div/div[2]/button[4]')
    next_button_hosting_site =(By.XPATH,'//*[@id="root"]/div/div[3]/div/div/div[2]/div[2]/div[2]/button[2]')
    name_input_field =(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div[2]/div[1]/div/div[1]/div/div/div[1]/div[1]/div/input')
    website_input_field =(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div[2]/div[1]/div/div[1]/div/div/div[1]/div[2]/div/input')
    target_audience_input_field =(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div[2]/div[1]/div/div[1]/div/div/div[2]/div/textarea')
    next_button_input_field =(By.XPATH,'//*[@id="root"]/div/div[3]/div/div/div[2]/div[2]/div[2]/button[2]')
    log_line_input =(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div[2]/div[1]/div/div/div/div/div/div/textarea')
    log_line_next_button= (By.XPATH,'//*[@id="root"]/div/div[3]/div/div/div[2]/div[2]/div[2]/button[2]')
    # implement scroll
    scrollWindow =(By.TAG_NAME,'body')
    video_check_box =(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div[2]/div[1]/div/div[1]/div/div/div[4]/div[2]/div[2]/div/div[1]/input')
    video_check_box_next_button = (By.XPATH,'//*[@id="root"]/div/div[3]/div/div/div[2]/div[2]/div[2]/button[2]')

    def click_film_next(self):
        self.driver.find_element(*self.film_next_button).click()

    def select_drama(self):
        self.driver.find_element(*self.drama_button).click()
    def select_horror(self):
        self.driver.find_element(*self.horror_button).click()
    def select_action(self):
        self.driver.find_element(*self.action_button).click()

    def click_qualities_next(self):
        self.driver.find_element(*self.qualities_next_button).click()
    def select_film_length(self):
        self.driver.find_element(*self.film_length_button).click()
    def select_hosting_site(self):
        self.driver.find_element(*self.film_hosting_site_web).click()
        self.driver.find_element(*self.film_hosting_site_youTube).click()
        self.driver.find_element(*self.film_hosting_site_instagram).click()

    def select_next_hosting(self):
        self.driver.find_element(*self.next_button_hosting_site).click()
    def enter_name(self, name):
        self.driver.find_element(*self.name_input_field).send_keys(name)
    def enter_website(self,website):
        self.driver.find_element(*self.website_input_field).send_keys(website)
    def enter_target_audience(self,text):
        self.driver.find_element(*self.target_audience_input_field).send_keys(text)
    def select_next_button_input(self):
        self.driver.find_element(*self.next_button_input_field).click()
    def enter_log_line(self, log):
        self.driver.find_element(*self.log_line_input).send_keys(log)
    def select_log_line_next(self):
        self.driver.find_element(*self.log_line_next_button).click()
    def select_video_check_box(self):
        self.driver.find_element(*self.video_check_box).click()
    def scroll_video_check_box(self, up):
        self.driver.find_element(*self.scrollWindow).send_keys(up)
        #self.driver.execute_script("window.scrollBy(0, 500)")
    def select_video_check_box_next_button(self):
        self.driver.find_element(*self.video_check_box_next_button).click()


