import random
import turtle as t
import pyflakes

t.bgcolor('yellow')

caterpillar = t.Turtle()
caterpillar.shape('square')
caterpillar.color('red')
caterpillar.speed(0)
caterpillar.penup()
caterpillar.hideturtle()

leaf = t.Turtle()
leaf_shape = ((0, 0), (14, 8), (18, 6), (20, 20), \
(6, 18), (2, 14))
t.register_shape('leaf', leaf_shape)
leaf.shape('leaf')
leaf.color('green')
leaf.penup() 
leaf.hideturtle()
leaf.speed(0)

game_started = False
text_turtle = t.Turtle()
text_turtle.write('press SPACE to start', align='center', )
font = ('Arial', 16, 'bold')
text_turtle.hideturtle

score_turtle = t.Turtle()
score_turtle.hideturtle()
score_turtle.speed(0)

def outside_window():
  left_wall = -t.window_width() / 2
	right_wall = -t.window_width() / 2
	top_wall = -t.window_height() / 2
	bottom_wall = -t.window_height() / 2
	(x, y) = caterpillar.pos()
	outside = \
	  x< left_wall or \
	  x> right_wall or \
	  y< bottom_wall or \
	  y> top_wall
	  return outside
  pass
def game_over():
	caterpillar.color('black')
	leaf.color('yellow')
	t.penup()
	t.hideturtle()
	t.write('GAME OVER!', align='center', font=('Arial', 30, 'normal'))
	pass
def display_score(current_score):
	pass 
def place_leaf():
	pass
def start_game():
    pass	
	global game_started
	if game_started:
		return
	game_started = True

	score = 0
	text_turtle.clear()

	caterpillar_speed = 2
	caterpillar_length = 3
	caterpillar.shapesize(1, caterpillar_length, 1)
	caterpillar.showturtle()
	display_score(score)
	place_leaf()
while True:
	caterpillar.forward(caterpillar_speed)
	if caterpillar.distance(leaf) < 20:
	  place_leaf()
    caterpillar_length = caterpillar_length + 1	   caterpillar.shapesize(1, caterpillar_length, 1)
	  caterpillar_speed = caterpillar_speed + 1
    score =	score + 1
    display_score(score)
      if outside_window():
      game_over()
      break
    t.onkkey(start_game, 'space')
    t.listen()
    t.mainloop()
