with open('drawing_numbers') as f:
    drawing_numbers = f.read().split(',')
# print(drawing_numbers)

with open('board') as f:
    lines = f.read().split('\n')
    numbers = []
    for line in lines:
        numbers.append(line.split(' '))

    for row in range(len(numbers)):
        for column in range(len(numbers[0])):
            numbers[row][column] = int(numbers[row][column])


def is_number_in_row(arr, column, check):
    for row in range(5):
        if arr[row][column] == check:
            return True
    return False


def is_number_in_column(arr, row, check):
    for column in range(5):
        if arr[row][column] == check:
            return True
    return False


print(is_number_in_row(numbers, 0, 65))
print(is_number_in_column(numbers, 0, 27))

print(numbers)
