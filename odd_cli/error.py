class CreateTokenError(Exception):
    def __init__(self, name, reason):
        super().__init__(f"Couldn't create token with {name=} by {reason=}")
