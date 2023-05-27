from typing import List, Union


def product_sum(arr: List[Union[int, List]], depth: int) -> int:
    """
    Recursively calculates the product sum of an array.

    The product sum of an array is defined as the sum of its elements multiplied by
    their respective depths. If an element is a list, its product sum is calculated
    recursively by multiplying the sum of its elements with its depth plus one.

    Args:
        arr (List[Union[int, List]]): The array of integers and nested lists.
        depth (int): The current depth level.

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


def product_sum_array(array: List[Union[int, List]]) -> int:
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


def main() -> int:
    """
    Main method to call the program and demonstrate the functionality.
    """
    return product_sum_array([1, [2, [3, 4]]])
