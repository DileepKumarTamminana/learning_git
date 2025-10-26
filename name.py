#test
import sys

#!/usr/bin/env python3
"""Reverse a string."""

def reverse_string(s: str) -> str:
    """Return the reverse of the given string."""
    return s[::-1]

def main() -> None:
    if len(sys.argv) > 1:
        # join arguments so "python name.py hello world" reverses "hello world"
        src = " ".join(sys.argv[1:])
    else:
        try:
            src = input("Enter string: ")
        except EOFError:
            return
    print(reverse_string(src))

if __name__ == "__main__":
    main()
    #commit test
