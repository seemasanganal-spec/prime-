import sys


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    
    if len(sys.argv) > 1:
        num = int(sys.argv[1])
    else:
        num = int(input("Enter a number: "))

    if is_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")


