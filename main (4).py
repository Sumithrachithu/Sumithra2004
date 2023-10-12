'''Implement a class called player that represents a cricket a a cricket player. The player class should have a
method called play() which prints "The players is playing cricket. Derive a two classes,Batsman and
Bowler,from the player class. Override the play() method in each derived class to print "The batsman
is batting" and "The blower is blowing", respectively. Write a program to create subjects or both the
Batsman and Bowler classes and call the play() method for each object.'''


#Define the base class player
class player:
      def play(self):
       print("The player is playing cricket.")

#Define The derived class Batsman
class Batsman(player):
      def play(self):
        print("The batsman is batting.")

#Define the derived class Bowler
class Bowler(player):
      def play(self):
        print("The bowler is bowling.")

#create objects of Batsman and Bowler classes
batsman=Batsman()
bowler=Bowler()

#call the paly() method for each object
batsman.play()
bowler.play()