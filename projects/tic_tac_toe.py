def draw_board(board):
    for i in range(3):
        for j in range(3):
            print(board[i][j], end=' ')
        print()

def is_valid(board, i, j):                                                                                                                                                 
    if i < 0 or i >= 3 or j < 0 or j >= 3 or board[i][j] != '-':
        return False
    return True

def take_and_place_valid_input(board):
    i, j = map(int, input("Enter input row and column separated by space: ").split())
    if is_valid(board, i, j):
        mark = input('Enter Mark:')
        board[i][j] = mark
        return
    else:
        while is_valid(board, i, j) == False:
            i, j = map(int, input("Enter input row and column separated by space again: ").split())
        if is_valid(board, i, j):
            mark = input('Enter Mark:')
            board[i][j] = mark
            return
        
def all_occupied(board):
    for i in range(3):
        for j in range(3):
            if board[i][j]=='-':
                return True
    return False

def check_win(b):
    if b[0][0] != '-' and b[0][0] == b[0][1] == b[0][2]:
        return True
    if b[1][0] != '-' and b[1][0] == b[1][1] == b[1][2]:
        return True
    if b[2][0] != '-' and b[2][0] == b[2][1] == b[2][2]:
        return True
    if b[0][0] != '-' and b[0][0] == b[1][0] == b[2][0]:
        return True
    if b[0][1] != '-' and b[0][1] == b[1][1] == b[2][1]:
        return True
    if b[0][2] != '-' and b[0][2] == b[1][2] == b[2][2]:
        return True
    if b[0][0] != '-' and b[1][1] == b[2][2] == b[0][0]:
        return True
    if b[0][2] != '-' and b[1][1] == b[0][2] == b[2][0]:
        return True
    return False
def who_won(b):
    if b[0][0] != '-' and b[0][0] == b[0][1] == b[0][2]=='a':
        return 'a'
    if b[0][0] != '-' and b[0][0] == b[0][1] == b[0][2]=='b':
        return 'b'
    if b[1][0] != '-' and b[1][0] == b[1][1] == b[1][2]=='a':
        return 'a'
    if b[1][0] != '-' and b[1][0] == b[1][1] == b[1][2]=='b':
        return 'b'
    if b[2][0] != '-' and b[2][0] == b[2][1] == b[2][2]=='a':
        return 'a'
    if b[2][0] != '-' and b[2][0] == b[2][1] == b[2][2]=='b':
        return 'b'
    if b[0][0] != '-' and b[0][0] == b[1][0] == b[2][0]=='a':
        return 'a'
    if b[0][0] != '-' and b[0][0] == b[1][0] == b[2][0]=='b':
        return 'b'
    if b[0][1] != '-' and b[0][1] == b[1][1] == b[2][1]=='a':
        return 'a'
    if b[0][1] != '-' and b[0][1] == b[1][1] == b[2][1]=='b':
        return 'b'
    if b[0][2] != '-' and b[0][2] == b[1][2] == b[2][2]=='a':
        return 'a'
    if b[0][2] != '-' and b[0][2] == b[1][2] == b[2][2]=='b':
        return 'b'
    if b[0][0] != '-' and b[1][1] == b[2][2] == b[0][0]=='a':
        return 'a'
    if b[0][0] != '-' and b[1][1] == b[2][2] == b[0][0]=='b':
        return 'b'
    if b[0][2] != '-' and b[1][1] == b[0][2] == b[2][0]=='a':
        return 'a'
    if b[0][2] != '-' and b[1][1] == b[0][2] == b[2][0]=='b':
        return 'b'

board = [['-' for _ in range(3)] for _ in range(3)]
def main():
    draw_board(board)
    take_and_place_valid_input(board)
    if check_win(board) == False and all_occupied(board)== True:
        main()
    elif all_occupied(board)== False and check_win(board) == False:
        print('Game Draw')
    else:
        print('Congargulations',who_won(board),'won the game')
main()