#!/usr/bin/env python3
"""Command-line utility to compute square root of an integer."""

import sys
import math


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: sqrt.py <integer>")
        sys.exit(1)
    try:
        value = int(sys.argv[1])
    except ValueError:
        print("Error: input must be an integer")
        sys.exit(1)
    if value < 0:
        print("Error: input must be non-negative")
        sys.exit(1)
    result = math.sqrt(value)
    print(result)


if __name__ == "__main__":
    main()
