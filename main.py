import turtle
import time
import random

# Initial game settings
delay = 0.15
score = 0
high_score = 0
current_level = "Normal"  # Default level is Normal

# Set up the screen
wn = turtle.Screen()
wn.title("Cyberpunk Snake Game")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)  # Turns off the screen updates

# Snake head with eyes
head = turtle.Turtle()
head.shape("circle")
head.color("red")  # Head is red
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake head eyes
eye1 = turtle.Turtle()
eye1.shape("circle")
eye1.color("black")
eye1.penup()
eye1.goto(-10, 15)
eye1.shapesize(0.5)  # Make the eye smaller

eye2 = turtle.Turtle()
eye2.shape("circle")
eye2.color("black")
eye2.penup()
eye2.goto(10, 15)
eye2.shapesize(0.5)  # Make the eye smaller

# Initial snake segments
segments = []
for _ in range(3):
    new_segment = turtle.Turtle()
    new_segment.shape("circle")
    new_segment.color("green")  # Body is green
    new_segment.penup()
    segments.append(new_segment)

# Snake food
food = turtle.Turtle()
food.shape("circle")
food.color("#FF00F5")
food.penup()
food.goto(0, 100)

# Pen for scoring
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

# Level selection function
def set_level(level):
    global delay, current_level
    current_level = level
    if level == "Easy":
        delay = 0.2
    elif level == "Normal":
        delay = 0.15
    elif level == "Hard":
        delay = 0.1

# Functions to control the snake
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Keyboard bindings
wn.listen()
wn.onkey(go_up, "Up")
wn.onkey(go_down, "Down")
wn.onkey(go_left, "Left")
wn.onkey(go_right, "Right")
wn.onkey(lambda: set_level("Easy"), "1")  # Set level to Easy
wn.onkey(lambda: set_level("Normal"), "2")  # Set level to Normal
wn.onkey(lambda: set_level("Hard"), "3")  # Set level to Hard

# Main game loop
while True:
    wn.update()

    # Check for a collision with the border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()

        # Reset the score
        score = 0
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # Check for a collision with the food
    if head.distance(food) < 20:
        # Move the food to a random spot
        while True:
            x = random.randint(-290, 290)
            y = random.randint(-290, 250)  # Prevent food from appearing in the top 50 pixels
            if abs(x) > 50 or y < 240:
                break
        food.goto(x, y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.shape("circle")
        new_segment.color("green")  # Body is green
        new_segment.penup()
        segments.append(new_segment)

        # Increase the score
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # Move the end segments first in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Check for head collision with body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()

            # Reset the score
            score = 0
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)

wn.mainloop()
