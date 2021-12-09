
input_file = open("input")

input_numbers = []

for line in input_file.readlines():
    input_number = int(line)
    input_numbers.append(input_number)

length_input_numbers = len(input_numbers)
steps = 0
current_sum = 0
y = 0
current_sums = []

while y < length_input_numbers:
    current_sum += input_numbers[y]
    steps += 1
    if steps == 3:
        current_sums.append(current_sum)
        y -= 1
        steps = 0
        current_sum = 0
    else:
        y += 1

length_current_sums = len(current_sums)
amount_of_numbers_greater_than_prev = 0
for i in range(1, length_current_sums):
    if current_sums[i] > current_sums[i-1]:
        amount_of_numbers_greater_than_prev += 1

print(amount_of_numbers_greater_than_prev)

input_file.close()
