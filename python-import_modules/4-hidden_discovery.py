#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    # Get all names defined in the module
    names = dir(hidden_4)
    
    # Filter names that don't start with '__' and sort alphabetically
    filtered_names = [name for name in names if not name.startswith('__')]
    filtered_names.sort()
    
    # Print one name per line
    for name in filtered_names:
        print(name)
