def solve(s):
    if not s:
        return 0

    seen = {}      # stores the last index of each character
    left = 0       # left pointer of the sliding window
    max_len = 0    # max length of substring found

    for right, ch in enumerate(s):
        if ch in seen and seen[ch] >= left:
            left = seen[ch] + 1
        seen[ch] = right
        curr_len = right - left + 1
        if curr_len > max_len:
            max_len = curr_len

    return max_len
