def minimum_waiting_time(queries: list[int]) -> int:
    """
    This function takes a list of query times and returns the minimum waiting time
    for all queries to be completed.
    """
    n = len(queries)
    if n <= 1:
        return 0
    sorted_queries = sorted(queries)
    return sum(query * (n - i - 1) for i, query in enumerate(sorted_queries))


def main() -> int:
    return minimum_waiting_time([3, 2, 1, 2, 6])
