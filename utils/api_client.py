import time
from playwright._impl._errors import Error
from utils.logger import get_logger


class APIClient:

    def __init__(self, request_context):
        self.request_context = request_context
        self.logger = get_logger("api")

    def _request_with_retry(self, method, url, **kwargs):

        for attempt in range(3):
            try:
                self.logger.info(
                    f"{method} request: {url} | Attempt {attempt + 1}"
                )

                response = getattr(
                    self.request_context, method.lower()
                )(url, **kwargs)

                return response

            except Error as error:
                if attempt == 2:
                    self.logger.error(
                        f"{method} request failed after 3 attempts: {error}"
                    )
                    raise

                self.logger.warning(
                    f"Temporary API connection error. Retrying: {error}"
                )
                time.sleep(2)

    def get(self, url, params=None, headers=None):
        return self._request_with_retry(
            "GET", url, params=params, headers=headers
        )

    def post(self, url, data=None, headers=None):
        return self._request_with_retry(
            "POST", url, data=data, headers=headers
        )

    def put(self, url, data=None, headers=None):
        return self._request_with_retry(
            "PUT", url, data=data, headers=headers
        )

    def patch(self, url, data=None, headers=None):
        return self._request_with_retry(
            "PATCH", url, data=data, headers=headers
        )

    def delete(self, url, headers=None):
        return self._request_with_retry(
            "DELETE", url, headers=headers
        )