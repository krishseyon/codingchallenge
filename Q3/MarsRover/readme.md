This program simulates the movement of rovers on a plateau on Mars. Each rover is represented by its x and y coordinates and a direction (N, E, S, or W), and can be controlled by a string of instructions consisting of 'L', 'R', and 'M'.
'L' and 'R' instruct the rover to turn left or right by 90 degrees, respectively, without changing its position.
'M' instructs the rover to move forward one grid point in its current direction.

The program takes as input the upper-right coordinates of the plateau, followed by the position and instructions for each rover. The output for each rover is its final position and direction.

Usage
To run the program, simply execute the following command in the terminal: python main.py

You will be prompted to enter the upper-right coordinates of the plateau. Enter two integers separated by a space and press Enter.

You will then be prompted to enter the position and instructions for each rover. Enter four values separated by spaces: the x and y coordinates, the direction, and the instructions. Press Enter to submit the input for each rover.

When you are finished entering rover data, simply press Enter on a blank line to exit the program.


Sample Input and Output

Enter the upper-right coordinates of the plateau: 5 5
Enter the position and instructions for the rover (e.g. 1 2 N LMLMLM): 1 2 N LMLMLMLMM
13N
Enter the position and instructions for the rover (e.g. 1 2 N LMLMLM): 3 3 E MMRMMRMRRM
51E
Enter the position and instructions for the rover (e.g. 1 2 N LMLMLM): ABC
invalid input



Testing
Testing can be done by running test.py in this folder.
This test case checks if the move method of the Rover class works correctly by testing if the direction and position of the rover are correctly updated after executing a sequence of instructions.
