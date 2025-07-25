
import copy
import random

intelligence = 0

def generator():
    global intelligence
    seed = random.randint(1, 30) ##Change the numbers to affect winrate
    intelligence = seed

X = "X"
O = "O"
EMPTY = None

signs = [X, O, EMPTY]

def initial_state(n):
    ini = [[EMPTY, EMPTY, EMPTY],
           [EMPTY, EMPTY, EMPTY],
           [EMPTY, EMPTY, EMPTY]]
    if n == 1:
        ini[random.randint(0, 2)][random.randint(0, 2)] = signs[0]
    return ini


def player(board):
    x_number = sum(board, []).count(X)
    o_number = sum(board, []).count(O)
    if x_number > o_number:
        c_player = O
    else:
        c_player = X
    return c_player


def actions(board):
    row_actions = []

    if not terminal(board)[0]:
        for x, row in enumerate(board):
            action = [(x, i) for i in range(len(row)) if row[i] == EMPTY]
            row_actions.append(action)

    actions_set = sum(row_actions, [])
    return actions_set

def result(board, action):
    b_state = copy.deepcopy(board)
    b_state[action[0]][action[1]] = player(b_state)

    return b_state


def winner(board):
    winner_s = None
    if terminal(board)[0]:
        winner_s = signs[terminal(board)[1]]

    return winner_s


def terminal(board):

    g_over = False

    wins = [[0, 0, 0], [1, 1, 1], [2, 2, 2], [0, 1, 2], [2, 1, 0]]


    def boardindex(sign):
        indi_board = []
        for row in board:
            if sign is not EMPTY:
                layout = ([i for i, x in enumerate(board[board.index(row)]) if x == sign])
                indi_board.append(layout)
        return indi_board

    x_board = boardindex(signs[0])
    o_board = boardindex(signs[1])

    def endgame(layout):
        counter = 0

        for i in range(len(wins)):

            for a in range(len(layout)):

                if len(layout[a]) == len(layout):
                    g_over = True
                    return g_over

                else:

                    for z in layout[a]:
                        if wins[i][a] == layout[a][layout[a].index(z)]:
                            counter += 1
                            if counter == len(layout):
                                g_over = True
                                return g_over
                            break

            counter = 0

    x_end = endgame(x_board)
    o_end = endgame(o_board)

    winner_ = 2

    if x_end:
        g_over = True
        winner_ = 0

    elif o_end:
        g_over = True
        winner_ = 1

    elif sum(board, []).count(EMPTY) == 0:
        g_over = True
        return g_over, winner_

    return g_over, winner_


def utility(board):
    v_map = [1, 0, -1]
    val = winner(board)
    if terminal(board)[0]:
        if val == X:
            return v_map[0]
        if val == O:
            return v_map[2]
        else:
            return v_map[1]

def minimax(board):
    print("difficulty: ", intelligence)
    b_state = copy.deepcopy(board)

    def maxvalue(b_state, depth=0):
        if depth < intelligence:
            if terminal(b_state)[0]:
                return utility(b_state)
            v = float('-inf')
            for action in actions(b_state):
                v = max(v, minvalue(result(b_state, action), depth+1))
                #print("depth", depth, v)
        else:
            v = float('-inf')
            for action in actions(b_state):
                v = max(v, minvalue(result(b_state, action), depth))
                #print("elseVdepth", depth, v)
        return v

    def minvalue(b_state, depth=0):
        if depth < intelligence:
            if terminal(b_state)[0]:
                return utility(b_state)
            v = float('inf')
            for action in actions(b_state):
                v = min(v, maxvalue(result(b_state, action), depth+1))
                #print("depth", depth, v)
        else:
            v = float('inf')
            for action in actions(b_state):
                v = min(v, maxvalue(result(b_state, action), depth))
                #print("elseVdepth", depth, v)
        return v


    def maxi(b_state):
        minactions = []
        coords = []
        for action in actions(b_state):
            minactions.append(minvalue(result(b_state, action)))
            coords.append(action)
        maximum = max(minactions)
        indices = [i for i, v in enumerate(minactions) if v == maximum]
        return coords[random.choice(indices)]

    def mini(b_state):
        maxactions = []
        coords = []
        for action in actions(b_state):
            maxactions.append(maxvalue(result(b_state, action)))
            coords.append(action)
        minimum = min(maxactions)
        indices = [i for i, v in enumerate(maxactions) if v == minimum]
        return coords[random.choice(indices)]

    if player(board) == X:
        if sum(board, []).count(EMPTY) == 9:
            return random.choice(actions(b_state))
        else:
            return maxi(b_state)
    elif player(board) == O:
        return mini(b_state)







