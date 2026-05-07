class CustomExceptionA(Exception):
    def __init__(self, message: str = "Invalid input", details: str | None = None):
        self.status_code = 400
        self.message = message
        self.details = details


class CustomExceptionB(Exception):
    def __init__(self, message: str = "Resource not found", details: str | None = None):
        self.status_code = 404
        self.message = message
        self.details = details

