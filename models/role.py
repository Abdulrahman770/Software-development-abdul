import enum


class UserType(enum.Enum):
    user = 1
    manager = 2
    administrator = 3


class User:
    def __init__(self, userId, estate, userType):
        self.userId = userId
        self.estate = estate
        self.userType = userType
