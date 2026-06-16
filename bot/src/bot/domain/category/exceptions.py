from bot.domain.shared import DomainException


class CategoryNotFoundException(DomainException):
    pass


class CategoryAlreadyExistsException(DomainException):
    pass
