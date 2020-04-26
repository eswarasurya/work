from copy import deepcopy
import pygame

pygame.init()


class Problem:  # Tic Tac Toe
    def __init__(self, state):
        self.initial_state = state

    def Player(self, state):
        if state.count(1) > state.count(2):
            return 2
        return 1

    def Actions(self, state):
        l = []
        if state.count(1) > state.count(2):
            for i in range(0, len(state)):
                if state[i] == 0:
                    l.append([i, 2])
        else:
            for i in range(0, len(state)):
                if state[i] == 0:
                    l.append([i, 1])
        return l

    def Result(self, state, action):
        state[action[0]] = action[1]
        return state

    def Termainal_Test(self, state):
        for i in range(0, len(state)):
            if state[i] == 0:
                return False
        return True

    def Utility(self, state, player):
        temp = 0
        if state[0] == state[1] == state[2] == player or state[3] == state[4] == state[5] == player or state[6] == \
                state[7] == state[8] == player:
            temp = 1  # Horizontal Lines
        elif state[0] == state[3] == state[6] == player or state[1] == state[4] == state[7] == player or state[2] == \
                state[5] == state[8] == player:
            temp = 1  # Vertical Lines
        elif state[0] == state[4] == state[8] == player or state[2] == state[4] == state[6] == player:
            temp = 1  # Diagonals
        if state[0] == state[1] == state[2] == 2 or state[3] == state[4] == state[5] == 2 or state[6] == \
                state[7] == state[8] == 2:
            temp = -1  # Horizontal Lines
        elif state[0] == state[3] == state[6] == 2 or state[1] == state[4] == state[7] == 2 or state[2] == \
                state[5] == state[8] == 2:
            temp = -1  # Vertical Lines
        elif state[0] == state[4] == state[8] == 2 or state[2] == state[4] == state[6] == 2:
            temp = -1  # Diagonals
        elif is_empty(state):
            temp = 0
        return temp

    def hurestic(self, state):
        sum = 0
        if state[0] == state[1] == state[2] == 1 or state[3] == state[4] == state[5] == 1 or state[6] == state[7] == \
                state[8] == 1:
            sum += 100
        elif state[0] == state[3] == state[6] == 1 or state[1] == state[4] == state[7] == 1 or state[2] == state[5] == \
                state[8] == 1:
            sum += 100  # Vertical Lines
        elif state[0] == state[4] == state[8] == 1 or state[2] == state[4] == state[6] == 1:
            sum += 100  # Diagonals

        if state[0] == state[1] == state[2] == 2 or state[3] == state[4] == state[5] == 2 or state[6] == state[7] == \
                state[8] == 2:
            sum -= 99
        elif state[0] == state[3] == state[6] == 2 or state[1] == state[4] == state[7] == 2 or state[2] == state[5] == \
                state[8] == 2:
            sum -= 99  # Vertical Lines
        elif state[0] == state[4] == state[8] == 2 or state[2] == state[4] == state[6] == 2:
            sum -= 99  # Diagonals

        for i in range(0, 7, 3):  # for Horizantal
            if state[i] != 2 and state[i + 1] != 2 and state[i + 2] != 2:
                if state[i] == state[i + 1] == 1 or state[i] == state[i + 2] == 1 or state[i + 1] == state[i + 2] == 1:
                    sum += 10

        for i in range(0, 3):  # for Vertical
            if state[i] != 2 and state[i + 3] != 2 and state[i + 6] != 2:
                if state[i] == state[i + 3] == 1 or state[i] == state[i + 6] == 1 or state[i + 3] == state[i + 6] == 1:
                    sum += 10

        if state[0] != 2 and state[4] != 2 and state[8] != 2:  # for Diagonals
            if state[0] == state[4] == 1 or state[4] == state[8] == 1 or state[0] == state[8] == 1:
                sum += 10
        if state[2] != 2 and state[4] != 2 and state[6] != 2:
            if state[2] == state[4] == 1 or state[4] == state[6] == 1 or state[2] == state[6] == 1:
                sum += 10

        for i in range(0, 7, 3):  # for Horizantal
            if state[i] != 1 and state[i + 1] != 1 and state[i + 2] != 1:
                if state[i] == state[i + 1] == 2 or state[i] == state[i + 2] == 2 or state[i + 1] == state[i + 2] == 2:
                    sum -= 9

        for i in range(0, 3):  # for Vertical
            if state[i] != 1 and state[i + 3] != 1 and state[i + 6] != 1:
                if state[i] == state[i + 3] == 2 or state[i] == state[i + 6] == 2 or state[i + 3] == state[i + 6] == 2:
                    sum -= 9

        if state[0] != 1 and state[4] != 1 and state[8] != 1:  # for Diagonals
            if state[0] == state[4] == 2 or state[4] == state[8] == 2 or state[0] == state[8] == 2:
                sum -= 9
        if state[2] != 1 and state[4] != 1 and state[6] != 1:
            if state[2] == state[4] == 2 or state[4] == state[6] == 2 or state[2] == state[6] == 2:
                sum -= 9

        for x in state:
            if x == 1:
                sum += 1
            elif x == 2:
                sum -= 0.5
        return sum


class Problem1:  # Open Field Tic Tac Toe
    def __init__(self, state, grid_size, win_number):
        self.initial_state = state
        self.n = grid_size
        self.win_number = win_number

    def Player(self, state):
        if state.count(1) > state.count(2):
            return 2
        return 1

    def Actions(self, state):
        l = []
        if state.count(1) > state.count(2):
            for i in range(0, len(state)):
                if state[i] == 0:
                    l.append([i, 2])
        else:
            for i in range(0, len(state)):
                if state[i] == 0:
                    l.append([i, 1])
        return l

    def Result(self, state, action):
        state[action[0]] = action[1]
        return state

    def Termainal_Test(self, state):
        for i in range(0, len(state)):
            if state[i] == 0:
                return False
        return True

    def Utility(self, state, player):
        init_temp = 0
        temp = 0
        if player == 1:
            counter_player = 2
        else:
            counter_player = 1
        size = self.n
        win = self.win_number
        for k in range(0, size):  # For Horizontal
            for i in range(size * k, size * k + size - win + 1):
                temp_l = []
                for j in range(i, i + win):
                    temp_l.append(state[j])
                if temp_l.count(player) == win:
                    temp = 1

        for i in range(0, (size - win + 1) * size):  # For Vertical
            temp_l = []
            for j in range(0, win):
                temp_l.append(state[i + j * size])
            if temp_l.count(player) == win:
                temp = 1

        for z in range(0, size - win + 1):
            l = []  # For Diagonal
            for i in range(0, size):
                for j in range(0, size):
                    if i == j - z:
                        l.append(state[size * i + j])
            for i in range(0, len(l) - win + 1):
                temp_l = []
                for j in range(i, i + win):
                    temp_l.append(l[j])
                if temp_l.count(player) == win:
                    temp = 1

        for z in range(1, size - win + 1):
            l = []  # For Diagonal
            for i in range(0, size):
                for j in range(0, size):
                    if i == j + z:
                        l.append(state[size * i + j])
            for i in range(0, len(l) - win + 1):
                temp_l = []
                for j in range(i, i + win):
                    temp_l.append(l[j])
                if temp_l.count(player) == win:
                    temp = 1

        for z in range(0, size - win + 1):
            l = []  # For Counter Diagonal
            for i in range(0, size):
                for j in range(0, size):
                    if i + j == size - 1 - z:
                        l.append(state[size * i + j])
            for i in range(0, len(l) - win + 1):
                temp_l = []
                for j in range(i, i + win):
                    temp_l.append(l[j])
                if temp_l.count(player) == win:
                    temp = 1

        for z in range(1, size - win + 1):
            l = []  # For Counter Diagonal
            for i in range(0, size):
                for j in range(0, size):
                    if i + j == size - 1 + z:
                        l.append(state[size * i + j])
            for i in range(0, len(l) - win + 1):
                temp_l = []
                for j in range(i, i + win):
                    temp_l.append(l[j])
                if temp_l.count(player) == win:
                    temp = 1

        # for Counter player

        for k in range(0, size):  # For Horizontal
            for i in range(size * k, size * k + size - win + 1):
                temp_l = []
                for j in range(i, i + win):
                    temp_l.append(state[j])
                if temp_l.count(counter_player) == win:
                    temp = -1

        for i in range(0, (size - win + 1) * size):  # For Vertical
            temp_l = []
            for j in range(0, win):
                temp_l.append(state[i + j * size])
            if temp_l.count(counter_player) == win:
                temp = -1

        for z in range(0, size - win + 1):
            l = []  # For Diagonal
            for i in range(0, size):
                for j in range(0, size):
                    if i == j - z:
                        l.append(state[size * i + j])
            for i in range(0, len(l) - win + 1):
                temp_l = []
                for j in range(i, i + win):
                    temp_l.append(l[j])
                if temp_l.count(counter_player) == win:
                    temp = -1

        for z in range(1, size - win + 1):
            l = []  # For Diagonal
            for i in range(0, size):
                for j in range(0, size):
                    if i == j + z:
                        l.append(state[size * i + j])
            for i in range(0, len(l) - win + 1):
                temp_l = []
                for j in range(i, i + win):
                    temp_l.append(l[j])
                if temp_l.count(counter_player) == win:
                    temp = -1

        for z in range(0, size - win + 1):
            l = []  # For Counter Diagonal
            for i in range(0, size):
                for j in range(0, size):
                    if i + j == size - 1 - z:
                        l.append(state[size * i + j])
            for i in range(0, len(l) - win + 1):
                temp_l = []
                for j in range(i, i + win):
                    temp_l.append(l[j])
                if temp_l.count(counter_player) == win:
                    temp = -1

        for z in range(1, size - win + 1):
            l = []  # For Counter Diagonal
            for i in range(0, size):
                for j in range(0, size):
                    if i + j == size - 1 + z:
                        l.append(state[size * i + j])
            for i in range(0, len(l) - win + 1):
                temp_l = []
                for j in range(i, i + win):
                    temp_l.append(l[j])
                if temp_l.count(counter_player) == win:
                    temp = -1

        if is_empty(state) and temp == 0:
            temp = 0
        return temp

    def hurestic(self, state):
        sum = 0
        size = self.n
        win = self.win_number
        for k in range(0, size):  # For Horizontal
            for i in range(size * k, size * k + size - win + 1):
                temp_l = []
                for j in range(i, i + win):
                    temp_l.append(state[j])
                sum += sum_compute(temp_l, win)

        for i in range(0, (size - win + 1) * size):  # For Vertical
            temp_l = []
            for j in range(0, win):
                temp_l.append(state[i + j * size])
            sum += sum_compute(temp_l, win)

        for z in range(0, size - win + 1):
            l = []  # For Diagonal
            for i in range(0, size):
                for j in range(0, size):
                    if i == j - z:
                        l.append(state[size * i + j])
            for i in range(0, len(l) - win + 1):
                temp_l = []
                for j in range(i, i + win):
                    temp_l.append(l[j])
                sum += sum_compute(temp_l, win)

        for z in range(1, size - win + 1):
            l = []  # For Diagonal
            for i in range(0, size):
                for j in range(0, size):
                    if i == j + z:
                        l.append(state[size * i + j])
            for i in range(0, len(l) - win + 1):
                temp_l = []
                for j in range(i, i + win):
                    temp_l.append(l[j])
                sum += sum_compute(temp_l, win)

        for z in range(0, size - win + 1):
            l = []  # For Counter Diagonal
            for i in range(0, size):
                for j in range(0, size):
                    if i + j == size - 1 - z:
                        l.append(state[size * i + j])
            for i in range(0, len(l) - win + 1):
                temp_l = []
                for j in range(i, i + win):
                    temp_l.append(l[j])
                sum += sum_compute(temp_l, win)

        for z in range(1, size - win + 1):
            l = []  # For Counter Diagonal
            for i in range(0, size):
                for j in range(0, size):
                    if i + j == size - 1 + z:
                        l.append(state[size * i + j])
            for i in range(0, len(l) - win + 1):
                temp_l = []
                for j in range(i, i + win):
                    temp_l.append(l[j])
                sum += sum_compute(temp_l, win)
        return sum


def sum_compute(state, win):  # Computes hurestic value of a given state
    max_score = 100
    sum = 0
    for i in range(0, win):
        if state.count(1) == win - i and state.count(2) == 0:
            sum += max_score / (4 * i + 1)

        if state.count(2) == win - i and state.count(1) == 0:
            sum -= max_score / (4 * i + 1) - 1
    return sum


def create_problem_list(size):  # Returns the initial state list for a given size
    l = []
    for i in range(0, size * size):
        l.append(0)
    return l


color = (0, 212, 50)
color_circle = (234, 98, 10)
color_cross = (124, 28, 174)
color1 = (250, 235, 214)
font = pygame.font.SysFont("Times new Roman", 68)
font1 = pygame.font.SysFont("Times new Roman", 40)
font2 = pygame.font.SysFont("Times new Roman", 25)
font3 = pygame.font.SysFont("Times new Roman", 40)
font4 = pygame.font.SysFont("Times new Roman", 20)

# Render the text in new surface
text = font.render("TIC TAC TOE", True, (158, 16, 16))
text_a = font1.render("Select Option", True, (44, 175, 238))
text1 = font1.render("Tic Tac Toe", True, color)
text2 = font2.render("Open field Tic Tac Toe", True, color)
text3 = font3.render("Select Option", True, (158, 16, 16))
text4 = font1.render("Basic Min Max", True, color)
text4_a = font4.render("(Works Slow)", True, color)
text5 = font2.render("Min Max with α β pruning", True, color)
text6 = font2.render("Min Max with Depth Limit", True, color)
text7 = font2.render("Min Max with DL and α,β", True, color)
text8 = font2.render("Experimental Min Max", True, color)
text9 = font2.render("Grid Size(x)", True, (36, 11, 207))
text9_a = font2.render("No. of connecting pieces to win(y)", True, (36, 11, 207))
text10 = font2.render("x = 3, y = 3", True, color)
text11 = font2.render("x = 4, y = 3", True, color)
text12 = font2.render("x = 4, y = 4", True, color)
text13 = font2.render("x = 5, y = 3", True, color)
text14 = font2.render("x = 5, y = 4", True, color)
text15 = font2.render("x = 5, y = 5", True, color)
text16 = font2.render("x = 6, y = 3", True, color)
text17 = font2.render("x = 6, y = 4", True, color)
text18 = font2.render("x = 6, y = 5", True, color)
text19 = font2.render("x = 6, y = 6", True, color)
text20 = font2.render("x = 7, y = 7", True, color)
text21 = font2.render("x = 7, y = 4", True, color)


def check(screen, x1, x2, y1, y2):  # Shows a rectangle background on hovering
    position = pygame.mouse.get_pos()
    if x1 <= position[0] <= x2 and y1 <= position[1] <= y2:
        pygame.draw.polygon(screen, color1, [(x1, y1), (x2, y1), (x2, y2), (x1, y2)])


def visuz():  # Asks weather Tic Tac Toe or open field Tic Tac Toe
    done = True
    screen = pygame.display.set_mode((500, 500))
    while done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = False
            position = pygame.mouse.get_pos()
            if 100 <= position[0] <= 400 and 300 <= position[1] <= 350 and pygame.mouse.get_pressed()[0] == 1:
                return 1
            if 100 <= position[0] <= 400 and 375 <= position[1] <= 415 and pygame.mouse.get_pressed()[0] == 1:
                return 2

        screen.fill((255, 255, 255))
        screen.blit(text, (50, 100))
        screen.blit(text_a, (115, 250))
        screen.blit(text1, (130, 300))
        check(screen, 100, 400, 300, 350)
        screen.blit(text1, (130, 300))

        screen.blit(text2, (130, 375))
        check(screen, 100, 400, 375, 415)
        screen.blit(text2, (130, 375))
        pygame.display.flip()


def get_method():  # Visualization for method to be selected
    done = True
    screen = pygame.display.set_mode((500, 500))
    while done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = False
                # pygame.display.quit()
            position = pygame.mouse.get_pos()
            if 100 <= position[0] <= 400 and 200 <= position[1] <= 250 and pygame.mouse.get_pressed()[0] == 1:
                print('Minimax_Decision')
                return 'Minimax_Decision'
                # done = False
            elif 100 <= position[0] <= 400 and 260 <= position[1] <= 310 and pygame.mouse.get_pressed()[0] == 1:
                print('ab_pruning')
                return 'ab_pruning'
                # done = False
            elif 100 <= position[0] <= 400 and 320 <= position[1] <= 370 and pygame.mouse.get_pressed()[0] == 1:
                print('DLS')
                return 'DLS'
                # done = False
            elif 100 <= position[0] <= 400 and 380 <= position[1] <= 430 and pygame.mouse.get_pressed()[0] == 1:
                print('abDLS')
                return 'abDLS'
                # done = False
            elif 100 <= position[0] <= 400 and 440 <= position[1] <= 490 and pygame.mouse.get_pressed()[0] == 1:
                print('experment')
                return 'experment'
                # done = False
        screen.fill((255, 255, 255))
        screen.blit(text3, (100, 50))
        screen.blit(text4, (120, 200))
        screen.blit(text4_a, (370, 220))
        check(screen, 100, 400, 200, 250)
        screen.blit(text4_a, (370, 220))
        screen.blit(text4, (120, 200))

        screen.blit(text5, (120, 270))
        screen.blit(text4_a, (390, 280))
        check(screen, 100, 400, 260, 310)
        screen.blit(text5, (120, 270))
        screen.blit(text4_a, (390, 280))

        screen.blit(text6, (120, 320))
        check(screen, 100, 400, 320, 370)
        screen.blit(text6, (120, 320))

        screen.blit(text7, (120, 390))
        check(screen, 100, 400, 380, 430)
        screen.blit(text7, (120, 390))

        screen.blit(text8, (120, 450))
        check(screen, 100, 400, 440, 490)
        screen.blit(text8, (120, 450))
        pygame.display.flip()


def get_size():  # To choose the grid size and the number of bits for consecutive win
    done = True
    screen = pygame.display.set_mode((500, 500))
    while done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = False
            position = pygame.mouse.get_pos()
            if 50 <= position[0] <= 200 and 200 <= position[1] <= 250 and pygame.mouse.get_pressed()[0] == 1:
                return 3, 3
            elif 50 <= position[0] <= 200 and 260 <= position[1] <= 310 and pygame.mouse.get_pressed()[0] == 1:
                return 4, 3
            elif 50 <= position[0] <= 200 and 320 <= position[1] <= 370 and pygame.mouse.get_pressed()[0] == 1:
                return 4, 4
            elif 50 <= position[0] <= 200 and 380 <= position[1] <= 430 and pygame.mouse.get_pressed()[0] == 1:
                return 5, 3
            elif 50 <= position[0] <= 200 and 440 <= position[1] <= 490 and pygame.mouse.get_pressed()[0] == 1:
                return 5, 4
            elif 250 <= position[0] <= 400 and 200 <= position[1] <= 250 and pygame.mouse.get_pressed()[0] == 1:
                return 5, 5
            elif 250 <= position[0] <= 400 and 260 <= position[1] <= 310 and pygame.mouse.get_pressed()[0] == 1:
                return 6, 3
            elif 250 <= position[0] <= 400 and 320 <= position[1] <= 370 and pygame.mouse.get_pressed()[0] == 1:
                return 6, 4
            elif 250 <= position[0] <= 400 and 380 <= position[1] <= 430 and pygame.mouse.get_pressed()[0] == 1:
                return 6, 5
            elif 250 <= position[0] <= 400 and 440 <= position[1] <= 490 and pygame.mouse.get_pressed()[0] == 1:
                return 6, 6
        screen.fill((255, 255, 255))
        screen.blit(text9, (100, 20))
        screen.blit(text9_a, (70, 70))
        screen.blit(text_a, (80, 150))
        screen.blit(text10, (60, 200))
        check(screen, 50, 200, 200, 250)
        screen.blit(text10, (60, 200))

        screen.blit(text11, (60, 260))
        check(screen, 50, 200, 260, 310)
        screen.blit(text11, (60, 260))

        screen.blit(text12, (60, 320))
        check(screen, 50, 200, 320, 370)
        screen.blit(text12, (60, 320))

        screen.blit(text13, (60, 380))
        check(screen, 50, 200, 380, 430)
        screen.blit(text13, (60, 380))

        screen.blit(text14, (60, 440))
        check(screen, 50, 200, 440, 490)
        screen.blit(text14, (60, 440))

        screen.blit(text15, (260, 200))
        check(screen, 250, 400, 200, 250)
        screen.blit(text15, (260, 200))

        screen.blit(text16, (260, 260))
        check(screen, 250, 400, 260, 310)
        screen.blit(text16, (260, 260))

        screen.blit(text17, (260, 320))
        check(screen, 250, 400, 320, 370)
        screen.blit(text17, (260, 320))

        screen.blit(text18, (260, 380))
        check(screen, 250, 400, 380, 430)
        screen.blit(text18, (260, 380))

        screen.blit(text19, (260, 440))
        check(screen, 250, 400, 440, 490)
        screen.blit(text19, (260, 440))

        pygame.display.flip()


tempx = visuz()
global meth
size_grid = 3
print(tempx)
if tempx == 1:
    p = Problem([0, 0, 0, 0, 0, 0, 0, 0, 0])
    meth = get_method()
elif tempx == 2:
    x, y = get_size()
    print(x, y)
    size_grid = x
    p = Problem1(create_problem_list(x), x, y)
    meth = get_method()


def Minimax_Decision(state):  # Basic min max
    temp_max = -10
    max_act = []

    for a in p.Actions(state):
        state1 = deepcopy(state)
        temp = Min_value(p.Result(state1, a))
        if temp > temp_max:
            temp_max = temp
            max_act = a
    return max_act


def Max_value(state):
    if p.Termainal_Test(state):
        return p.Utility(state, 1)
    v = -1 * float("inf")

    for a in p.Actions(state):
        state1 = deepcopy(state)
        v = max(v, Min_value(p.Result(state1, a)))
    return v


def Min_value(state):
    if p.Termainal_Test(state):
        return p.Utility(state, 1)
    v = float("inf")

    for a in p.Actions(state):
        state1 = deepcopy(state)
        v = min(v, Max_value(p.Result(state1, a)))
    return v


def alpha_beta_pruning(state, maximizingPlayer, alpha, beta):
    if p.Termainal_Test(state):
        return p.Utility(state, 1)
    if alpha > beta:
        return 0
    alpha1 = deepcopy(alpha)
    beta1 = deepcopy(beta)
    if maximizingPlayer:
        v = -1 * float("inf")
        for a in p.Actions(state):
            state1 = deepcopy(state)
            v = max(v, alpha_beta_pruning(p.Result(state1, a), False, alpha1, beta1))
            alpha1 = v
    else:
        v = float("inf")
        for a in p.Actions(state):
            state1 = deepcopy(state)
            v = min(v, alpha_beta_pruning(p.Result(state1, a), True, alpha1, beta1))
            beta1 = v
    return v


def ab_pruning(state):  # min max with alpha beta pruning
    temp_max = -10
    max_act = []
    alpha = -1 * float("inf")
    beta = float("inf")
    for a in p.Actions(state):
        state1 = deepcopy(state)
        temp = alpha_beta_pruning(p.Result(state1, a), False, alpha, beta)
        if temp > temp_max:
            temp_max = temp
            max_act = a
        alpha = temp_max
    return max_act


def is_empty(state):
    for x in state:
        if x == 0:
            return False
    return True


def print_pretty(state, size):  # Prints the given state in a nice way
    for i in range(0, len(state)):
        if i % size == 0:
            print()
        if state[i] == 0:
            print('_', end=' ')
        elif state[i] == 1:
            print('O', end=' ')
        elif state[i] == 2:
            print('X', end=' ')
    print()


def experment(state):  # expermental minimax function
    temp_max = -1 * float("inf")
    max_act = []
    for a in p.Actions(state):
        state1 = deepcopy(state)
        temp = p.hurestic(p.Result(state1, a))
        if temp > temp_max:
            temp_max = temp
            max_act = a
    return max_act


def Deapth_limit_search(state, depth, maximizingPlayer):
    if p.Termainal_Test(state) or depth == 0:
        return p.hurestic(state)
    if maximizingPlayer:
        v = -1 * float("inf")
        for a in p.Actions(state):
            state1 = deepcopy(state)
            v = max(v, Deapth_limit_search(p.Result(state1, a), depth - 1, False))
    else:
        v = float("inf")
        for a in p.Actions(state):
            state1 = deepcopy(state)
            v = min(v, Deapth_limit_search(p.Result(state1, a), depth - 1, True))
    return v


def DLS(state):  # Depth limit version of the minimax
    temp_max = -1 * float("inf")
    max_act = []
    depth = 1
    for a in p.Actions(state):
        state1 = deepcopy(state)
        temp = Deapth_limit_search(p.Result(state1, a), depth, False)
        if temp > temp_max:
            temp_max = temp
            max_act = a
    return max_act


def ab_pruning_depth_limit(state, maximizingPlayer, depth, alpha, beta):
    if p.Termainal_Test(state) or depth == 0:
        return p.hurestic(state)
    if alpha > beta:
        return 0
    alpha1 = deepcopy(alpha)
    beta1 = deepcopy(beta)
    if maximizingPlayer:
        v = -1 * float("inf")
        for a in p.Actions(state):
            state1 = deepcopy(state)
            v = max(v, ab_pruning_depth_limit(p.Result(state1, a), False, depth - 1, alpha1, beta1))
            alpha1 = v
    else:
        v = float("inf")
        for a in p.Actions(state):
            state1 = deepcopy(state)
            v = min(v, ab_pruning_depth_limit(p.Result(state1, a), True, depth - 1, alpha1, beta1))
            beta1 = v
    return v


def abDLS(state):  # depth limit and alpha beta pruning version of minimax
    temp_max = -1 * float("inf")
    max_act = []
    alpha = -1 * float("inf")
    beta = float("inf")
    depth = 1
    for a in p.Actions(state):
        state1 = deepcopy(state)
        temp = ab_pruning_depth_limit(p.Result(state1, a), False, depth, alpha, beta)
        if temp > temp_max:
            temp_max = temp
            max_act = a
        alpha = temp_max
    return max_act


def draw_circle(screen, x, y, color_circle):  # Draws the circle in the given position of the grid
    pygame.draw.circle(screen, color_circle, (x * 100 + 50, y * 100 + 50), 30, 10)


def draw_cross(screen, x, y, color_cross):  # Draws the cross in the given position of the grid
    pygame.draw.line(screen, color_cross, ((x * 100 + 50) - 30, (y * 100 + 50) - 30),
                     ((x * 100 + 50) + 30, (y * 100 + 50) + 30), 10)
    pygame.draw.line(screen, color_cross, ((x * 100 + 50) + 30, (y * 100 + 50) - 30),
                     ((x * 100 + 50) - 30, (y * 100 + 50) + 30), 10)


def draw_circle_in_position(position, size):  # Gives the position when clicks on the grid
    x = None
    y = None
    for i in range(0, size):
        for j in range(0, size):
            if j * 100 <= position[0] <= (j + 1) * 100 and i * 100 <= position[1] <= (i + 1) * 100:
                x = j
                y = i
                break
    return x, y


def fill_grid(screen, state, color_circle, color_cross, size):  # fills the grid based on a given state
    screen.fill((0, 0, 0))
    for i in range(0, size):
        for j in range(0, size):
            if state[i + size * j] == 1:
                draw_cross(screen, i, j, color_cross)
            elif state[i + size * j] == 2:
                draw_circle(screen, i, j, color_circle)
    pygame.draw.polygon(screen, (0, 255, 255),
                        [(0, size * 100), (size * 100, size * 100), (size * 100, size * 100 + 70),
                         (0, size * 100 + 70)])


def print_on_screen(screen, p):  # prints given text on the screen
    myfont = pygame.font.SysFont('Comic Sans MS', 70)
    textsurface = myfont.render(p, False, (255, 255, 102))
    screen.blit(textsurface, (50, 85))


def game(fun):  # main function and the argument fun is the variant of the nextstep() function
    screen = pygame.display.set_mode((size_grid * 100, size_grid * 100))
    done = True

    color = (0, 212, 50)
    color_circle = (234, 98, 10)
    color_cross = (124, 28, 174)

    is_computer = True

    message = ''
    is_message = False
    while done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = False

            if is_computer == False and pygame.mouse.get_pressed()[0] == 1:
                is_computer = True
                position = pygame.mouse.get_pos()
                x, y = draw_circle_in_position(position, size_grid)
                if x is None or y is None or p.initial_state[x + size_grid * y] != 0:
                    is_computer = False
                else:
                    p.initial_state = p.Result(p.initial_state, [x + size_grid * y, 2])
                    fill_grid(screen, p.initial_state, color_circle, color_cross, size_grid)
                    print_pretty(p.initial_state, size_grid)
                    if p.Utility(p.initial_state, 1) == -1:
                        print('You won')
                        is_message = True
                        message = 'U Won'
                        is_computer = False
                    # break

                    elif is_empty(p.initial_state):
                        print('Draw')
                        is_message = True
                        message = 'Draw'
                        is_computer = False
                    # break

        if is_computer:
            is_computer = False
            act = fun(p.initial_state)
            p.initial_state = p.Result(p.initial_state, act)
            fill_grid(screen, p.initial_state, color_circle, color_cross, size_grid)
            print_pretty(p.initial_state, size_grid)
            if p.Utility(p.initial_state, 1) == 1:
                print('I won')
                is_message = True
                message = 'I Won'
                # break
            elif is_empty(p.initial_state):
                print('Draw')
                is_message = True
                message = 'Draw'
                # break

        for i in range(1, size_grid):
            pygame.draw.line(screen, color, (0, i * 100), (size_grid * 100, i * 100), 10)

        for i in range(1, size_grid):
            pygame.draw.line(screen, color, (i * 100, 0), (i * 100, size_grid * 100), 10)
        if is_message:
            print_on_screen(screen, message)
        pygame.display.flip()


dispacher = {'DLS': DLS, 'Minimax_Decision': Minimax_Decision, 'ab_pruning': ab_pruning, 'experment': experment,
             'abDLS': abDLS}
game(dispacher[meth])
