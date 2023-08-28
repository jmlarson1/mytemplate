from pathlib import Path


def compute_a(x):
    filename = Path(__file__).resolve()
    print()
    print(f"{filename} called")
    
    if x < -100:
        print("this line should never be covered")
        k = 1+1
        print("this line also should never be covered")
    return x**2
