def solve(x: int) -> bool:
    if x < 0:
        return False
    
    if x == 0:
        return True

    # Reverses the second half of the number and compares it with the first half.
    reverted_number = 0
    temp = x
    
    while temp > reverted_number:
        reverted_number = reverted_number * 10 + temp % 10
        temp //= 10

    # For even number of digits, temp == reverted_number.
    # For odd number of digits, temp == reverted_number // 10 
    # (since the middle digit is skipped in the reverted_number).
    return temp == reverted_number or temp == reverted_number // 10

if __name__ == '__main__':
    pass