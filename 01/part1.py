input_file = open("input")

input_numbers_list = []

for line in input_file.readlines():
    input_number = int(line)
    input_numbers_list.append(input_number)


count = 0

for i in range(1, len(input_numbers_list)):
    if input_numbers_list[i] > input_numbers_list[i-1]:
        count += 1

print(f"{count} measurements are greater than its previous one!")
