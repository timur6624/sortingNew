def check_winner(moves):
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
    for r, c in moves:
        for dr, dc in directions:
            count = 1
            for i in range(1, 5):
                if (r + i * dr, c + i * dc) in moves:
                    count += 1
                else:
                    break
                if count == 5:
                    return True
    return False

def tic_tac_toe_winner(n, moves):
    first_moves = []
    second_moves = []

    for i in range(n):
        r, c = moves[i]
        if i % 2 == 0:
            first_moves.append((r, c))
            if check_winner(first_moves):
                if i == n - 1:
                    return "First"
                else:
                    return "Inattention"
        else:
            second_moves.append((r, c))
            if check_winner(second_moves):
                if i == n - 1:
                    return "Second"
                else:
                    return "Inattention"

    if len(moves) == 10000:
        return "Draw"

    return "Draw"

# Чтение ввода
n = int(input())
moves = []
for _ in range(n):
    r, c = map(int, input().split())
    moves.append((r, c))

# Вывод результата
print(tic_tac_toe_winner(n, moves))
