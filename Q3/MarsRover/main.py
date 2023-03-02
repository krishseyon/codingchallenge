class Rover:
    # Constructor to initialize rover position and direction
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    # Function to execute a given sequence of instructions
    def move(self, instruction, plateau):
        if instruction == 'L':
            self.turn_left()
        elif instruction == 'R':
            self.turn_right()
        elif instruction == 'M':
            self.move_forward(plateau)

    # Function to turn the rover left by 90 degrees
    def turn_left(self):
        if self.direction == 'N':
            self.direction = 'W'
        elif self.direction == 'W':
            self.direction = 'S'
        elif self.direction == 'S':
            self.direction = 'E'
        elif self.direction == 'E':
            self.direction = 'N'

    # Function to turn the rover right by 90 degrees
    def turn_right(self):
        if self.direction == 'N':
            self.direction = 'E'
        elif self.direction == 'E':
            self.direction = 'S'
        elif self.direction == 'S':
            self.direction = 'W'
        elif self.direction == 'W':
            self.direction = 'N'

    # Function to move the rover forward in its current direction
    def move_forward(self, plateau):
        if self.direction == 'N':
            if self.y < plateau[1]:
                self.y += 1
        elif self.direction == 'E':
            if self.x < plateau[0]:
                self.x += 1
        elif self.direction == 'S':
            if self.y > 0:
                self.y -= 1
        elif self.direction == 'W':
            if self.x > 0:
                self.x -= 1

    def __str__(self):
        return f"{self.x}{self.y}{self.direction}"


def main():
    try:
        plateau = input("Enter the upper-right coordinates of the plateau: ")
        plateau = [int(x) for x in plateau.split()]

        while True:
            position = input("Enter the position and instructions for the rover (e.g. 1 2 N LMLMLM): ")
            if position == "":
                break
            x, y, direction, instructions = position.split()
            rover = Rover(int(x), int(y), direction)
            for instruction in instructions:
                rover.move(instruction, plateau)
            print(rover)
    except:
        print("invalid input")


if __name__ == '__main__':
    main()
