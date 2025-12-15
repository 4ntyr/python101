import turtle
ecken = abs(int(input("Wie viele Ecken soll die Form haben?: ")))
alice = turtle.Turtle()
i = ecken
while i>0:
    alice.forward(500/ecken)
    alice.left(360/ecken)
    i -= 1
turtle.done()