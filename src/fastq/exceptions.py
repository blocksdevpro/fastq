class FastQException(Exception):
    """Base exception for FastQ"""

    pass


class FastQTaskNotFoundException(FastQException):
    """Exception for task not found"""

    pass
