import math

def find_median_sorted_arrays(A, B):
    m, n = len(A), len(B)
    if m > n:
        A, B, m, n = B, A, n, m
    if n == 0:
        return None
    if m == 0:
        if n % 2 == 1:
            return B[n//2]
        else:
            return (B[n//2 - 1] + B[n//2]) / 2.0
    low, high = 0, m
    half_len = (m + n + 1) // 2
    while low <= high:
        i = (low + high) // 2
        j = half_len - i
        A_left = A[i-1] if i > 0 else -math.inf
        A_right = A[i] if i < m else math.inf
        B_left = B[j-1] if j > 0 else -math.inf
        B_right = B[j] if j < n else math.inf
        if A_left <= B_right and B_left <= A_right:
            if (m + n) % 2 == 1:
                return max(A_left, B_left)
            else:
                return (max(A_left, B_left) + min(A_right, B_right)) / 2.0
        elif A_left > B_right:
            high = i - 1
        else:
            low = i + 1
    return None

# Step 5 wrapper
def solve_wrapper():
    A = [1, 3, 5]
    B = [2, 4, 6]
    return find_median_sorted_arrays(sorted(A), sorted(B))

if __name__ == "__main__":
    print("H1 Copilot result:", solve_wrapper())  # Expected: 3.5
