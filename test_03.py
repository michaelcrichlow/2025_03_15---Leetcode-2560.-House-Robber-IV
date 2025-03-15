# Leetcode 2560. House Robber IV


# 1.) Testcases Passed!
# 2.) WORKS! Memory Limit Exceeded. (28 / 64 testcases passed)
def minCapability(nums: list[int], k: int) -> int:    
    def get_non_adjacent_power_set(l: list[int], k: int) -> list[list[int]]:
        def helper(index: int, current: list[int], result: list[list[int]]):
            # If we've reached the end of the list, add the current subset to results
            if index >= len(l):
                result.append(current[:])  # Add a copy of the current subset
                return

            # Option 1: Skip the current number (move to the next index)
            helper(index + 1, current, result)

            # Option 2: Include the current number (skip the next number to avoid adjacency)
            current.append(l[index])
            helper(index + 2, current, result)
            current.pop()  # Backtrack to explore other possibilities

        # Initialize the result list and call the helper function
        result = [[]]
        helper(0, [], result)

        # filter the results to subsets that are `k` elements long
        res = []
        for val in result:
            if len(val) == k:
                res.append(val)

        return res
    
    local_array = get_non_adjacent_power_set(nums, k)
    _maxs = []
    for val in local_array:
        _maxs.append(max(val))

    
    return min(_maxs)

def main() -> None:
    print(minCapability(nums = [2,3,5,9], k = 2))
    print(minCapability(nums = [2,7,9,3,1], k = 2))
    # # First thoughts:
    # # Bad testcases: Don't reveal the depth of what is being asked.
    print(minCapability(nums = [4,22,11,14,25], k = 3)) # testcase 7 (error)
    print(minCapability(nums = [9,6,20,21,8], k = 3)) # testcase 17 (error)
        


if __name__ == '__main__':
    main()