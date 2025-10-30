#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """Add two tuples element-wise"""
    # Ensure both tuples have at least 2 elements, using 0 for missing values
    a1 = tuple_a[0] if len(tuple_a) >= 1 else 0
    a2 = tuple_a[1] if len(tuple_a) >= 2 else 0
    
    b1 = tuple_b[0] if len(tuple_b) >= 1 else 0
    b2 = tuple_b[1] if len(tuple_b) >= 2 else 0
    
    return (a1 + b1, a2 + b2)
