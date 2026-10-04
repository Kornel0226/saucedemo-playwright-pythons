from playwright.sync_api import Page, expect

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.inventory_items = page.get_by_test_id("inventory-item")

    def navigate(self):
        """Navigates to the SauceDemo inventory page."""
        self.page.goto("https://www.saucedemo.com/inventory.html")

    def assert_is_loaded(self):
        """Asserts that the inventory page is loaded by checking for the presence of inventory items."""
        expect(self.inventory_items.first).to_be_visible()
       