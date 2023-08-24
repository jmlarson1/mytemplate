from pathlib import Path


def compute(x):
    filename = Path(__file__).resolve()
    print(f"{filename} called")
    return 5.0 * x
