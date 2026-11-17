class APIClient:

    def __init__(self, request_context):
        self.request_context = request_context

    def get(self, url, params=None, headers=None):
        return self.request_context.get(
            url,
            params=params,
            headers=headers
        )

    def post(self, url, data=None, headers=None):
        return self.request_context.post(
            url,
            data=data,
            headers=headers
        )

    def put(self, url, data=None, headers=None):
        return self.request_context.put(
            url,
            data=data,
            headers=headers
        )

    def patch(self, url, data=None, headers=None):
        return self.request_context.patch(
            url,
            data=data,
            headers=headers
        )

    def delete(self, url, headers=None):
        return self.request_context.delete(
            url,
            headers=headers
        )