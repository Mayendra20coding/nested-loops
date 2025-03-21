def decimal_to_binary(n):
    if n == 0:
        return "0"
    binary = ""
    while n > 0:
        remainder = n % 2
        binary = str(remainder) + binary
        n = n // 2
    return binary

# Get user input
decimal_number = int(input("Enter a decimal number: "))
print(f"Binary equivalent: {decimal_to_binary(decimal_number)}")