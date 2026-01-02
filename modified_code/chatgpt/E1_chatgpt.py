# ----------------------------
# Original ChatGPT logic preserved
# ----------------------------
def two_sum(nums, target):
    index_map = {}
    for i, num in enumerate(nums):
        needed = target - num
        if needed in index_map:
            return [index_map[needed], i]
        index_map[num] = i
    return []

# ----------------------------
# Step 5: Uniform solve wrapper
# ----------------------------
def solve():
    nums = [2, 7, 11, 15]
    target = 9
    return two_sum(nums, target)

if __name__ == "__main__":
    result = solve()
    print("E1_chatgpt two-sum result:", result)
