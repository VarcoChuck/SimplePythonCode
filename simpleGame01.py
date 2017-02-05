import turtle
import math
from random import randint
from random import choice

class game():

	score = 0
	colorList = ['red', 'blue', 'green', 'yellow', 'orange', 'black', 'white', 'lightgreen']
	def __init__(self):
		self.Screen_Setings()
		self.Wall_Setings()
		self.Player_Setings()

	def Screen_Setings(self):
		screen = turtle.Screen()
		screen.title("My First Game")
		screen.bgcolor("lightblue")
		screen.setup(width=500, height=500, startx=None, starty=None)

	def Wall_Setings(self):
		wall = turtle.Turtle()
		wall.up()
		wall.setposition(-230, -230)
		wall.down()
		wall.pensize(3)
		for i in xrange(4):
			wall.forward(460)
			wall.left(90)

	def Enemy_Setings(self):
		self.enemy = turtle.Turtle()
		self.enemy.color("red")
		self.enemy.shape("circle")
		self.enemy.up()
		self.enemy.setposition(randint(-220, 220), randint(-220, 220))

	def Player_Setings(self):
		self.Enemy_Setings()
		player = turtle.Turtle()
		player.color("green")
		player.shape("turtle")
		player.up()
		
		#Player Speed
		self.playerSpeed = 1
		
		#Function define
		def speedUp():
			self.playerSpeed += 0.25
		def speedDown():
			self.playerSpeed -= 0.25
		def turnLeft():
			player.left(30)
		def turnRight():
			player.right(30)
		def gameExit():
			turtle.bye()
		#Player key bind!
		turtle.onkey(speedUp, 'Up')
		turtle.onkey(speedDown, 'Down')
		turtle.onkey(turnLeft, 'Left')
		turtle.onkey(turnRight, 'Right')
		turtle.onkey(gameExit, 'q')
		turtle.listen()
		#PLayer Move Seting
		playerMove  = True
		while playerMove:
			player.forward(self.playerSpeed)
			if player.xcor() >= 230 or player.xcor() <= -230:
				player.left(180)
			elif player.ycor() >= 230 or player.ycor() <= -230:
				player.left(180)
			d = math.sqrt(math.pow(player.xcor() - self.enemy.xcor(), 2) + math.pow(player.ycor() - self.enemy.ycor(), 2))
			if d <= 8:
				self.enemy.setposition(randint(-220, 220), randint(-220, 220))
				self.enemy.color(choice(game.colorList))
#Initialization class!
game = game()
game.__init__()
