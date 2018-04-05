
# n queens is the problem of placing queens so that no queens threaten each other
# solution requires that no queens share the same row, column, or diagonal


class NQueens:
    def __init__(self, size):
        self.size = size
        self.columns = [] * self.size

    def place(self, start_row=0):                            # function to find place for queen
        if len(self.columns) == self.size:
            return self.columns
        else:
            for row in range(start_row, self.size):
                if self.is_safe(len(self.columns), row) is True:
                    self.columns.append(row)
                    return self.place()
            else:
                last_row = self.columns.pop()
                return self.place(start_row=last_row + 1)

    def is_safe(self, column, row):                         # function to check if the block is safe
        for threat_row in self.columns:
            threat_column = self.columns.index(threat_row)
            if row == threat_row or column == self.columns.index(threat_row):
                return False
            elif threat_row + threat_column == row + column or threat_row - threat_column == row - column:
                return False
        return True

n = int(input('enter number of queens:'))
queens = NQueens(n)
queens.place()

for col in queens.columns:
    board = ['0'] * len(queens.columns)
    board[col] = 'Q'
    print(' '.join(board))
