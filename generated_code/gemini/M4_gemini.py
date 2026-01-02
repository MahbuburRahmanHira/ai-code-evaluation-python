from typing import List
from collections import defaultdict

def solve(strs: List[str]) -> List[List[str]]:
    """
    Groups anagrams from a list of strings. Anagrams are grouped by their sorted form.
    """
    # Use a defaultdict where the key is the sorted version of a string 
    # and the value is a list of strings that are anagrams of the key.
    anagram_map = defaultdict(list)
    
    for s in strs:
        # Sort the string to create a canonical key for all its anagrams
        # e.g., "eat", "tea", "ate" all become "aet"
        sorted_s = "".join(sorted(s))
        
        # Append the original string to the list corresponding to its sorted key
        anagram_map[sorted_s].append(s)
        
    # The result is the list of all the values (the grouped lists of anagrams) 
    # stored in the hash map.
    return list(anagram_map.values())

if __name__ == '__main__':
    # Test Case 1
    input_1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    output_1 = solve(input_1)
    # The order of the inner lists and the strings within them may vary, 
    # but the content should be the same.
    # Expected groups: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
    print(f"Input: {input_1}, Output: {output_1}") 

    # Test Case 2 (Empty list)
    input_2 = []
    output_2 = solve(input_2)
    print(f"Input: {input_2}, Output: {output_2}") 

    # Test Case 3 (Single element)
    input_3 = ["a"]
    output_3 = solve(input_3)
    print(f"Input: {input_3}, Output: {output_3}") 
    
    # Test Case 4 (Empty strings)
    input_4 = ["", ""]
    output_4 = solve(input_4)
    print(f"Input: {input_4}, Output: {output_4}")

    # Test Case 5 (No anagrams)
    input_5 = ["hello", "world", "test"]
    output_5 = solve(input_5)
    print(f"Input: {input_5}, Output: {output_5}")