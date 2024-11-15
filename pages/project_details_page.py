import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from os import times


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
    video_check_box =(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div[2]/div[1]/div/div[1]/div/div/div[4]/div/div[2]/div/div[1]/input')
    video_check_box_next_button = (By.XPATH,'//*[@id="root"]/div/div[3]/div/div/div[2]/div[2]/div[2]/button[2]')
    budget_input =(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div[2]/div[1]/div/div[1]/div/div/div[1]/div/textarea')
    scrollCalendarWindow =(By.TAG_NAME,'body')
    calendar_next =(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div[2]/div[2]/button[2]')
    scroll_button_creative_page =(By.TAG_NAME,'body')
    download_button =(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div[2]/div[1]/div/div[1]/div/div/button')
    next_button_creative_page =(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div[2]/div[2]/button[2]')
    scroll_script_window =(By.TAG_NAME,'body')
    next_button_script =(By.XPATH,'//*[@id="root"]/div/div[3]/div/div/div[2]/div[2]/div[2]/button[2]')
    dropdown_input_field = (By.XPATH, "//input[@class='m_8fb7ebe7 mantine-Input-input mantine-Select-input' and @aria-haspopup='listbox']")
    cinematic_option = (By.XPATH, "//div[@role='option' and normalize-space()='Cinematic']")
    next_story_board =(By.XPATH,"//button[@type='button' and contains(@class, 'bg-green') and contains(@class, 'text-white')]")
    back_button_story_board =(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div[2]/div[2]/button')


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
    """
    def enter_name(self, name):
        self.driver.find_element(*self.name_input_field).clear()
        self.driver.find_element(*self.name_input_field).send_keys(name)"""
    def enter_name(self, name):
        name_field = self.driver.find_element(*self.name_input_field)
        name_field.send_keys(Keys.CONTROL + "a")
        name_field.send_keys(Keys.DELETE)
        name_field.send_keys(name)

    def enter_website(self,website):
        website_field = self.driver.find_element(*self.website_input_field)
        website_field.send_keys(Keys.CONTROL + "a")
        website_field.send_keys(Keys.DELETE)
        website_field.send_keys(website)

    def enter_target_audience(self,text):
        target_audience_field =self.driver.find_element(*self.target_audience_input_field)
        target_audience_field.send_keys(Keys.CONTROL + "a")
        target_audience_field.send_keys(Keys.DELETE)
        target_audience_field.send_keys(text)

    def select_next_button_input(self):
        self.driver.find_element(*self.next_button_input_field).click()

    def enter_log_line(self, log):
        log_line_field =self.driver.find_element(*self.log_line_input)
        log_line_field.send_keys(Keys.CONTROL + "a")
        log_line_field.send_keys(Keys.DELETE)
        log_line_field.send_keys(log)

    def select_log_line_next(self):
        self.driver.find_element(*self.log_line_next_button).click()

    def select_video_check_box(self):
        self.driver.find_element(*self.video_check_box).click()

    def scroll_video_check_box(self, down):
        self.driver.find_element(*self.scrollWindow).send_keys(down)
        #self.driver.execute_script("window.scrollBy(0, 500)")

    def select_video_check_box_next_button(self):
        self.driver.find_element(*self.video_check_box_next_button).click()

    def enter_budget(self, amount):
        budget_field = self.driver.find_element(*self.budget_input)
        budget_field.send_keys(Keys.CONTROL + "a")
        budget_field.send_keys(Keys.DELETE)
        budget_field.send_keys(amount)

    def scroll_calendar_page(self, low):
        self.driver.find_element(*self.scrollCalendarWindow).send_keys(low)



    calendar_next_button = (By.XPATH, "//button[@data-direction='next']")
    calendar_month_label = (By.XPATH, "//button[contains(@class, 'mantine-DatePicker-calendarHeaderLevel')]")

    def select_date(self, month_year, day):

        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(self.calendar_month_label))
        while True:
            current_month = self.driver.find_element(*self.calendar_month_label).text
            if current_month == month_year:
                break
            else:
                self.driver.find_element(*self.calendar_next_button).click()
                WebDriverWait(self.driver, 15).until(EC.text_to_be_present_in_element(self.calendar_month_label, current_month))

        day_button_xpath = f"//button[@aria-label='{day} {month_year}']"
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, day_button_xpath)))
        self.driver.find_element(By.XPATH, day_button_xpath).click()

    def select_calender_next(self):
        self.driver.find_element(*self.calendar_next_button).click()

    def scroll_creative_page(self, down):
        self.driver.find_element(*self.scroll_button_creative_page).send_keys(down)


    def select_download_pdf(self):
        self.driver.find_element(*self.download_button).click()

    def select_next_button_creative_page(self):
        self.driver.find_element(*self.next_button_creative_page).click()

    def scroll_script_page(self,down):

        self.driver.find_element(*self.scroll_script_window).send_keys(down)
        self.driver.find_element(*self.scroll_script_window).send_keys(down)
        print("Fim Script Page")
        time.sleep(40)

    def select_next_button_script(self):
        self.driver.find_element(*self.next_button_script).click()

    def select_cinematic_dropdown(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(*self.dropdown_input_field)).click()

    def select_cinematic_option(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(*self.cinematic_option)).click()

  #  def select_next_story_button(self):
  #      self.driver.find_element(*self.next_story_board).click()

    def select_next_story_button(self):
        print("enter method")
        try:

            next_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.next_story_board)
            )
            next_button.click()
        except Exception as e:
            print(f"Standard click failed: {e}")

            try:
                next_button = self.driver.find_element(*self.next_story_board)
                self.driver.execute_script("arguments[0].click();", next_button)
                print("Clicked using JavaScript.")
            except Exception as js_error:
                print(f"JavaScript click also failed: {js_error}")


    def select_back_button(self):
        self.driver.find_element(*self.back_button_story_board).click()


