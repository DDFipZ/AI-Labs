class Node:  # Node has only PARENT_NODE, STATE, DEPTH
    def __init__(self, state, cost, parent=None, depth=0):
        self.STATE = state
        self.PARENT_NODE = parent
        self.DEPTH = depth
        self.COST = cost

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
        return 'State: ' + str(self.STATE) + ' - Depth: ' + str(self.DEPTH)


'''
Search the tree for the goal state and return path from initial state to goal state
'''
def TREE_SEARCH():
    fringe = []
    initial_node = Node(INITIAL_STATE[0], INITIAL_STATE[1]) #Create Initial Node
    fringe = INSERT(initial_node, fringe) #Insert Initial Node
    while fringe is not None:
        node = REMOVE_FIRST(fringe) #Removes the node at fringe[0]
        if node.STATE == GOAL_STATE: #If the node is the destination node
            return node.path()
        children = EXPAND(node)
        fringe = INSERT_ALL(children, fringe)
        print("fringe: {}".format(fringe))


'''
Expands node and gets the successors (children) of that node.
Return list of the successor nodes.
'''
def EXPAND(node):
    successors = []
    children = successor_fn(node.STATE, node.COST)
    for child in children:
        s = Node(child[0], child[1])
        s.PARENT_NODE = node
        s.DEPTH = node.DEPTH + 1
        if successors:
            if successors[0].COST > s.COST:
                successors.clear()
        
        successors = INSERT(s, successors)
        # s = Node(node)  # create node for each in state list
        # s.STATE = child  # e.g. result = 'F' then 'G' from list ['F', 'G']
        # s.PARENT_NODE = node
        # s.DEPTH = node.DEPTH + 1
        
    return successors


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
def successor_fn(state, cost):  # Lookup list of successor states
    return STATE_SPACE[state, cost]  # successor_fn( 'C' ) returns ['F', 'G']


INITIAL_STATE = ("A", 6)
GOAL_STATE = "L"
STATE_SPACE = { 
                ("A", 6): [("B", 5), ("C", 5), ("D", 2)],
                ("B", 5): [("F", 5), ("E", 4)],
                ("F", 5): [("G", 4)],
                ("E", 4): [("G", 4), ("H", 1)],
                ("G", 4): [("K", 0)],
                ("H", 1): [("K", 0), ("L", 0)],
                ("K", 0): [],
                ("L", 0): [],
                ("C", 5): [("E", 4)],
                ("D", 2): [("I", 2), ("J", 1)],
                ("I", 2): [("L", 0)],
                ("J", 1): []

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