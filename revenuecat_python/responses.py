class RevenueCatError(Exception):
    def __init__(
        self,
        message=None,
        http_status=None,
        json_body=None,
        headers=None,
    ):
        super(RevenueCatError, self).__init__(message)

        self._message = message
        self.http_status = http_status
        self.json_body = json_body
        self.headers = headers or {}

    def __str__(self):
        return self._message or "<empty message>"

    def __repr__(self):
        return "(message={}, http_status={})".format(self._message, self.http_status)


class RevenueCatResponse:
    def __init__(
        self,
        http_status=None,
        json_body=None,
        headers=None,
    ):
        self.http_status = http_status
        self.json_body = json_body
        self.headers = headers or {}
