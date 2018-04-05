
# The Knight’s tour problem
# find the best path followed by knight to cover all cells of 8x8 chess board


import sys


class KnightsTour:                                           # initialize class
    def __init__(self, width, height):                       # max values of board (grid)
        self.width = width
        self.height = height
        self.board = []                                      # list to save board (grid)
        self.create_board()

    def create_board(self):                                  # function to create board (grid)
        for i in range(self.height):
            self.board.append([0] * self.width)              # create 2d list (board) of all 0's 

    def print_board(self):                                   # function to print board (grid)
        print('Knight path to cover all blocks of chess board:')
        for row in self.board:                               # iterate through rows
            for column in row:                               # iterate through column of each row
                print(column, end='  ')
            print()

    def jump(self, current_position):                        # find best possible jump for knight
        possible_position = []
        move_offsets = [(1, 2), (1, -2), (-1, 2), (-1, -2),  # possible steps take by knight
                        (2, 1), (2, -1), (-2, 1), (-2, -1)]

        for move in move_offsets:                            # finding the move from current position
            x = current_position[0] + move[0]
            y = current_position[1] + move[1]

            if x >= self.height:
                continue
            elif x < 0:
                continue
            elif y >= self.width:
                continue
            elif y < 0:
                continue
            else:
                possible_position.append((x, y))
        return possible_position

    def neighbours(self, next_node):                         # function to find the near neighbours
        neighbor_list = self.jump(next_node)
        empty_neighbours = []

        for neighbor in neighbor_list:
            np_value = self.board[neighbor[0]][neighbor[1]]
            if np_value == 0:
                empty_neighbours.append(neighbor)

        scores = []
        for empty in empty_neighbours:
            score = [empty, 0]
            moves = self.jump(empty)
            for m in moves:
                if self.board[m[0]][m[1]] == 0:
                    score[1] += 1
            scores.append(score)

        sorted_score = sorted(scores, key=lambda s: s[1])
        sorted_neighbours = [s[0] for s in sorted_score]
        return sorted_neighbours

    def tour(self, current_depth, current_path, next_node):

        self.board[next_node[0]][next_node[1]] = current_depth
        current_path.append(next_node)                       # append the newest vertex to the current point

        if current_depth == self.width * self.height:        # if every block is filled
            self.print_board()
            sys.exit()

        else:
            sorted_neighbours = self.neighbours(next_node)
            for neighbor in sorted_neighbours:
                self.tour(current_depth + 1, current_path, neighbor)

            # If we exit this loop, all neighbours failed so we reset
            self.board[next_node[0]][next_node[1]] = 0
            try:
                current_path.pop()
            except IndexError:
                print("No path found")
                sys.exit()


knight = KnightsTour(8, 8)          # initiate object with 8x8 size
knight.tour(1, [], (0, 0))          # set starting point as 0,0
