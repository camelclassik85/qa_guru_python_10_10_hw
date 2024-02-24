import allure
from selene import browser, have


class LeftPanel:

    def __init__(self):
        self.elements = browser.element('.category-cards').all('.card-body')
        self.menu_texts = browser.all('.menu-list').all('.text')

    @allure.step('Open category {category} and menu {menu_name}')
    def open(self, category, menu_name):
        browser.open('')
        self.elements.element_by(have.text(category)).click()
        self.menu_texts.element_by(have.text(menu_name)).click()

    @allure.step('Open simple registration form from left menu')
    def open_simple_registration_form(self):
        self.open('Elements', 'Text Box')
