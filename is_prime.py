#!/usr/bin/env python3
import math

def is_prime(n):
    """Check if n is prime by dividing by odd numbers up to sqrt(n)."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    limit = int(math.sqrt(n)) + 1
    for i in range(3, limit, 2):
        if n % i == 0:
            return False
    return True

def main():
    try:
        n = int(input("Enter an integer: "))
    except ValueError:
        print("Please enter a valid integer.")
        return

    if is_prime(n):
        print(f"{n} is a prime number.")
    else:
        print(f"{n} is not a prime number.")

if __name__ == "__main__":
    main()
