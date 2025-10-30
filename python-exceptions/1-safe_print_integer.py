#!/usr/bin/python3
def safe_print_integer(value):
    """Print an integer with formatting"""
    try:
        print("{:d}".format(value))
        return True
    except ValueError:
        return False
    except TypeError:
        return False
