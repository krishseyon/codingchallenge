Usage
To use this code, simply call the solve_train_problem() function, which will solve the problem by answering the following questions:

The distance of the route A-B-C
The distance of the route A-D
The distance of the route A-D-C
The distance of the route A-E-B-C-D
The distance of the route A-E-D
The number of trips starting at C and ending at C with a maximum of 3 stops
The number of trips starting at A and ending at C with exactly 4 stops
The length of the shortest route (in terms of distance to travel) from A to C
The output for each question will be displayed in the console.

Helper Functions
The calculate_distance() function calculates the distance of a given route in the graph. If the route is invalid, it will return "NO SUCH ROUTE".

The count_trips_with_max_stops() function counts the number of trips starting at a given node and ending at another node with a maximum number of stops.

The count_trips_with_exact_stops() function counts the number of trips starting at a given node and ending at another node with an exact number of stops.

The shortest_path() function calculates the length of the shortest route (in terms of distance to travel) from one node to another using Dijkstra's algorithm.

To use the code, simply run the solve() function. This will output the answers to the following questions:



Dependencies
This code does not have any external dependencies and only requires Python 3 to run.