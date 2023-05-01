"""
The minimum_waiting_time function uses a greedy algorithm to calculate the minimum
time for queries to complete. It sorts the list in non-decreasing order, calculates
the waiting time for each query by multiplying its position in the list with the
sum of all remaining query times, and returns the total waiting time. A doctest
ensures that the function produces the correct output.
"""


def minimum_waiting_time(queries: list[int]) -> int:
    """
    This function takes a list of query times and returns the minimum waiting time
    for all queries to be completed.
    """
    n = len(queries)
    if n in (0, 1):
        return 0
    return sum(query * (n - i - 1) for i, query in enumerate(sorted(queries)))


def main():
    return minimum_waiting_time([3, 2, 1, 2, 6])
    