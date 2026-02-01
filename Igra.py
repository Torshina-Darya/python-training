def print_board(board):
    """Вывод игрового поля на экран"""
    print("\n    0  1  2 ")
    for i, row in enumerate(board):
        print(f" {i}  {'  '.join(row)} ")
    print()
 
def check_winner(board):
    """Проверка победы"""
    # Проверка строк
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return row[0]
    
    # Проверка столбцов
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return board[0][col]
    
    # Проверка диагоналей
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    
    return None
 
def check_draw(board):
    """Проверка на ничью"""
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True
 
def make_move(board, row, col, current_player):
    """Ход игрока"""
    if row < 0 or row > 2 or col < 0 or col > 2:
        print("Неверные координаты хода. Используйте числа от 0 до 2")
        return False
        
    if board[row][col] != ' ':
        print("Клетка уже занята")
        return False
        
    board[row][col] = current_player
    return True
 
def play_game():
    """Основной игровой цикл"""
    # Инициализация игрового поля
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    game_over = False
    winner = None
    
    print("Игроки поочередно вводят координаты клетки (строка/столбец)")
    
    while not game_over:
        print_board(board)
        print(f"Ход игрока {current_player}")
        
        try:
            coords = input("Введите координаты (строка/столбец): ").split()
            if len(coords) != 2:
                print("Введите 2 координаты через пробел")
                continue
                
            row, col = int(coords[0]), int(coords[1])
            
            if make_move(board, row, col, current_player):
                # Проверка победы
                winner = check_winner(board)
                if winner:
                    game_over = True
                # Проверка на ничью
                elif check_draw(board):
                    game_over = True
                else:
                    # Смена игрока
                    current_player = 'O' if current_player == 'X' else 'X'
            
        except ValueError:
            print("Необходимо вводить только числа")
        except KeyboardInterrupt:
            print("\nИгра прервана")
            return
    
    print_board(board)
    
    if winner:
        print(f"Игрок {winner} победил")
    else:
        print("Ничья")
        
# Запуск игры
if __name__ == "__main__":
    play_game()