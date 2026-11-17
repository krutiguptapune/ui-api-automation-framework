class InventoryPage:

    def __init__(self, page):
        self.page = page
        self.sort_dropdown = page.locator('[data-test="product-sort-container"]')
        self.product_names = page.locator('[data-test="inventory-item-name"]')
        self.product_prices = page.locator('[data-test="inventory-item-price"]')
        self.cart_icon = page.locator('[data-test="shopping-cart-link"]')

    def sort_products(self, option):
        self.sort_dropdown.select_option(option)

    def get_product_names(self):
        return self.product_names.all_inner_texts()

    def get_product_prices(self):
        prices = self.product_prices.all_inner_texts()
        return [float(price.replace("$", "")) for price in prices]

    def add_backpack_to_cart(self):
        self.page.locator(
            '[data-test="add-to-cart-sauce-labs-backpack"]'
        ).click()

    def open_cart(self):
        self.cart_icon.click()