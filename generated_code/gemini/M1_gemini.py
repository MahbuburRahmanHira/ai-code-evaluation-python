def solve(s: str) -> int:
    """
    Given a string s, return the length of the longest substring without repeating characters.
    """
    n = len(s)
    if n == 0:
        return 0

    # A set to store characters in the current window (substring s[left:right+1])
    char_set = set()
    
    # left pointer of the sliding window
    left = 0
    
    # Maximum length found so far
    max_length = 0

    # right pointer iterates from the start to the end of the string
    for right in range(n):
        # If the character at 'right' is already in the set, 
        # it means we have a repeating character.
        while s[right] in char_set:
            # Shrink the window from the left by removing the character at 'left'
            char_set.remove(s[left])
            left += 1
        
        # Add the current character (s[right]) to the set as it's now unique
        char_set.add(s[right])
        
        # Update the maximum length found so far
        # The current substring length is right - left + 1
        max_length = max(max_length, right - left + 1)

    return max_length

if __name__ == '__main__':
    # Test cases
    print(f"Input: 'abcabcbb', Output: {solve('abcabcbb')}")
    print(f"Input: 'bbbbb', Output: {solve('bbbbb')}")
    print(f"Input: 'pwwkew', Output: {solve('pwwkew')}")
    print(f"Input: '', Output: {solve('')}")
    print(f"Input: 'a', Output: {solve('a')}")
    print(f"Input: 'dvdf', Output: {solve('dvdf')}")
    print(f"Input: ' ', Output: {solve(' ')}")
    print(f"Input: 'au', Output: {solve('au')}")