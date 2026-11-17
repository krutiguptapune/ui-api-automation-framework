class CheckoutPage:

    def __init__(self, page):
        self.page = page

        self.first_name = page.locator('[data-test="firstName"]')
        self.last_name = page.locator('[data-test="lastName"]')
        self.postal_code = page.locator('[data-test="postalCode"]')
        self.continue_button = page.locator('[data-test="continue"]')
        self.finish_button = page.locator('[data-test="finish"]')
        self.complete_header = page.locator('[data-test="complete-header"]')

    def enter_customer_details(self, first, last, postal):
        self.first_name.fill(first)
        self.last_name.fill(last)
        self.postal_code.fill(postal)

    def click_continue(self):
        self.continue_button.click()

    def finish_order(self):
        self.finish_button.click()

    def get_confirmation_message(self):
        return self.complete_header.inner_text()