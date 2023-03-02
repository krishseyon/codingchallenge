# Define the directed graph as a dictionary
graph = {'A': {'B': 5, 'D': 5, 'E': 7},
         'B': {'C': 4},
         'C': {'D': 8, 'E': 2},
         'D': {'C': 8, 'E': 6},
         'E': {'B': 3}}


# Helper function to calculate the distance of a given route
def calculate_distance(route):
    distance = 0
    for i in range(len(route) - 1):
        if route[i + 1] not in graph[route[i]]:
            return 'NO SUCH ROUTE'
        distance += graph[route[i]][route[i + 1]]
    return distance


# Function to solve the Train problem
def solve():
    # a. The distance of the route A-B-C
    print(f"Output #1: {calculate_distance(['A', 'B', 'C'])}")

    # b. The distance of the route A-D
    print(f"Output #2: {calculate_distance(['A', 'D'])}")

    # c. The distance of the route A-D-C
    print(f"Output #3: {calculate_distance(['A', 'D', 'C'])}")

    # d. The distance of the route A-E-B-C-D
    print(f"Output #4: {calculate_distance(['A', 'E', 'B', 'C', 'D'])}")

    # e. The distance of the route A-E-D
    print(f"Output #5: {calculate_distance(['A', 'E', 'D'])}")

    # f. The number of trips starting at C and ending at C with a maximum of 3 stops
    def count_trips_with_max_stops(start, end, max_stops, current_stops=0):
        if current_stops > max_stops:
            return 0
        if current_stops > 0 and start == end:
            return 1
        count = 0
        for neighbor in graph[start]:
            count += count_trips_with_max_stops(neighbor, end, max_stops, current_stops + 1)
        return count

    print(f"Output #6: {count_trips_with_max_stops('C', 'C', 3)}")

    # g. The number of trips starting at A and ending at C with exactly 4 stops
    def count_trips_with_exact_stops(start, end, exact_stops, current_stops=0):
        if current_stops == exact_stops and start == end:
            return 1
        if current_stops < exact_stops:
            count = 0
            for neighbor in graph[start]:
                count += count_trips_with_exact_stops(neighbor, end, exact_stops, current_stops + 1)
            return count
        return 0

    print(f"Output #7: {count_trips_with_exact_stops('A', 'C', 4)}")

    # h. The length of the shortest route (in terms of distance to travel) from A to C
    import heapq

    def shortest_path(start, end):
        distances = {vertex: float('inf') for vertex in graph}
        distances[start] = 0
        pq = [(0, start)]
        while pq:
            current_distance, current_vertex = heapq.heappop(pq)
            if current_distance > distances[current_vertex]:
                continue
            for neighbor, weight in graph[current_vertex].items():
                distance = current_distance + weight

solve()



