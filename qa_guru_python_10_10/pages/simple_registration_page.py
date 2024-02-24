import allure
from selene import browser
from qa_guru_python_10_10.data.users import SimpleUser


class SimpleUserRegistrationPage:

    def __init__(self):
        self.full_name = browser.element('#userName')
        self.email = browser.element('#userEmail')
        self.current_address = browser.element("#currentAddress")
        self.permanent_address = browser.element("#permanentAddress")
        self.submit_button = browser.element("#submit")

    @allure.step('Open simple user registration page')
    def open(self):
        browser.open("/text-box")

    @allure.step('Simple user registration')
    def simple_user_registration(self, user: SimpleUser):
        self.full_name.type(user.full_name)
        self.email.type(user.email)
        self.current_address.type(user.current_address)
        self.permanent_address.type(user.permanent_address)
        self.submit_button.click()
