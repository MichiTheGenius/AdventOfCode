
sample_file = open('sample')

first_line = sample_file.readline().replace('\n', '')


first_line_split = first_line.split('->')

x1y1_str = first_line_split[0].strip().split(',')
x2y2_str = first_line_split[1].strip().split(',')

x1y1_int = [int(i) for i in x1y1_str]
x2y2_int = [int(i) for i in x2y2_str]

x1 = x1y1_int[0]
y1 = x1y1_int[1]

x2 = x2y2_int[0]
y2 = x2y2_int[1]
print(first_line)
print('----------------------')
print(first_line_split)
print('----------------------')
print(x1y1_int)
print('----------------------')
print(x2y2_int)
print('----------------------')

x_list = []
y_list = []
for x in range(x1, x2+1):
    x_list.append(x)
    print(x)

print('----------------------')

for y in range(y1, y2 + 1):
    y_list.append(y)
    print(y)

for x in range(len(x_list)):
    for y in range(len(y_list)):
        print(f"range: {x_list[x]} -> {y_list[y]}")
