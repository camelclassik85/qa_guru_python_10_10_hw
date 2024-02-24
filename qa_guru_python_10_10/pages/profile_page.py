from selene import browser, have
import allure
from qa_guru_python_10_10.data.users import SimpleUser


class ProfilePage:

    @allure.step('Checking registered user information')
    def should_have_registered_user_info(self, user: SimpleUser):
        browser.element('.border').all('p').should(
            have.exact_texts(
                f'Name:{user.full_name}',
                f'Email:{user.email}',
                f'Current Address :{user.current_address}',
                f'Permananet Address :{user.permanent_address}',
            )
        )
