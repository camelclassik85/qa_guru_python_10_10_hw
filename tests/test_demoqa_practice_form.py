from qa_guru_python_10_10.pages.registration_page import RegistrationPage
import allure
from allure_commons.types import Severity


@allure.tag('qa_guru_python_10_10_hw')
@allure.severity(Severity.CRITICAL)
@allure.label('Owner', 'AD')
@allure.feature('Student Registration Form')
@allure.story('Filling registration form')
def test_fill_registration_form():

    registration_form = RegistrationPage()

    # open registration form
    registration_form.open()
    
    # WHEN
    registration_form.fill_first_name('Good')
    registration_form.fill_last_name('Game')
    registration_form.fill_user_email('gg@goga.com')
    registration_form.choose_gender('Male')
    registration_form.fill_phone_number('9876543210')
    registration_form.fill_date_of_birth(year=1955, month=7, day=20)
    registration_form.fill_subjects('comp', 'eng')
    registration_form.choose_hobbies('Sports', 'Music')
    registration_form.upload_picture('cat.jpg')
    registration_form.fill_current_address('Good for good 123456')
    registration_form.fill_state('Haryana')
    registration_form.fill_city('Karnal')
    registration_form.click_submit_button()

    # THEN
    registration_form.should_registered_user_with(
            'Good',
            'Game',
            'gg@goga.com',
            'Male',
            '9876543210',
            '20 July,1955',
            'Computer Science, English',
            'Sports, Music',
            'cat.jpg',
            'Good for good 123456',
            'Haryana',
            'Karnal',
    )
