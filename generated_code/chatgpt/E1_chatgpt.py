def two_sum(nums, target):
    # Dictionary to store numbers we've seen and their indices
    index_map = {}
    
    for i, num in enumerate(nums):
        # Calculate the number we need to find
        needed = target - num
        # If we already saw the needed number, return its index and current index
        if needed in index_map:
            return [index_map[needed], i]
        # Otherwise, store the current number and its index
        index_map[num] = i
        
    # Return empty list if no solution is found
    return []

# Example usage
print(two_sum([2, 7, 11, 15], 9))
