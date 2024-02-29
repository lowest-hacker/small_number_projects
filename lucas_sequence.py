def dynamic_lucas():
    memo = {}
    def lucas(n):
        if n in memo:
            return memo[n]
        elif n == 0:
            return 2
        elif n == 1:
            return 1
        else:
            memo[n] = lucas(n - 1) + lucas(n - 2)
            return memo[n]
    return lucas

lucas_equation = dynamic_lucas()

# Multiplies two matrices together and returns the result
def matrix_mult(matrixA, matrixB):
    # Get rows and cols
    rows = len(matrixA)
    cols = len(matrixA[0])
    # Initialize result matrix
    result = [[0, 0], [0, 0]]
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

# Utilizes matrix exponentiation to calculate the Lucas sequence in logarithmic time
def lucas_matrix_exponentiation(n):
    if n == 0:
        return 2
    if n == 1:
        return 1
    matrix = [[1, 1], [1, 0]]
    result = matrix_exponentiation(matrix, n - 1)
    return result[0][0]

print(str(lucas_equation(75)))
print(str(lucas_matrix_exponentiation(150)))
