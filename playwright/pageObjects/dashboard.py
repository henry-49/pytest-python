# Dashboard Page
from .orders_history import OrdersHistoryPage


class DashboardPage:

    # constructor
    def __init__(self, page):
        self.page = page

    def select_orders_navigation_link(self):
        # orders history page -> order is present
        self.page.get_by_role("button", name="ORDERS").click()
        order_history_page = OrdersHistoryPage(self.page)
        return order_history_page

