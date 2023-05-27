def factorial(n: int) -> int:
    """
    Compute the factorial of a non-negative integer n.
    """
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


def main() -> int:
    return factorial(5)
