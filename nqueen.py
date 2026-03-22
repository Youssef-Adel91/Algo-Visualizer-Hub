

def is_safe(board, row, col, n):
    # Check column
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    # Check upper-left diagonal
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i = i - 1
        j = j - 1
    
    # Check upper-right diagonal
    i = row - 1
    j = col + 1
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i = i - 1
        j = j + 1
    
    return True


def solve_n_queens(board, row, n):
    # Base case
    if row == n:
        return True
    
    # Try placing queen in each column
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            
            if solve_n_queens(board, row + 1, n):
                return True
            
            # Backtrack
            board[row][col] = 0
    
    return False


def print_board(board, n):
    """
    Print the board - DO NOT MODIFY
    Q = Queen, . = Empty
    """
    print()
    print("  " + " ".join(str(i) for i in range(n)))
    print("  " + "-" * (n * 2 - 1))
    for i in range(n):
        row_str = ""
        for j in range(n):
            if board[i][j] == 1:
                row_str = row_str + "Q "
            else:
                row_str = row_str + ". "
        print(str(i) + "|" + row_str)
    print()


def solve_8_queens():
    """
    Solve the 8 Queens problem - DO NOT MODIFY
    """
    n = 8
    
    # Create empty 8x8 board
    board = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(0)
        board.append(row)
    
    print("=" * 50)
    print("8 QUEENS PROBLEM")
    print("=" * 50)
    print()
    
    # Solve the problem
    if solve_n_queens(board, 0, n):
        print("Solution found!")
        print_board(board, n)
        
        # Print column positions
        print("Queens at columns:")
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    print("Row " + str(i) + ": Column " + str(j))
    else:
        print("No solution exists!")


# Test with smaller board first
print("TEST 1: 4-Queens (easier)")
print("=" * 50)
n = 4
board = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(0)
    board.append(row)

if solve_n_queens(board, 0, n):
    print("4-Queens solution found!")
    print_board(board, n)
else:
    print("No solution for 4-Queens")

print()
print()

# Test 8-Queens
print("TEST 2: 8-Queens (main problem)")
solve_8_queens()