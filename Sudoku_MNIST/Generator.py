import time
import copy
import random

""" [Level of Difficulty] = Input the level of difficulty of the sudoku puzzle. Difficulty levels
    include ‘0 Easy’ ‘1 Medium’ ‘2 Hard’ and ‘3 Insane’. Outputs a sudoku of desired
    difficulty."""




class Cell():
  """ Initilalizes cell object. A cell is a single box of a sudoku puzzle. 81 cells make up the body of a
    sudoku puzzle. Initializes puzzle with all possible answers available, solved to false, and position of cell within the
    sudoku puzzle"""
  def __init__(self, position):
    self.possibleAnswers = [1,2,3,4,5,6,7,8,9]
    self.answer = None
    self.position = position
    self.solved = False

  def remove(self, num):
    """Removes num from list of possible anwers in cell object."""
    if num in self.possibleAnswers and self.solved == False:
      self.possibleAnswers.remove(num)
      if len(self.possibleAnswers) == 1:
        self.answer = self.possibleAnswers[0]
        self.solved = True
    if num in self.possibleAnswers and self.solved == True:
      self.answer = 0

  def solvedMethod(self):
    """ Returns whether or not a cell has been solved"""
    return self.solved

  def checkPosition(self):
    """ Returns the position of a cell within a sudoku puzzle. x = row; y = col; z = box number"""
    return self.position

  def returnPossible(self):
    """ Returns a list of possible answers that a cell can still use"""
    return self.possibleAnswers

  def lenOfPossible(self):
    """ Returns an integer of the length of the possible answers list"""
    return len(self.possibleAnswers)

  def returnSolved(self):
    """ Returns whether or not a cell has been solved"""
    if self.solved == True:
      return self.possibleAnswers[0]
    else:
      return None

  def setAnswer(self, num):
    """ Sets an answer of a puzzle and sets a cell's solved method to true. This
      method also eliminates all other possible numbers"""
    if num in [1,2,3,4,5,6,7,8,9]:
      self.solved = True
      self.answer = num
      self.possibleAnswers = [num]
    else:
      raise(ValueError)

  def reset(self):
    """ Resets all attributes of a cell to the original conditions"""
    self.possibleAnswers = [1,2,3,4,5,6,7,8,9]
    self.answer = None
    self.solved = False

class Generator():
  def emptySudoku(self):
    ''' Creates an empty sudoku in row major form. Sets up all of the x, y, and z
      coordinates for the sudoku cells'''
    ans = []
    for x in range(1,10):
      if x in [7,8,9]:
        intz = 7
        z = 7
      if x in [4,5,6]:
        intz = 4
        z = 4
      if x in [1,2,3]:
        intz = 1
        z = 1
      for y in range(1,10):
        z = intz
        if y in [7,8,9]:
          z += 2
        if y in [4,5,6]:
          z += 1
        if y in [1,2,3]:
          z += 0
        c = Cell((x,y,z))
        ans.append(c)
    return ans

  def printSudoku(self, sudoku):
    '''Prints out a sudoku in a format that is easy for a human to read'''
    row1 = []
    row2 = []
    row3 = []
    row4 = []
    row5 = []
    row6 = []
    row7 = []
    row8 = []
    row9 = []
    for i in range(81):
      if i in range(0,9):
        row1.append(sudoku[i].returnSolved())
      if i in range(9,18):
        row2.append(sudoku[i].returnSolved())
      if i in range(18,27):
        row3.append(sudoku[i].returnSolved())
      if i in range(27,36):
        row4.append(sudoku[i].returnSolved())
      if i in range(36,45):
        row5.append(sudoku[i].returnSolved())
      if i in range(45,54):
        row6.append(sudoku[i].returnSolved())
      if i in range(54,63):
        row7.append(sudoku[i].returnSolved())
      if i in range(63,72):
        row8.append(sudoku[i].returnSolved())
      if i in range(72,81):
        row9.append(sudoku[i].returnSolved())
    print(row1[0:3],row1[3:6],row1[6:10])
    print(row2[0:3],row2[3:6],row2[6:10])
    print(row3[0:3],row3[3:6],row3[6:10])
    print('')
    print(row4[0:3],row4[3:6],row4[6:10])
    print(row5[0:3],row5[3:6],row5[6:10])
    print(row6[0:3],row6[3:6],row6[6:10])
    print('')
    print(row7[0:3],row7[3:6],row7[6:10])
    print(row8[0:3],row8[3:6],row8[6:10])
    print(row9[0:3],row9[3:6],row9[6:10])

  def sudokuGen(self):
    '''Generates a completed sudoku. Sudoku is completly random'''
    cells = [i for i in range(81)] ## our cells is the positions of cells not currently set
    sudoku = self.emptySudoku()
    while len(cells) != 0:         # until there is blanks
      lowestNum = []
      Lowest = []
      for i in cells:
        lowestNum.append(sudoku[i].lenOfPossible())  ## finds all the lengths of possible answers for each remaining cell
      m = min(lowestNum)  ## finds the minimum of possible answers
      '''Puts all of the cells with the lowest number of possible answers in a list titled Lowest'''
      for i in cells:
        if sudoku[i].lenOfPossible() == m:   # if some cell have lowest length of possible answers
          Lowest.append(sudoku[i])           # append it to lowest list
      '''Now we randomly choose a possible answer and set it to the cell'''
      choiceElement = random.choice(Lowest)  # maybe there are many elements which have same length of possible answers, so, pick one randomly
      choiceIndex = sudoku.index(choiceElement)  # check index of elements
      cells.remove(choiceIndex)                  # remove it from cells(0-80)
      position1 = choiceElement.checkPosition()  # check the cell's position
      if choiceElement.solvedMethod() == False:  # if the cell was not solved yet
        possibleValues = choiceElement.returnPossible()  # check possible values
        finalValue = random.choice(possibleValues)       # choose value from possible values "randomly" which can lead wrong results
        choiceElement.setAnswer(finalValue)              # assign final value to the cell
        for i in cells:  ## in sudoku, every row, col, box can't have same number
          position2 = sudoku[i].checkPosition()   # for the left every cells,
          if position1[0] == position2[0]:        # if they have same row
            sudoku[i].remove(finalValue)          # remove the final value which already have been used
          if position1[1] == position2[1]:        # if they have same col
            sudoku[i].remove(finalValue)          # remove the final value which already have been used
          if position1[2] == position2[2]:        # if they have same box
            sudoku[i].remove(finalValue)          # remove the final value which already have been used

      else:                                       # if the cell was solved which means there's only one possible answer
        finalValue = choiceElement.returnSolved() # final value is the last possiblen answer
        for i in cells:  ##now we iterate through the remaining unset cells and remove the input if it's in the same row, col, or box
          position2 = sudoku[i].checkPosition()
          if position1[0] == position2[0]:
            sudoku[i].remove(finalValue)
          if position1[1] == position2[1]:
            sudoku[i].remove(finalValue)
          if position1[2] == position2[2]:
            sudoku[i].remove(finalValue)
    return sudoku

  def sudokuChecker(self, sudoku):
    """ Checks to see if an input a completed sudoku puzzle is of the correct format and abides by all
      of the rules of a sudoku puzzle. Returns True if the puzzle is correct. False if otherwise"""
    for i in range(len(sudoku)):
      for n in range(len(sudoku)):
        if i != n:    # for every cell, we'll consider every combination of two cell
          position1 = sudoku[i].checkPosition()  # check position of first cell
          position2 = sudoku[n].checkPosition()  # check position of second cell
          if position1[0] == position2[0] or position1[1] == position2[1] or position1[2] == position2[2]:   # if two cell have same row or col or box
            num1 = sudoku[i].returnSolved()  # shows first cell's solved value
            num2 = sudoku[n].returnSolved()  # shows second cell's solved value
            if num1 == num2:                 # If two cells have same value
              return False                   # then return False
    return True                              # or return True

  def perfectSudoku(self):
    '''Generates a completed sudoku. Sudoku is in the correct format and is completly random'''
    result = False
    while result == False:    # if solved sudoku can pass sudoku checker, they'll stop generating solutions
      s = self.sudokuGen()    # if solved sudoku can't pass sudoku checker, they'll make another solution from the first step
      result = self.sudokuChecker(s)   # check by sudoku checker and refresh result which was assigned as False
    return s

  def solver(self, sudoku, f = 0):
    """ Input an incomplete Sudoku puzzle and solver method will return the solution to the puzzle. First checks to see if any obvious answers can be set
      then checks the rows columns and boxes for obvious solutions. Lastly the solver 'guesses' a random possible answer from a random cell and checks to see if that is a
      possible answer. If the 'guessed' answer is incorrect, then it removes the guess and tries a different answer in a different cell and checks for a solution. It does this until
      all of the cells have been solved. Returns a printed solution to the puzzle and the number of guesses that it took to complete the puzzle. The number of guesses is
      a measure of the difficulty of the puzzle. The more guesses that it takes to solve a given puzzle the more challenging it is to solve the puzzle"""
    if f > 900:    # If this sudoku needs more than 900 trials,
      return False #  we define this sudoku as impossible to solve.
    guesses = 0    # trials start from 0
    copy_s = copy.deepcopy(sudoku)  # Copy original sudoku
    cells = [i for i in range(81)] ## our cells is the positions of cells not currently set
    solvedCells = []  # solved cell was empty at first
    for i in cells:   # for 81 cells,
      if copy_s[i].lenOfPossible() == 1:  # if some cells have only one possible option,
        solvedCells.append(i)             # we add those cells in solved cells.
    while solvedCells != []:              # so, if there are something in solved cells,
      for n in solvedCells:
        cell = copy_s[n]
        position1 = cell.checkPosition()
        finalValue = copy_s[n].returnSolved()
        for i in cells:  ##now we itterate through the remaing unset cells and remove the input if it's in the same row, col, or box
          position2 = copy_s[i].checkPosition()
          if position1[0] == position2[0]:
            copy_s[i].remove(finalValue)
          if position1[1] == position2[1]:
            copy_s[i].remove(finalValue)
          if position1[2] == position2[2]:
            copy_s[i].remove(finalValue)
          if copy_s[i].lenOfPossible() == 1 and i not in solvedCells and i in cells:
            solvedCells.append(i)
          ##print(n)
        solvedCells.remove(n)
        cells.remove(n)
      if cells != [] and solvedCells == []:
        lowestNum=[]
        lowest = []
        for i in cells:
          lowestNum.append(copy_s[i].lenOfPossible())
        m = min(lowestNum)
        for i in cells:
          if copy_s[i].lenOfPossible() == m:
            lowest.append(copy_s[i])
        randomChoice = random.choice(lowest)
        randCell = copy_s.index(randomChoice)
        randGuess = random.choice(copy_s[randCell].returnPossible())
        copy_s[randCell].setAnswer(randGuess)
        solvedCells.append(randCell)
        guesses += 1
    if self.sudokuChecker(copy_s):
      if guesses == 0:
        level = 0
      elif guesses <= 2:
        level = 1
      elif guesses <= 7:
        level = 2
      else:
        level = 3
      return copy_s, guesses, level
    else:
      return self.solver(sudoku, f+1)

  def solve(self, sudoku, n = 0):
    """ Uses the solver method to solve a puzzle. This method was built in order to avoid recursion depth errors. Returns True if the puzzle is solvable and
      false if otherwise"""
    if n < 30:
      s = self.solver(sudoku)
      if s != False:
        return s
      else:
        self.solve(sudoku, n+1)
    else:
      return False

  def puzzleGen(self, sudoku):
    """ Generates a puzzle with a unique solution. """
    cells = [i for i in range(81)]
    while cells != []:
      copy_s = copy.deepcopy(sudoku)
      randIndex = random.choice(cells)
      cells.remove(randIndex)
      copy_s[randIndex].reset()
      s = self.solve(copy_s)
      if s[0] == False:
        f = self.solve(sudoku)
        print("Guesses: " + str(f[1]))
        print("Level: " + str(f[2]))
        return self.printSudoku(sudoku)
      elif self.equalChecker(s[0], self.solve(copy_s)[0]):
        if self.equalChecker(s[0], self.solve(copy_s)[0]):
          sudoku[randIndex].reset()
      else:
        f = self.solve(sudoku)

        return sudoku, f[1], f[2]

  def equalChecker(self,s1,s2):
    """ Checks to see if two puzzles are the same"""
    for i in range(len(s1)):
      if s1[i].returnSolved() != s2[i].returnSolved():
        return False
    return True

  def generate(self, level):
    """ Input the level of difficulty of the sudoku puzzle. Difficulty levels
      include ‘Easy’ ‘Medium’ ‘Hard’ and ‘Insane’. Outputs a sudoku of desired
      difficulty."""
    t1 = time.time()
    n = 0
    p = self.perfectSudoku()
    answer = copy.deepcopy(p)
    s = self.puzzleGen(p)

    if level == 0:
      if s[2] != 0:
        return self.generate(level)
    elif level == 1:
      while s[2] == 0:
        n += 1
        s = self.puzzleGen(p)
        if n > 50:
          return self.generate(level)
      if s[2] != 1:
        return self.generate(level)
    elif level == 2:
      while s[2] == 0:
        n += 1
        s = self.puzzleGen(p)
        if n > 50:
          return self.generate(level)
      while s[2] == 1:
        n += 1
        s = self.puzzleGen(p)
        if n > 50:
          return self.generate(level)
      if s[2] != 2:
        return self.generate(level)
    elif level == 3:
      while s[2] != 3:
        n += 1
        s = self.puzzleGen(p)
        if n > 50:
          return self.generate(level)
    else:
      raise(ValueError)

    t2 = time.time()
    t3 = t2 - t1
    print("Runtime is " + str(t3) + " seconds")
    print("Guesses: " + str(s[1]))
    print("Level: " + str(s[2]))
    self.printSudoku(s[0])

    return s[0], answer

  def get(self, sudoku):
    result = []
    for i in range(81):
      result.append(sudoku[i].returnSolved())
    return result
