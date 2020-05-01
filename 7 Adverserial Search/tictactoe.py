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
    if state[0] == state[3] == state[6] and isinstance(state[0], str):
        return True
    elif state[1] == state[4] == state[7] and isinstance(state[1], str):
        return True
    elif state[2] == state[5] == state[8] and isinstance(state[2], str):
        return True
    elif state[0] == state[1] == state[2] and isinstance(state[0], str):
        return True
    elif state[3] == state[4] == state[5] and isinstance(state[3], str):
        return True
    elif state[6] == state[7] == state[8] and isinstance(state[6], str):
        return True
    elif state[0] == state[4] == state[8] and isinstance(state[0], str):
        return True
    elif state[2] == state[4] == state[6] and isinstance(state[2], str):
        return True
    else:
        bools = all(isinstance(element, str) for element in state) 
        return all(isinstance(element, str) for element in state)
    return False


def utility_of(state):
    """
    returns +1 if winner is X (MAX player), -1 if winner is O (MIN player), or 0 otherwise
    :param state: State of the checkerboard. Ex: [0; 1; 2; 3; X; 5; 6; 7; 8]
    :return:
    """
    if state[0] == state[3] == state[6] and isinstance(state[0], str):
        if state[0] == "X":
            return 1
        else:
            return -1
    elif state[1] == state[4] == state[7] and isinstance(state[1], str):
        if state[1] == "X":
            return 1
        else:
            return -1
    elif state[2] == state[5] == state[8] and isinstance(state[2], str):
        if state[2] == "X":
            return 1
        else:
            return -1
    elif state[0] == state[1] == state[2] and isinstance(state[0], str):
        if state[0] == "X":
            return 1
        else:
            return -1
    elif state[3] == state[4] == state[5] and isinstance(state[3], str):
        if state[3] == "X":
            return 1
        else:
            return -1
    elif state[6] == state[7] == state[8] and isinstance(state[6], str):
        if state[6] == "X":
            return 1
        else:
            return -1
    elif state[0] == state[4] == state[8] and isinstance(state[0], str):
        if state[0] == "X":
            return 1
        else:
            return -1
    elif state[2] == state[4] == state[6] and isinstance(state[2], str):
        if state[2] == "X":
            return 1
        else:
            return -1
    else:
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
        if isinstance(newstate[x], int):
            newstate[x] = "Z"
            list.append((x, newstate))
            print(list)
    return list


def display(state):
    print("-----")
    for c in [0, 3, 6]:
        print(state[c + 0], state[c + 1], state[c + 2])


def main():
    board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    while not is_terminal(board):
        board[minmax_decision(board)] = 'X'
        if not is_terminal(board):
            display(board)
            board[int(input('Your move? '))] = 'O'
    display(board)


def argmax(iterable, func):
    return max(iterable, key=func)


if __name__ == '__main__':
    main()
