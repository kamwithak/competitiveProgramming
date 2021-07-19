"""
Given a 2D List:
return the difference between two sums 

n-sized matrix 
n=3
[[a,b,c],[d,e,f],[g,h,i]]

sumA = a + e + i
sumB = c + e + g

=> sumA - sumB
"""

def differenceInSum(arr):

  i = 0
  j = len(arr[0])-1

  sum_A, sum_B = 0, 0

  for vector in arr:
    sum_A += vector[i]
    i += 1
    sum_B += vector[j]
    j -= 1

  print(f"sum_A: {sum_A}")
  print(f"sum_B: {sum_B}")

  return sum_A - sum_B

# print(differenceInSum([[2,1,1],[1,2,1],[1,1,1]]))

"""

Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

"""

def reverseWords(s: str) -> str:
  arr = s.split(" ")
  words = []
  for word in arr[::-1]:
    if (word != ''):
      words.append(word)
  return ' '.join(words)

# print(reverseWords('hey how    are you'))

"""
Make tic tac toe!!!
"""

class TicTacToe():
  def __init__(self, initial_player='X', game_exit=False):
    self.board = self.initialize_empty_board()
    self.current_player = initial_player
    self.game_exit = game_exit
    self.game_winner = None
    self.turn_ctr = 1
    self.print_board()

  def initialize_empty_board(self):
    return {
      1: None,
      2: None,
      3: None,
      4: None,
      5: None,
      6: None,
      7: None,
      8: None,
      9: None,
    }

  def print_board(self):
    print('~~~~~')
    print(f"{self.board[7] if (self.board[7] != None) else 7}|{self.board[8] if (self.board[8] != None) else 8}|{self.board[9] if (self.board[9] != None) else 9}")
    print(f"{self.board[4] if (self.board[4] != None) else 4}|{self.board[5] if (self.board[5] != None) else 5}|{self.board[6] if (self.board[6] != None) else 6}")
    print(f"{self.board[1] if (self.board[1] != None) else 1}|{self.board[2] if (self.board[2] != None) else 2}|{self.board[3] if (self.board[3] != None) else 3}")
    print('~~~~~')

  def game_engine(self):
    print('Welcome to a new game of Tic Tac Toe!')
    while (not self.game_exit):
      print(f'Current player: {self.current_player}')
      desired_position = input('Please select a position between 1 and 9:')
      if (desired_position.isalpha() or desired_position == ''):
        continue
      elif (not (1 <= int(desired_position) <= 9)):
        continue
      else:
        desired_position = int(desired_position)
        if (not self.board[desired_position]):
          print(f"Turn: {self.turn_ctr}")
          self.board[desired_position] = self.current_player
          
          if (self.verify_winner()):
            print(f'Winner: {self.game_winner}')
            self.game_exit = True
          elif (self.turn_ctr == 9):
            print('Tie! No Winner...')
            self.game_exit = True
          
          if (self.current_player == 'X'):
            self.current_player = 'Y'
          elif (self.current_player == 'Y'):
            self.current_player = 'X'

        else:
          print(f'Sorry, {desired_position} is occupied')
          continue
        
        self.turn_ctr += 1
        self.print_board()

        if (self.game_winner):
          restart = input('Do you want to restart? y/n').lower()
          if (restart == 'y'):
            self.__init__(initial_player=self.game_winner)

  def verify_winner(self):
    if (self.turn_ctr < 4):
      return False

    desired_symbol = self.current_player

    if (self.board[1] == self.board[2] == self.board[3] == desired_symbol):
      self.game_winner = desired_symbol
      return True
    elif (self.board[4] == self.board[5] == self.board[6] == desired_symbol):
      self.game_winner = desired_symbol
      return True
    elif (self.board[7] == self.board[8] == self.board[9] == desired_symbol):
      self.game_winner = desired_symbol
      return True
    elif (self.board[1] == self.board[4] == self.board[7] == desired_symbol):
      self.game_winner = desired_symbol
      return True
    elif (self.board[2] == self.board[5] == self.board[8] == desired_symbol):
      self.game_winner = desired_symbol
      return True
    elif (self.board[3] == self.board[6] == self.board[9] == desired_symbol):
      self.game_winner = desired_symbol
      return True
    elif (self.board[1] == self.board[5] == self.board[9] == desired_symbol):
      self.game_winner = desired_symbol
      return True
    elif (self.board[7] == self.board[5] == self.board[3] == desired_symbol):
      self.game_winner = desired_symbol
      return True

    return False
    

if __name__ == '__main__':
  obj = TicTacToe()
  obj.game_engine()















