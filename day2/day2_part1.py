# Open the file in read mode and process it
with open("data.txt", "r") as file:
    # Read all lines from the file
    lines = file.readlines()

nbrOfTrue = 0

# Function to check if a list of numbers is either strictly increasing or strictly decreasing
def is_increasing_or_decreasing(numbers):
    increasing = all(numbers[i] < numbers[i + 1] for i in range(len(numbers) - 1))
    decreasing = all(numbers[i] > numbers[i + 1] for i in range(len(numbers) - 1))
    valid_difference = all(1 <= abs(numbers[i] - numbers[i + 1]) <= 3 for i in range(len(numbers) - 1))
    return (increasing or decreasing) and valid_difference



# Process the lines
for line in lines:
    # Split the line into a list of integers
    numbers = list(map(int, line.split()))
    # Check if the numbers are increasing or decreasing
    if is_increasing_or_decreasing(numbers):
        nbrOfTrue += 1
        print(f"Safe: {numbers}")


print(f"Number of safe rows: {nbrOfTrue}")
