def matrix_chain_order(p):
    n = len(p) - 1  # Number of matrices
    m = [[0] * (n + 1) for _ in range(n + 1)]  # Initialize a 2D table for storing costs
    s = [[0] * (n + 1) for _ in range(n + 1)]  # Initialize a 2D table for storing split points

    # Calculate the cost of multiplying chains of increasing lengths
    for chain_len in range(2, n + 1):
        for i in range(1, n - chain_len + 2):
            j = i + chain_len - 1
            m[i][j] = float('inf')  # Initialize to positive infinity
            for k in range(i, j):
                # Calculate the cost of multiplying matrices from i to k and from k+1 to j
                cost = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                if cost < m[i][j]:
                    m[i][j] = cost
                    s[i][j] = k

    return m, s

def print_optimal_parenthesization(s, i, j):
    if i == j:
        print("A", i, end="")
    else:
        print("(", end="")
        print_optimal_parenthesization(s, i, s[i][j])
        print_optimal_parenthesization(s, s[i][j] + 1, j)
        print(")", end="")

# Example usage:
matrix_dimensions = [30, 35, 15, 5, 10, 20, 25]
m, s = matrix_chain_order(matrix_dimensions)
print("Optimal Parenthesization:")
print_optimal_parenthesization(s, 1, len(matrix_dimensions) - 1)
print("\nMinimum Scalar Multiplications:", m[1][-1])
