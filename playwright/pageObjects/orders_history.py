# Order History Page
from .order_details import OrderDetailsPage


class OrdersHistoryPage:

    def __init__(self, page):
        self.page = page


    def select_order(self, orderId):
        order_row = self.page.locator("tr", has_text=orderId)
        order_row.get_by_role("button", name="View").click()
        order_detail_page = OrderDetailsPage(self.page)
        return order_detail_page