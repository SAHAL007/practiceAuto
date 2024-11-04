from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProjectsPage:
    def __init__(self, driver):
        self.driver = driver


    project_list_container = (By.XPATH, "/html/body/div[1]/div/div[3]/div/div[2]/div/div[1]/div")
    project_titles = (By.XPATH, "/html/body/div[1]/div/div[3]/div/div[2]/div/div[1]/div/div[1]/div[1]/p")
    project_plus_button = (By.XPATH, "//button[@aria-label='AddProject']//span[@class='m_8d3afb97 mantine-ActionIcon-icon']//*[name()='svg']")
    project_name_field = (By.XPATH, "/html/body/div[3]/div/div/div[2]/section/div/div[1]/div/input")
    create_project_button = (By.XPATH, "//span[contains(text(),'Create')]")
    open_project_button = (By.XPATH, "//div[contains(text(),'Automation Project')]/following-sibling::div/a/button/span/span")
    sign_out_button = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/div')


    def is_project_exist(self, project_name):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(self.project_list_container))
        project_elements = self.driver.find_elements(*self.project_titles)

        for project in project_elements:
            if project.text == project_name:
                return project
        return None

    def click_open_project(self, project_element):
        project_element.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[2]/div/div[1]/div/div[1]/div[2]/a[1]/button/span/span').click()

    def click_add_project(self):
        self.driver.find_element(*self.project_plus_button).click()

    def enter_project_name(self, project_name):
        self.driver.find_element(*self.project_name_field).send_keys(project_name)

    def click_create_project(self):
        self.driver.find_element(*self.create_project_button).click()

    def click_sign_out(self):
        self.driver.find_element(*self.sign_out_button).click()
