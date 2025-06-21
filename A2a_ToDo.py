# from A2a_Base import *
#
# #______DO NOT EDIT ABOVE THIS LINE____________#
#
# #use deque functions to add and remove frontier entries
#
#
# #______EDITING BELOW THIS LINE IS ALLOWED, ONLY EDIT THE INTERNAL IMPLEMENTATION OF THE FUNCTIONS ____________#
# def breadth_first_graph_search(problem):
#     """
#     Implement the breadth first search for the graph here.
#     some skeleton code is provided, feel free to edit it.
#     Search through the successors/actions of a problem to find a goal.
#     The initial frontier should be an empty queue.
#     Does not get trapped by loops.
#     If two paths reach a state, only use the first one.
#     """
#     node = Node(problem.initial)
#     if problem.goal_test(node.state):
#         return node
#     frontier = deque([node])
#     explored = set()
#     while frontier:
#         # YOUR CODE GOES HERE
#     return None
#
#
# def depth_first_graph_search(problem):
#     """
#     Search the deepest nodes in the search tree first.
#     Search through the successors/actions of a problem to find a goal.
#     The initial frontier should be an empty queue.
#     Does not get trapped by loops.
#     If two paths reach a state, only use the first one.
#     """
#     frontier = [(Node(problem.initial))]  # Stack
#     # YOUR CODE GOES HERE
#     return None
#
#
