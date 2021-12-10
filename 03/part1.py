# we need the power consumption
# we get it by multiplying the gamma rate and the epsilon rate

class PowerConsumption():
    def __init__(self):
        self.input_file = open('input')
        self.report = self.input_file.read().strip().split('\n')
        self.lines = len(self.report)

        # chars per line is the length of one line
        self.chars_per_line = len(self.report[0])

        self.ones = 0
        self.zeros = 0

        self.most_common_bits = []  # for gamma rate
        self.least_common_bits = []  # for epsilon rate

    def get_most_common_bit(self):
        if self.ones > self.zeros:
            return 1
        elif self.zeros > self.ones:
            return 0

    def get_least_common_bit(self):
        if self.ones > self.zeros:
            return 0
        elif self.zeros > self.ones:
            return 1

    def reset_ones_zeros(self):
        self.ones = 0
        self.zeros = 0

    def convert_from_binary_to_int(self, input):
        return int(input, 2)

    def part1(self):
        most_common_bit = 0
        least_common_bit = 0
        for i in range(self.chars_per_line):  # go through each character of the line
            for j in range(self.lines):  # go through each line
                if int(self.report[j][i]) == 0:
                    self.zeros += 1
                elif int(self.report[j][i]) == 1:
                    self.ones += 1

            most_common_bit = self.get_most_common_bit()
            least_common_bit = self.get_least_common_bit()

            self.most_common_bits.append(most_common_bit)
            self.least_common_bits.append(least_common_bit)
            self.reset_ones_zeros()

        binary_string_gamma = ""
        for bit in self.most_common_bits:
            binary_string_gamma += str(bit)

        binary_string_epsilon = ""
        for bit in self.least_common_bits:
            binary_string_epsilon += str(bit)

        converted_number_gamma = self.convert_from_binary_to_int(
            binary_string_gamma)
        print(f"gamma: {converted_number_gamma}")

        converted_number_epsilon = self.convert_from_binary_to_int(
            binary_string_epsilon)
        print(f"epsilon: {converted_number_epsilon}")

        power_consumption = converted_number_gamma * converted_number_epsilon

        print(f"power_consumption: {power_consumption}")


ps = PowerConsumption()
ps.part1()
