# API BASE
from playwright.sync_api import Playwright
baseUrl = "https://rahulshettyacademy.com/client"
ordersPayLoad = {"orders": [{"country": "Germany", "productOrderedId": "6581cade9fd99c85e8ee7ff5"}]}
# loginPayLoad = {"userEmail": "gregsmith@gmail.com", "userPassword": "Iamking@000"}


class APIUtils:

    def get_token(self, playwright:Playwright):
        api_req_contetx = playwright.request.new_context(base_url="https://rahulshettyacademy.com/client")
        response_result = api_req_contetx.post("/api/ecom/auth/login",
                                               data={"userEmail": "gregsmith@gmail.com" , "userPassword": "Iamking@000"})
        assert response_result.ok
        print(response_result.json())
        response_body = response_result.json()
        return response_body["token"]


    def create_order(self, playwright:Playwright):
        token = self.get_token(playwright)
        api_req_contetx = playwright.request.new_context(base_url="https://rahulshettyacademy.com/client")
        response_result = api_req_contetx.post("/api/ecom/order/create-order",
                            data=ordersPayLoad,
                            headers= {"Authorization": token, "Content-Type": "application/json"})

        print(response_result.json())

        response_body = response_result.json()
        orderId = response_body["orders"][0]
        # print("Order Id: " + orderId)
        return orderId


