class Error(Exception):
    """Base class for other exceptions"""
    pass


class MethodNotCallableForThatClass(Error):
    """Raised when not applicable for that character"""
    pass
