from A2b_Base import *

#______DO NOT EDIT ABOVE THIS LINE____________#
#use deque functions to add and remove frontier entries
#______EDITING BELOW THIS LINE IS ALLOWED, ONLY EDIT THE INTERNAL IMPLEMENTATION OF THE FUNCTIONS ____________#

class AStarGraph(GraphProblem):
    #use this child class, Inherit from the GraphProblem class, in this class implement hueristic (h) function
    """h function is straight-line distance from a node's state to goal."""
    # in this case use the romania_map.locations attribute to compute h.
    def h(self, node):
        #YOUR CODE GOES HERE
        # node.state is the current node's state
        current_x, current_y = self.graph.locations[node.state]
        # use romania_map.locations to get the goal's coordinates
        goal_x, goal_y = self.graph.locations[self.goal]
        
        # This formula is used to calculate the distance between 2 points 
        return ((current_x - goal_x) ** 2 + (current_y - goal_y) ** 2) ** 0.5


def astar_search(problem, h=None):
    """A* search is best-first (you may use priority queue) graph search with f(n) = g(n)+h(n).
    You need to specify the h function when you call astar_search, (ALREADY ADDED in TEST CASE),
    The tests check through a call to solution() function which returns a list of expanded cities along the path"""

    # YOUR CODE GOES HERE
    if h is None: 
        h = problem.h

    # Similar to bfs and dfs we did earlier, we will use these steps to implemment A* search:=
    # Step 1: Create initial node
    # Step 2: Goal test
    # Step 3: Expand node
    # Step 4: Add to frontier
    # Step 5: Remove from frontier and repeat the process 
    
    # Unlike bfs/dfs, we will not do goal test at the beginning, we will do it after expanding the node ~ in the loop instead
    # The reason is that for bfs and dfs, we do not consider the cost of the path => goal at start -> no need to expand
    # But for A* search, sometimes even if the initial node is the goal, there might be a better path to the goal (loop back to the goal)
    node = Node(problem.initial)
    # Based on f(n) = g(n) + h(n)
    frontier = PriorityQueue('min', lambda n: n.path_cost + h(n.state))
    frontier.append(node)
    explored = set()
    
    while frontier:
        current_node = frontier.pop()
        if problem.goal_test(current_node.state):
            return current_node
        explored.add(current_node.state)
        
        for child in current_node.expand(problem):
            # Check if the node is already explored or in the frontier or not
            # if not explored and not in frontier -> add to frontier 
            if child.state not in explored and child not in frontier:
                frontier.append(child)
            # If the child already in the fr
            elif child in frontier:
                # check if the new path is better
                # Yes -> Update the path 
                if child.path_cost < frontier[child].path_cost:
                    frontier.remove(child)
                    frontier.append(child)
    
    return None 
