

class Dive():
    def __init__(self):
        self.horizontal_position = 0
        self.depth = 0
        self.file = open("input")

    def forward(self, units):
        self.horizontal_position += units

    def down(self, units):
        self.depth += units

    def up(self, units):
        self.depth -= units

    def get_pos_and_depth(self):
        for line in self.file.readlines():
            line_split = line.split(" ")
            command = line_split[0]
            units = int(line_split[1])
            if command == "forward":
                self.forward(units)
            elif command == "down":
                self.down(units)
            elif command == "up":
                self.up(units)
        self.file.close()
        return self.horizontal_position, self.depth


dive = Dive()
pos_and_depth = dive.get_pos_and_depth()
result = pos_and_depth[0] * pos_and_depth[1]
print(pos_and_depth)
print(result)
