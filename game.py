class Game():

  """docstring for Game"""

  status = True
  team1 = 0
  team2 = 0
  
  dict1 = { 0 : "0", 1:"15", 2: "30", 3:"40", 4: "set!"}

  def __init__(self, team1, team2, status):
    self.status = status
    self.team1 = team1
    self.team2 = team2
    

  #@classmethod
  def scores(self,team):

    if self.status:
      if team == 1:
        self.team1 = self.team1 + 1
      elif team == 2:
        self.team2 = self.team2 + 1
      elif self.team2-self.team1 == 2 or self.team1-self.team2 == 2:
        self.status = False

      return self
      
  #@classmethod
  def score(self):
      #print (self.team1)
      #print (self.team2)
    if((self.team1 >= 4 <= self.team2) ):
      if self.team1-self.team2 == 1:
        print ('['+'advantage1, deuce'+']')
      elif self.team2-self.team1 == 1:
        print ('['+'deuce, advantage2'+']')
      elif self.team1 == self.team2:
        print ('['+'deuce, deuce'+']')
      elif self.team1-self.team2 == 2:
        print ('['+'Wins!, deuce'+']')
      elif self.team2-self.team1 == 2:
        print ('['+'deuce, Wins!'+']')
    elif((self.team1 >= 3 <= self.team2)):
      if self.team1-self.team2 == 1:
        print ('['+'advantage1, 40'+']')
      elif self.team2-self.team1 == 1:
        print ('['+'40, advantage2'+']')
      elif self.team1 == self.team2:
        print ('['+'deuce, deuce'+']')
      elif self.team1-self.team2 == 2:
        print ('['+'Wins!, Loses'+']')
      elif self.team2-self.team1 == 2:
        print ('['+'loses, Wins!'+']')
    elif((self.team1 < 5 or self.team2 < 5) and not(self.team1 == self.team2 >= 3) ):
      x = self.dict1.get(self.team1)
      y = self.dict1.get(self.team2)
      print ('['+x+','+y+']')

    


      
def funcionI():
  """
  >>> g = Game(0,0, True)
  >>> g.score()
  [0,0]
  >>> g = Game(0,0, True)
  >>> g.scores(1).score()
  [15,0]
  >>> g = Game(0,0, True)
  >>> g.scores(1).scores(1).score()
  [30,0]
  >>> g = Game(0,0, True)
  >>> g.scores(1).scores(1).scores(1).score()
  [40,0]
  >>> g = Game(0,0, True)
  >>> g.scores(1).scores(2).score()
  [15,15]
  >>> g = Game(0,0, True)
  >>> g.scores(1).scores(1).scores(1).scores(2).scores(2).scores(2).score()
  [deuce, deuce]
  >>> g = Game(0,0, True)
  >>> g.scores(1).scores(1).scores(1).scores(2).scores(2).scores(2).scores(1).score() 
  [advantage1, 40]
  >>> g = Game(0,0, True)
  >>> g.scores(1).scores(1).scores(1).scores(2).scores(2).scores(2).scores(1).scores(2).score()
  [deuce, deuce]
  >>> g = Game(0,0, True)
  >>> g.scores(1).scores(1).scores(1).scores(2).scores(2).scores(2).scores(1).scores(2).scores(1).score()
  [advantage1, deuce]
  >>> g = Game(0,0, True)
  >>> g.scores(1).scores(1).scores(1).scores(2).scores(2).scores(2).scores(1).scores(2).scores(1).scores(1).score()
  [Wins!, deuce]
  



  
  """
  return 


if __name__ == "__main__":
    import doctest
    doctest.testmod()