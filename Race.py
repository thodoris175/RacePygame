import turtle
import random
dice=[1,2,3,4,5,6]
dice1 = random.choice(dice)
dice2 = random.choice(dice)
player1 = turtle.Turtle()
player2 = turtle.Turtle()
player1.shape("turtle")
player2.shape("turtle")
player1.color("green")
player2.color("blue")
player1.penup()
player2.penup()
player1.setpos(-100,100)
player2.setpos(-100,-100)

player1.forward(500)
player1.pendown()
player1.circle(60)
player1.penup()
player1.goto(-100,150)

player2.forward(500)
player2.pendown()
player2.circle(60)
player2.penup()
player2.goto(-100,-50)

while player1.pos()<(400,150) and player2.pos()<(400,-50):
    player1.fd(10*dice1)
    player2.fd(10*dice2)

    if player1.pos() >= (400,150):
        print("Player1 wins")
    elif player2.pos() >= (400,-50):
        print("Player2 wins")


turtle.done()
