# 2. Создайте программу для игры в ""Крестики-нолики"".

board = list(range(1,10))

def draw_board(board):
    print("-" * 13)
    print("|", board[0], "|", board[1], "|", board[2], "|")
    print("-" * 13)
    print("|", board[3], "|", board[4], "|", board[5], "|")
    print("-" * 13)
    print("|", board[6], "|", board[7], "|", board[8], "|")
    print("-" * 13)


def take_input(player_token):
   valid = False
   while not valid:
      player_answer = int(input("Куда поставим " + player_token+"? "))
      if player_answer >= 1 and player_answer <= 9:
         if(str(board[player_answer-1]) not in "XO"):
            board[player_answer-1] = player_token
            valid = True
         else:
            print("Эта клетка уже занята!")
      else:
        print("Некорректный ввод. Введите число от 1 до 9.")

def check_win(board):
   win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for cell in win_coord:
       if board[cell[0]] == board[cell[1]] == board[cell[2]]:
          return board[cell[0]]
   return False

def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
           take_input("X")
        else:
           take_input("O")
        counter += 1
        if counter > 4:
           tmp = check_win(board)
           if tmp:
              print(tmp, "выиграл!")
              win = True
              break
        if counter == 9:
            print("Ничья!")
            break
    draw_board(board)

main(board)

