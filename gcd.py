def gcd(m, n):
    """
    Uses Euclid's method to compute the greatest common divisor
    (also called greatest common factor) of m and n.
    REturns the GCD of m and n.
    """
    if n == 0:
        return m
    else:
        return gcd(n, m % n)

def iterative_gcd(num1, num2):
    """
    Uses a naive algorithm to compute the greatest common divisor
    returns the GCD of m and n.
    """

    min = num1 if num1 < num2 else num2
    largest_factor = 1;
    for i in range(1, min + 1):
        if num1 % i == 0 and num2 % i == 0:
            largest_factor = i
    return largest_factor

def main():
    """ Try out the gcd function """
    for num1 in range(1, 101):
        for num2 in range(1, 101):
            print("gcd of", num1, "and", num2, "is", gcd(num1, num2))

main()