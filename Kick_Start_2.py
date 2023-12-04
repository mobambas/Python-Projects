def min_operations_to_favorite(S, F):
    def distance(a, b):
        return min(abs(ord(a) - ord(b)), 26 - abs(ord(a) - ord(b)))

    total_operations = 0
    for i in range(len(S)):
        current_char = S[i]
        target_char = F[i % len(F)]  # Using modulo to cycle through the favorite letters
        total_operations += distance(current_char, target_char)

    return total_operations

# Example usage:
S = "abc"
F = "abz"
result = min_operations_to_favorite(S, F)
print("Minimum operations:", result)
