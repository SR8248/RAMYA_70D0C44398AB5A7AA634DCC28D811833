

#Define the base class player
class player:
  def play(self):
     print("The player is playing cricket.")

#Define thw derived class batsman
class batsman(player):
  def play(self):
      print ("The batsman is batting.")

#Define the derived class bowler
class bowler(player):
  def play(self):
    print("The bowler is bowling.")

#create objects of batsman and bowler classes
batsman = batsman()
bowler = bowler()

#call the play() method for each object
batsman.play()
bowler.play()
