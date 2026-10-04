from playwright.sync_api import Page, expect
from config import LOGIN_URL

class LoginPage:
    """SauceDemo login Page Object Model class."""

    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.get_by_placeholder("Username")
        self.password_input = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.error_message = page.get_by_test_id("error")
        self.close_error_button = page.get_by_role("button", name="Dismiss error")

    def navigate(self):
        """Navigates to the SauceDemo login page."""
        self.page.goto(LOGIN_URL)

    def login(self, username: str, password: str):
        """Logs in with the specified username and password."""

        # Fill in the username and password fields and click the login button
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def assert_error_message(self, expected_message: str):
        """Asserts that the error message is displayed on the login page."""
        expect(self.page.get_by_text(expected_message)).to_be_visible()

    def dismiss_error(self):
        """Dismisses the error message on the login page."""
        self.close_error_button.click()

    def assert_error_not_visible(self):
        """Asserts that the error message is not visible on the login page."""
        expect(self.error_message).not_to_be_visible()