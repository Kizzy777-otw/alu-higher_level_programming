#!/usr/bin/python3
def raise_exception_msg(message=""):
    """Raise a NameError exception with a message"""
    if not isinstance(message, str):
        raise TypeError("Message must be a string")
    raise NameError(message)
