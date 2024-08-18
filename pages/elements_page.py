import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from self import self

from generator.generator import generated_person
from locators.elements_page_locators import TextBoxPageLocators
from pages.base_page import BasePage


class WebDriver:
    driver = webdriver.Chrome()


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        # используем генераторы:
        person_info = next(generated_person())  # возьмем  поля ниже по одному разу
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address
        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        return full_name, email, current_address, permanent_address

    def move_to_element(self, element):
        element = self.element_is_visible(self.locators.SUBMIT)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.element_is_visible(self.locators.SUBMIT).click()
        time.sleep(2)
        return (self.locators.FULL_NAME, self.locators.EMAIL, self.locators.CURRENT_ADDRESS,
                self.locators.PERMANENT_ADDRESS)

    @property
    def check_filled_form(self):  # проверка введенного текста в полях
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(':')[1]
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(':')[1]
        current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, current_address, permanent_address
