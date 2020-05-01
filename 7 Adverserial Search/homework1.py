import lab05.alpha_beta
def minmax_decision(state):

    def max_value(state):
        if is_terminal(state):
            return utility_of(state)
        v = -infinity
        for (a, s) in successors_of(state):
            v = max(v, min_value(s))
        print('V: ' + str(v))
        return v

    def min_value(state):
        if is_terminal(state):
            return utility_of(state)
        v = infinity
        for (a, s) in successors_of(state):
            v = min(v, max_value(s))
        return v

    infinity = float('inf')
    action, state = argmax(successors_of(state), lambda a: min_value(a[1]))
    return action


def is_terminal(state):
    """
    returns True if the state is either a win or a tie (board full)
    :param state: State of the checkerboard. Ex: [0; 1; 2; 3; X; 5; 6; 7; 8]
    :return:
    """
    isTerminal = True
    for x in state:
        if int(x) > 2:
            isTerminal = False
    return isTerminal


def utility_of(state):
    """
    returns +1 if winner is X (MAX player), -1 if winner is O (MIN player), or 0 otherwise
    :param state: State of the checkerboard. Ex: [0; 1; 2; 3; X; 5; 6; 7; 8]
    :return:
    """
    return 0


def successors_of(state):
    """
    returns a list of tuples (move, state) as shown in the exercise slides
    :param state: State of the checkerboard. Ex: [0; 1; 2; 3; X; 5; 6; 7; 8]
    :return:
    """
    list = []
    for x in range(0, len(state)):
        newstate = state.copy()
        y = newstate[x]
        if y > 2:
            z = y - 1
            newstate[x] = z
            newstate.append(1)
            list.append((x, newstate))
        if y > 3:
            newstate = state.copy()
            z = y - 2
            newstate[x] = z
            newstate.append(2)
            list.append((x, newstate))
        if y > 4:
            newstate = state.copy()
            z = y - 3
            newstate[x] = z
            newstate.append(3)
            list.append((x, newstate))
    return list


def display(state):
    print("-----")
    print(state)


def main():
    board = [15]
    while not is_terminal(board):
        if not is_terminal(board):
            display(board)
            board[int(input('Your move? '))] = 0
    display(board)


def argmax(iterable, func):
    return max(iterable, key=func)


if __name__ == '__main__':
    main()
