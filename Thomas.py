
team_name = 'Thomas'
strategy_name = 'DRS "Down right side"'
strategy_description = ''

'''def print_board(board):
  print(board[0][0]+'|'+board[0][1]+'|'+board[0][2])
  print('-+-+-')
  print(board[1][0]+'|'+board[1][1]+'|'+board[1][2])
  print('-+-+-')
  print(board[2][0]+'|'+board[2][1]+'|'+board[2][2])'''

spot1= 0,0
spot2= 0,1
spot3= 0,2
spot4= 1,0
spot5= 1,1
spot6= 1,2
spot7= 2,0
spot8= 2,1
spot9= 2,2

def move(player, board, score):
  r = 0
  c = 2
  while board[r][c] != ' ':
    r = r + 1
    if r > 2:
      r = 0
      c = c - 2
      
  
  return r, c
  