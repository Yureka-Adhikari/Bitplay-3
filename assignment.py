def longest_consecutive_ones(n):
    binary = bin(n)[2:]
    ones_groups = binary.split('0')
    return max(len(group) for group in ones_groups)

number = int(input("Enter a number: "))
print(f"Longest consecutive 1's: {longest_consecutive_ones(number)}")