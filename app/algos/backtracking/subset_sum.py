from typing import List


def generate_sum_of_subsets_soln(nums: List[int], max_sum: int) -> List[List[int]]:
    result: List[List[int]] = []
    path: List[int] = []
    num_index = 0
    remaining_nums_sum = sum(nums)
    create_state_space_tree(nums, max_sum, num_index,
                            path, result, remaining_nums_sum)
    return result


def create_state_space_tree(
    nums: List[int],
    max_sum: int,
    num_index: int,
    path: List[int],
    result: List[List[int]],
    remaining_nums_sum: int,
) -> None:
    """
    Creates a state space tree to iterate through each branch using DFS.
    It terminates the branching of a node when any of the two conditions
    given below satisfy.
    This algorithm follows depth-first search and backtracks when the node is not branchable.
    """
    if sum(path) > max_sum or (remaining_nums_sum + sum(path)) < max_sum:
        return
    if sum(path) == max_sum:
        result.append(path)
        return
    for index in range(num_index, len(nums)):
        create_state_space_tree(
            nums,
            max_sum,
            index + 1,
            path + [nums[index]],
            result,
            remaining_nums_sum - nums[index],
        )


def main() -> List[List[int]]:
    nums = [3, 34, 4, 12, 5, 2]
    max_sum = 9
    return generate_sum_of_subsets_soln(nums, max_sum)
