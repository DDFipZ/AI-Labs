class Node:  # Node has only PARENT_NODE, STATE, DEPTH
    def __init__(self, state, parent=None, depth=0, goal_dist = 0, heuristic = 0, traveled_dist = 0):
        self.STATE = state
        self.PARENT_NODE = parent
        self.DEPTH = depth
        self.GOAL_DIST = goal_dist
        self.TRAVELED_DIST = traveled_dist
        self.HEURISTIC = heuristic
        

    def path(self):  # Create a list of nodes from the root to this node.
        current_node = self
        path = [self]
        while current_node.PARENT_NODE:  # while current node has parent
            current_node = current_node.PARENT_NODE  # make parent the current node
            path.append(current_node)   # add current node to path
        return path

    def display(self):
        print(self)

    def __repr__(self):
        return 'State: ' + str(self.STATE) + ' - Heuristic: ' + str(self.HEURISTIC)


'''
Search the tree for the goal state and return path from initial state to goal state
'''
def TREE_SEARCH():
    fringe = []
    initial_node = Node(INITIAL_STATE) #Create Initial Node
    fringe = INSERT(initial_node, fringe) #Insert Initial Node
    while fringe is not None:
        node = REMOVE_FIRST(fringe) #Removes the node at fringe[0]
        if node.STATE == GOAL_STATE: #If the node is the destination node
            return node.path()
        children = EXPAND(node)
        fringe = INSERT_ALL(children, fringe)
        fringe = sorted(fringe, key=lambda node: node.HEURISTIC)
        print("fringe: {}".format(fringe))


'''
Expands node and gets the successors (children) of that node.
Return list of the successor nodes.
'''
def EXPAND(node):
    successors = []
    children = successor_fn(node.STATE)
    for child in children:
        s = Node(node)  # create node for each in state list
        s.STATE = child  # e.g. result = 'F' then 'G' from list ['F', 'G']
        s.PARENT_NODE = node
        s.DEPTH = node.DEPTH + 1
        s.GOAL_DIST = STATE_HEURISTIC[s.STATE]
        s.TRAVELED_DIST = s.PARENT_NODE.HEURISTIC + get_distance(s.PARENT_NODE.STATE, s.STATE)
        s.HEURISTIC = s.TRAVELED_DIST + s.GOAL_DIST
        successors = INSERT(s, successors)
    return sorted(successors, key=lambda node: node.HEURISTIC)


'''
Insert node in to the queue (fringe).
'''
def INSERT(node, queue):
    queue.append(node)
    return queue


'''
Insert list of nodes into the fringe
'''
def INSERT_ALL(list, queue):
    for n in list:
        queue.append(n)
    return queue


'''
Removes and returns the first element from fringe
'''
def REMOVE_FIRST(queue):
    f = queue[0]
    queue.pop(0)
    return f

'''
Successor function, mapping the nodes to its successors
'''
def successor_fn(state):  # Lookup list of successor states
    return STATE_SPACE[state]  # successor_fn( 'C' ) returns ['F', 'G']


#Gets Distance between points
def get_distance(state1, state2):
    return STATE_DISTANCE[(state1, state2)]



INITIAL_STATE = 'A'
GOAL_STATE = "L"
STATE_SPACE = { 'A': ['B', 'C', "D"],
                'B': ['F', 'E'],
                'C': ["E"],
                'D': ["H", "I", "J"],
                'E': ["G", "H"],
                'F': ["G"],
                'G': ["K"],
                'H': ["K", "L"], 
                'I': ["L"],
                "J": [],
                "K": []
                }


STATE_DISTANCE = {
                ("A", "B"): 1,
                ("A", "C"): 2,
                ("A", "D"): 4,
                ("B", "F"): 5,
                ("B", "E"): 4,
                ("C", "E"): 1,
                ("D", "H"): 1,
                ("D", "I"): 4,
                ("D", "J"): 2,
                ("F", "G"): 1,
                ("E", "G"): 2,
                ("E", "H"): 3,
                ("I", "L"): 3,
                ("G", "K"): 6,
                ("H", "K"): 6,
                ("H", "L"): 5

}


STATE_HEURISTIC = {
                "A": 6,
                "B": 5,
                "C": 5,
                "D": 2,
                "E": 4,
                "F": 5,
                "G": 4,
                "H": 1,
                "I": 2,
                "J": 1,
                "K": 0,
                "L": 0
}

'''
Run tree search and display the nodes in the path to goal node
'''
def run():
    path = TREE_SEARCH()
    print('Solution path:')
    for node in path:
        node.display()


if __name__ == '__main__':
    run()