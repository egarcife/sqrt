import subprocess
import sys


def run_sqrt(arg: str) -> str:
    result = subprocess.run([sys.executable, "sqrt.py", arg], capture_output=True, text=True)
    return result.stdout.strip()


def test_perfect_square():
    assert run_sqrt("9") == "3.0"


def test_zero():
    assert run_sqrt("0") == "0.0"


def test_non_square():
    assert run_sqrt("2") == str(2 ** 0.5)


def test_negative():
    result = subprocess.run([sys.executable, "sqrt.py", "-1"], capture_output=True, text=True)
    assert result.returncode != 0
    assert "no negativa" in result.stdout


def test_invalid_input():
    result = subprocess.run([sys.executable, "sqrt.py", "abc"], capture_output=True, text=True)
    assert result.returncode != 0
    assert "debe ser un entero" in result.stdout

