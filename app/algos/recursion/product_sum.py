"""
We need to create a function that calculates the product sum of a "special" array.
This array can contain integers or nested arrays. The product sum is obtained by
adding all the elements together and multiplying by their respective depth.

For example, in the array [x, y], the product sum is (x + y). In the array [x, [y, z]],
the product sum is x + 2 * (y + z). In the array [x, [y, [z]]],
the product sum is x + 2 * (y + 3z).
"""


def product_sum(arr: list, depth: int) -> int:
    """
    Recursively calculates the product sum of an array.

    The product sum of an array is defined as the sum of its elements multiplied by
    their respective depths.If an element is a list, its product sum is calculated
    recursively by multiplying the sum of its elements with its depth plus one.

    Args:
        arr: The array of integers and nested lists.
        depth: The current depth level.

    Returns:
        int: The product sum of the array.
    """
    total_sum = 0
    for ele in arr:
        if isinstance(ele, list):
            total_sum += product_sum(ele, depth + 1)
        else:
            total_sum += ele
    return total_sum * depth


def product_sum_array(array: list) -> int:
    """
    Calculates the product sum of an array.

    Args:
        array (List[Union[int, List]]): The array of integers and nested lists.

    Returns:
        int: The product sum of the array.

    Examples:
        product_sum_array([1, 2, 3])
        6
        product_sum_array([1, [2, 3]])
        11
    """
    return product_sum(array, 1)


def main():
    return product_sum_array([1, [2, [3, 4]]])
