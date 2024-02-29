def dynamic_padovan():
    memo = {}
    def padovan(n):
        if n in memo:
            return memo[n]
        elif n < 3:
            # base case
            return 1
        else:
            memo[n] = padovan(n - 2) + padovan(n - 3)
            return memo[n]
    return padovan

padovan_equation = dynamic_padovan()

# Multiplies two matrices together and returns the result
def matrix_mult(matrixA, matrixB):
    # Get rows and cols
    rows = len(matrixA)
    cols = len(matrixA[0])
    # Initialize result matrix
    result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    # Multiply matrices, rows * cols
    for i in range(rows):
        for j in range(cols):
            for k in range(cols):
                result[i][j] += matrixA[i][k] * matrixB[k][j]
    return result

# Raises a matrix to an exponent of itself
def matrix_exponentiation(matrix, exponent):
    # Anything to the power of 1 is itself
    if exponent == 1:
        return matrix
    # If even, then recursively compute half of the exponent
    if exponent % 2 == 0:
        half_exponent = matrix_exponentiation(matrix, exponent // 2)
        return matrix_mult(half_exponent, half_exponent)
    # If odd, recursively compute the half of the exponent minus one
    half = matrix_exponentiation(matrix, exponent // 2)
    full_exponent = matrix_mult(half, half)
    return matrix_mult(full_exponent, matrix)

# Utilizes matrix exponentiation to calculate the Padovan sequence in logarithmic time
def padovan_matrix_exponentiation(n):
    if n < 3:
        return 1
    matrix = [[1, 1, 0], [0, 0, 1], [1, 0, 0]]
    result = matrix_exponentiation(matrix, n - 2)
    return result[0][0] + result[0][1]

print(str(padovan_equation(20)))  # Prints the 20th term of the Padovan sequence using dynamic programming
print(str(padovan_matrix_exponentiation(20)))  # Prints the 20th term of the Padovan sequence using matrix exponentiation
