


# Function to compute even parity bit
def compute_even_parity(data):
    # Sum the data bits and take modulo 2.
    # If sum is odd, parity bit is 1 (to make total even); if even, parity bit is 0.
    return sum(data) % 2

# Original data bits (example)
data = [1, 0, 1, 0, 1, 1, 1, 0]

# Calculate the parity bit
parity_bit = compute_even_parity(data)

# Print the original data and computed parity
print("Original Data: ", data)
print("Computed Parity Bit (Even):", parity_bit)

# Transmitting data: append parity bit to the data array
transmitted_data = data + [parity_bit]
print("\nTransmitted Data (Data + Parity):", transmitted_data)

# Simulate an error: flip a bit in the transmitted data
# For example, flip the bit at index 3 (0-indexed)
error_index = 3
data_with_error = transmitted_data.copy()
data_with_error[error_index] = 1 - data_with_error[error_index]
print("\nData with an Error Introduced at index", error_index, ":",
data_with_error)
# At the receiver, perform the parity check.
# For even parity, the sum of all bits should be even.
if sum(data_with_error) % 2 == 0:
    print("\nNo error detected (Parity Check Passed)")
else:
    print("\nError detected (Parity Check Failed)")
