class CartPage:

    def __init__(self, page):
        self.page = page
        self.checkout_button = page.locator('[data-test="checkout"]')
        self.cart_items = page.locator('[data-test="inventory-item-name"]')

    def get_cart_items(self):
        return self.cart_items.all_inner_texts()

    def click_checkout(self):
        self.checkout_button.click()

    def remove_backpack(self):
        self.page.locator(
            '[data-test="remove-sauce-labs-backpack"]'
        ).click()

    def get_cart_count(self):
        return self.cart_items.count()