#board
#display board
#play game
#check win
  #check rows,columns,diagonals
#check tie
# flip between player

#global variable
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

game_still_going = True

winner = None

current_player = "X"

 

def play_game():
  display_board()
  while game_still_going:

     handle_turn(current_player)
     check_if_game_over()
     flip_player()
  
  #THE GAME HAS ENDED
  if winner == "X" or winner == "O":
    print(winner + " won!") 
  elif winner == None:
    print("its a tie! ")   

def display_board():         
  print(board[0] + " | " + board[1] + " | " + board[2])
  print(board[3] + " | " + board[4] + " | " + board[5])
  print(board[6] + " | " + board[7] + " | " + board[8])      

def handle_turn(player):
  print(player + " 's turn")
  position = input("enter position between 1 to 9:- ")
  
  valid = False
  while not valid:
     while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
       position = input("Choose a position between 1 to 9:- ")

     position = int(position) - 1

     if board[position] == "-":
       valid = True
     else:  
       print(" OOPS ! you can't overrite the position. Go Again!")

  board[position] = player

  display_board()

def check_if_game_over():
  check_for_winner()
  check_tie()

def check_for_winner():
  global winner
  #check rows
  row_winner = check_rows()
  #check columns
  col_winner = check_col()
  #check diagonals
  diag_winner = check_diag()
  if row_winner:
    winner = row_winner
  elif col_winner:
    winner = col_winner
  elif diag_winner:
    winner = diag_winner
  else: 
    winner = None  
  

def check_rows():

  global game_still_going

  row1 = board[0] == board[1] == board[2] != "-"
  row2 = board[3] == board[4] == board[5] != "-"
  row3 = board[6] == board[7] == board[8] != "-"
  #if any row has a match, flat that it is a winner
  if row1 or row2 or row3:
    game_still_going = False
  if row1:
    return board[0]
  elif row2:
    return board[3]
  elif row3:
    return board[6]  
  else:
    return None      
  

def check_col():
  global game_still_going
  col1 = board[0] == board[3] == board[6] != "-"
  col2 = board[1] == board[4] == board[7] != "-"
  col3 = board[2] == board[5] == board[8] != "-"
  #if any row has a match, flat that it is a winner
  if col1 or col2 or col3:
    game_still_going = False


  if col1:
    return board[0]
  elif col2:
    return board[1]
  elif col3:
    return board[2]   
  else: 
    return None  


def check_diag():

  global game_still_going

  diag1 = board[0] == board[4] == board[8] != "-"
  diag2 = board[2] == board[4] == board[6] != "-"
  
  #if any row has a match, flat that it is a winner
  if diag1 or diag2:
    game_still_going = False
    #return the winner X or O
  if diag1:
    return board[0]
  elif diag2:
    return board[2]
  else:
    return None  
 
  

def check_tie():

  global game_still_going

  if "-" not in board:
    game_still_going = False
    return True
  else:
    return False  

def flip_player():

  global current_player

  if current_player == "X":
    current_player = "O"

  elif current_player == "O":
    current_player = "X"  
  

play_game()  