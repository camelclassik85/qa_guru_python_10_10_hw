from qa_guru_python_10_10.components.left_panel import LeftPanel
from qa_guru_python_10_10.pages.profile_page import ProfilePage
from qa_guru_python_10_10.pages.simple_registration_page import SimpleUserRegistrationPage


class ApplicationManager:
    def __init__(self):
        self.simple_registration_form = SimpleUserRegistrationPage()
        self.profile = ProfilePage()
        self.left_panel = LeftPanel()


app = ApplicationManager()
