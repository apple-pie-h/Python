def eliminate_odd_numbers(numbers):
    for n in range(len(numbers) - 1, -1, -1):  # Iterate backwards
        if numbers[n] % 2 != 0:
            del numbers[n]  # Delete odd numbers
            
    return numbers
