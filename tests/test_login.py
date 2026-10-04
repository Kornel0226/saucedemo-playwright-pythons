import pytest
from playwright.sync_api import Page, expect
from config import INVENTORY_URL, LOGIN_URL
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_successful_login(page: Page):
    """Tests that a successful login redirects the user to the inventory page."""
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    expect(page).to_have_url(INVENTORY_URL)
    inventory_page.assert_is_loaded()


@pytest.mark.parametrize(
    "username, password, expected_error",
    [
        (
            "invalid_user",
            "invalid_password",
            "Epic sadface: Username and password do not match any user in this service",
        ),
        (
            "",
            "secret_sauce",
            "Epic sadface: Username is required"
        ),
        (
            "standard_user",
            "",
            "Epic sadface: Password is required"
        ),
        (
            "locked_out_user",
            "secret_sauce",
            "Epic sadface: Sorry, this user has been locked out.",
        ),
    ],
    ids=["invalid_credentials", "empty_username", "empty_password", "locked_out_user"],
)
def test_login_validation_errors(
    page: Page, username: str, password: str, expected_error: str
):
    """Tests various negative login scenarios and verifies appropriate error messages."""
    login_page = LoginPage(page)

    login_page.navigate()
    login_page.login(username, password)

    expect(page).to_have_url(LOGIN_URL)
    login_page.assert_error_message(expected_error)


def test_dismiss_error_message(page: Page):
    """Tests that the error message can be dismissed after an unsuccessful login attempt."""
    login_page = LoginPage(page)

    login_page.navigate()
    login_page.login("invalid_user", "invalid_password")

    expect(page).to_have_url(LOGIN_URL)
    login_page.assert_error_message(
        "Epic sadface: Username and password do not match any user in this service"
    )

    login_page.dismiss_error()
    login_page.assert_error_not_visible()