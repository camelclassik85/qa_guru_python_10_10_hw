import allure
from allure_commons.types import Severity
from qa_guru_python_10_10.application import app
from qa_guru_python_10_10.data import users


@allure.tag('qa_guru_python_10_10_hw')
@allure.severity(Severity.CRITICAL)
@allure.label('Owner', 'AD')
@allure.feature('Simple registration form')
@allure.story('Filling simple registration form')
@allure.link('https://demoqa.com', name='Text Box')
def test_simple_user_registration():
    app.left_panel.open_simple_registration_form()

    app.simple_registration_form.simple_user_registration(users.gg)

    app.profile.should_have_registered_user_info(users.gg)
