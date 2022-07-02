
class Node:
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.h = 0
        self.g = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def heuristic(cell1, cell2):
    """Returns the Manhattan distance between two cells

    Args:
        cell1 (tuple): coordinates of the first node
        cell2 (tuple): coordinates of the second node

    Returns:
        int: Manhattan distance between cell1 and cell2
    """

    x1, y1 = cell1
    x2, y2 = cell2

    return abs(x2-x1) + abs(y2-y1)


def a_star(maze, start, end):
    """Returns shortest path between two points in the warehouse

    Args:
        maze (list of lists): Warehouse configuration
        start (Node): Starting node for the search
        end (_type_): Ending node for the search

    Returns:
        list: Shortest path from start to end//-1 for error case
    """

    start_node = Node(None, start)
    start_node.h = heuristic(start, end)
    start_node.g = 0
    start_node.f = start_node.h + start_node.g

    end_node = Node(None, end)
    end_node.h = 0

    # Open and close list
    # An array that contains the nodes that have been generated but have not been expanded yet.
    open_list = []
    close_list = []  # An array which contains the expanded nodes.

    open_list.append(start_node)

    # Loop
    while len(open_list) > 0:
        current_node = open_list[0]  # Not necessarily an ordered list
        current_index = 0

        for index, item in enumerate(open_list):  # n complexity
            if item.f < current_node.f:
                current_node = item  # Node class
                current_index = index

        # Pop eliminates the current node from the open list and then with append we add it to the close list
        open_list.pop(current_index)
        close_list.append(current_node)

        # Goal
        if current_node == end_node:
            path = []  # List with the path
            # It goes from last node to the start one going through parent nodes.
            while current_node is not None:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]

        # Generate Leaves
        leaves = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            # Get neighbour node position
            neighbour_position = (
                current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Guarantees neighbours inside the warehouse
            if neighbour_position[0] > (len(maze) - 1) or neighbour_position[0] < 0 or neighbour_position[1] > (len(maze[0]) - 1) or neighbour_position[1] < 0:
                continue
            # Guarantees we are not in a barrier
            if maze[neighbour_position[0]][neighbour_position[1]] != 0:
                continue
            new_node = Node(current_node, neighbour_position)
            inCloseList = False
            # for leave in leaves:
            for closed_leave in close_list:  # n complexity
                if new_node == closed_leave:
                    inCloseList = True

            if inCloseList:
                continue
            # New node

            leaves.append(new_node)

        # Loop for leaves
        for leave in leaves:

            # Heuristic, g() and f() values
            leave.g = current_node.g + 1
            leave.h = heuristic(leave.position, end_node.position)
            leave.f = leave.g + leave.h

            # Leave already in open list
            inOpenList = False
            for open_node in open_list:  # n complexity
                if leave == open_node:
                    inOpenList = True
            if inOpenList:
                continue
            open_list.append(leave)
    return -1
