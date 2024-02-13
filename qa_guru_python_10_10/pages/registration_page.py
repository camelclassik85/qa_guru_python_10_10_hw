from selene import browser, be, have, command
from qa_guru_python_10_10 import resource
import allure


class RegistrationPage:

    @allure.step('Open practice-form')
    def open(self):
        browser.open("automation-practice-form")

    @allure.step('Fill first name {value}')
    def fill_first_name(self, value):
        browser.element('#firstName').should(be.blank).type(value)

    @allure.step('Fill last name {value}')
    def fill_last_name(self, value):
        browser.element('#lastName').should(be.blank).type(value)

    @allure.step('Fill email {value}')
    def fill_user_email(self, value):
        browser.element('#userEmail').should(be.blank).type(value)

    @allure.step('Choose gender {value}')
    def choose_gender(self, value):
        browser.all('[for^=gender-radio]').element_by(have.exact_text(value)).click()

    @allure.step('Fill phone number {value}')
    def fill_phone_number(self, value):
        browser.element('#userNumber').should(be.blank).type(value)

    @allure.step('Fill date of birth {year}.{month}.{day}')
    def fill_date_of_birth(self, year: int, month: int, day: int):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').click()
        browser.element(f'[value="{year}"]').perform(command.js.scroll_into_view).click()
        browser.element('.react-datepicker__month-select').click().element(f'[value="{month - 1}"]').click()
        browser.element(f'.react-datepicker__day--0{day}').click()

    @allure.step('Fill subjects {value1}, {value2}')
    def fill_subjects(self, value1, value2):
        browser.element('#subjectsInput').should(be.blank).type(value1).press_enter()
        browser.element('#subjectsInput').type(value2)
        browser.element('#react-select-2-option-0').click()

    @allure.step('Choose hobbies {args}')
    def choose_hobbies(self, *args):
        browser.element('[for=hobbies-checkbox-2]').perform(command.js.scroll_into_view)
        for hobby in args:
            browser.all('[for^=hobbies-checkbox]').element_by(have.exact_text(hobby)).click()

    @allure.step('Upload picture {value}')
    def upload_picture(self, value):
        browser.element('#uploadPicture').send_keys(resource.path(value))

    @allure.step('Fill current address {value}')
    def fill_current_address(self, value):
        browser.element('#currentAddress').should(be.blank).type(value)

    @allure.step('Fill state {value}')
    def fill_state(self, value):
        browser.element('#state').click()
        browser.all("[id^='react-select-3-option']").element_by(have.exact_text(value)).click()

    @allure.step('Fill city {value}')
    def fill_city(self, value):
        browser.element('#city').click()
        browser.all("[id^='react-select-4-option']").element_by(have.exact_text(value)).click()

    @allure.step('Submit')
    def click_submit_button(self):
        browser.element('#submit').perform(command.js.click)

    @allure.step('Check data correctness after registration')
    def should_registered_user_with(self, first_name, last_name, email, gender, number, date_of_birth, subjects, hobbies,
                                    photo, current_address, state, city):
        browser.element('.modal-dialog').should(be.existing)
        browser.element(".table").all('td').even.should(
            have.exact_texts(
                f'{first_name} {last_name}',
                email,
                gender,
                number,
                date_of_birth,
                subjects,
                hobbies,
                photo,
                current_address,
                f'{state} {city}',
            ))
