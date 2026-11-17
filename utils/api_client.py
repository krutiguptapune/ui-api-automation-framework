from utils.logger import get_logger


class APIClient:

    def __init__(self, request_context):
        self.request_context = request_context
        self.logger = get_logger("api")

    def get(self, url, params=None, headers=None):
        self.logger.info(f"GET request: {url}")
        return self.request_context.get(
            url, params=params, headers=headers
        )

    def post(self, url, data=None, headers=None):
        self.logger.info(f"POST request: {url}")
        return self.request_context.post(
            url, data=data, headers=headers
        )

    def put(self, url, data=None, headers=None):
        self.logger.info(f"PUT request: {url}")
        return self.request_context.put(
            url, data=data, headers=headers
        )

    def patch(self, url, data=None, headers=None):
        self.logger.info(f"PATCH request: {url}")
        return self.request_context.patch(
            url, data=data, headers=headers
        )

    def delete(self, url, headers=None):
        self.logger.info(f"DELETE request: {url}")
        return self.request_context.delete(
            url, headers=headers
        )