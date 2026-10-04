import pytest
from playwright.sync_api import Playwright

@pytest.fixture(scope="session", autouse=True)
def configure_playwright(playwright: Playwright):
    """
    Configures the Playwright environment before tests are run.
    This function can be used to set up browser contexts, launch options, etc.
    """
    playwright.selectors.set_test_id_attribute("data-test")