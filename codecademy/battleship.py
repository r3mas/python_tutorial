from random import randint

board = []

for i in range(5):
    board.append(['O'] * 5)


def print_board(board_in):
    for row in board_in:
        print " ".join(row)

def random_row(board_in):
    return randint(0,len(board_in) -1)

def random_col(board_in):
    return randint(0,len(board_in) -1)

ship_row = random_row(board)
ship_col = random_col(board)

print ship_row
print ship_col

guess_row = int(raw_input("Guess Row: "))
guess_col = int(raw_input("Guess Col: "))

if guess_row == ship_row and guess_col == ship_col:
    print "Congratulations! You sank my battleship!"

#print board
#print_board(board)

