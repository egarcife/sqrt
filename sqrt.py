#!/usr/bin/env python3
"""Utilidad de línea de comandos para calcular la raíz cuadrada de un entero."""

import sys
import math


def main() -> None:
    if len(sys.argv) != 2:
        print("Uso: sqrt.py <entero>")
        sys.exit(1)
    try:
        value = int(sys.argv[1])
    except ValueError:
        print("Error: la entrada debe ser un entero")
        sys.exit(1)
    if value < 0:
        print("Error: la entrada debe ser no negativa")
        sys.exit(1)
    result = math.sqrt(value)
    print(result)


if __name__ == "__main__":
    main()
