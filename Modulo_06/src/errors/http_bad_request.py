class HttpUnprocessableEntityError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.massage = message
        self.name = 'Bad Request'
        self.status_code = 400