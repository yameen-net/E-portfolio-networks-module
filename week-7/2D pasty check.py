import numpy as np

def compute_parity(mat):
# Returns (row_parity, col_parity) for even parity
    return np.sum(mat, axis=1) % 2, np.sum(mat, axis=0) % 2
# Create a 4x4 data matrix
data = np.array([
[1, 0, 1, 1],
[0, 1, 0, 0],
[1, 1, 1, 0],
[0, 0, 1, 1]
])
print("Original Data:\n", data)
# Compute original parity bits
row_par, col_par = compute_parity(data)
print("Row Parity:", row_par)
print("Column Parity:", col_par)
# Introduce an error by flipping the bit at row 2, column 1 (0-indexed)