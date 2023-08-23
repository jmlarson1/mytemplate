from pathlib import Path


def compute_b(x):
    filename = Path(__file__).resolve()
    print()
    print(f"{filename} called")
    return x**3
