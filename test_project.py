from os import times

import pytest
import time
from selenium import webdriver
from pages.login_page import LoginPage
from pages.projects_page import ProjectsPage
from pages.project_details_page import ProjectDetailsPage
from selenium.webdriver.common.keys import Keys



@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_project_creation_and_navigation(driver):
    login_page = LoginPage(driver)
    projects_page = ProjectsPage(driver)
    project_details_page = ProjectDetailsPage(driver)


    login_page.load()
    time.sleep(2)
    login_page.enter_email("sahal.ahamad@brainstation-23.com")
    login_page.enter_password("123456@Aa")
    login_page.click_sign_in()
    time.sleep(10)


    project_name = "Automation Project"
    existing_project = projects_page.is_project_exist(project_name)
    if existing_project:
        print(f"Project '{project_name}' found, opening it.")
        projects_page.click_open_project(existing_project)
    else:
        print(f"Project '{project_name}' not found, creating a new one.")
        projects_page.click_add_project()
        time.sleep(2)
        projects_page.enter_project_name(project_name)
        projects_page.click_create_project()
        time.sleep(5)


        new_project_element = projects_page.is_project_exist(project_name)
        projects_page.click_open_project(new_project_element)


    time.sleep(5)
    project_details_page.click_film_next()
    time.sleep(2)
    project_details_page.select_drama()
    project_details_page.select_horror()
    project_details_page.select_action()
    time.sleep(5)
    project_details_page.click_qualities_next()
    project_details_page.select_film_length()
    project_details_page.select_hosting_site()
    time.sleep(2)
    project_details_page.select_next_hosting()
    time.sleep(5)
    project_details_page.enter_name("sahal")
    project_details_page.enter_website("sahal.com")
    project_details_page.enter_target_audience("age between 15 to 50 years old ")
    time.sleep(5)
    project_details_page.select_next_button_input()
    project_details_page.enter_log_line("In a game where passion meets strategy, the last-minute goal tells the real story")
    time.sleep(5)
    project_details_page.select_log_line_next()
    time.sleep(20)
    project_details_page.scroll_video_check_box(Keys.PAGE_DOWN)
    time.sleep(5)
    project_details_page.select_video_check_box()
    time.sleep(5)
    project_details_page.select_video_check_box_next_button()
    time.sleep(5)
    project_details_page.enter_budget("$500")
    project_details_page.scroll_calendar_page(Keys.PAGE_DOWN)
    time.sleep(10)
    project_details_page.select_date("November 2024", "29")
    time.sleep(10)


    print("Current title of the website is "+driver.title)
    projects_page.click_sign_out()
    print("Signed out successfully.")
    time.sleep(2)
