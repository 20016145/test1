import turtle
t = turtle.Turtle()
sides = int(input("how many sides do you  have:"))
side_length = int (input("what are the lengths ："))
def polygon(side_length, sides):
	for i in range(0, sides):
		t.forward(side_length)
		t.right(360/sides)

	turtle.done()
polygon(side_length, sides)


import random 
import turtle
t = turtle.Turtle()
n = 1
size = turetle.Screen()
move = list()
for i in range(1):
        move.append(t)
def walker():
	for i in range(1):
		randomPicked = random.randint(0, 3)
		angle = randomPicked * 90
		move[i].seth(angle)
		move[i].forward(50)
		size.ontimer(walker,20)
walker()

turtle.done()
