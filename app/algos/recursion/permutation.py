def helper(arr: list, perm: list, perms: list) -> None:
    """
    Recursively generates permutations of an array.

    Args:
        arr (list): The remaining elements to permute.
        perm (list): The current permutation being built.
        perms (list): The list to store all generated permutations.

    Returns:
        None
    """
    if len(arr) == 0:
        # Make a copy of the permutation to avoid appending the same list multiple times.
        perms.append(perm.copy())
    else:
        for ele in arr:
            new_list = arr.copy()
            new_list.remove(ele)
            new_perm = perm.copy()
            new_perm.append(ele)
            helper(new_list, new_perm, perms)


def get_permutations(array: list) -> list:
    """
    Generates all permutations of an array.

    Args:
        array (list): The input array.

    Returns:
        list: A list of all generated permutations.
    """
    if len(array) == 0:
        return []
    perms = []
    helper(array, [], perms)
    return perms


def main() -> list:
    """
    Main method to call the program and demonstrate the functionality.
    """
    array = [1, 2, 3]
    return get_permutations(array)
