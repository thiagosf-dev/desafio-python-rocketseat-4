class HttpBadRequestError(Exception):
    def __init__(self, message: str = 'BadRequest') -> None:
        super().__init__(message)
        self.message = message
        self.status_code = 400
        self.name = 'BadRequest'
