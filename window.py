import pygame as pg
import random as r

# Colors
white = (255,255,255)
blue = (10,10,255)

# Studbollar
class Ball:
    def __init__(self, cords):
        self.color = (r.randint(0,255) , r.randint(0,255), r.randint(0,255))
        self.cords = list(cords)
        self.size = 20
        self.vel = [r.random()-0.5, 0]
        self.gravity = 0.005

    def move(self):
        # Apply gravity to the vertical velocity
        self.vel[1] += self.gravity

        # Update the ball's position based on its velocity
        self.cords[0] += self.vel[0]
        self.cords[1] += self.vel[1]

        # Check for collision with the horizontal borders and reverse direction if necessary
        if self.cords[0] <= 0 or self.cords[0] >= 1000:  # Horizontal bounds
            self.vel[0] = -self.vel[0]

        # Check for collision with the ground and speed up on bounce
        if self.cords[1] >= 700:  # Vertical bounds (ground level)
            self.cords[1] = 700  # Prevent the ball from going below the ground
            self.vel[1] = -self.vel[1]  # Reverse and increase the vertical velocity

class Game:
    def __init__(self):
        self.winSize = [1000,700]
        self.win = pg.display.set_mode(self.winSize)
        self.winColor = white
    
        
    def drawBall(self, oBall):
        pg.draw.circle(screen.win, oBall.color, oBall.cords, oBall.size)
    
# Create the screen and ball objects
screen = Game()
balls = []


def main():
    while True:
        screen.win.fill(screen.winColor)

        # Draw all the balls
        for ball in balls:
            ball.move()
            screen.drawBall(ball)
        

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    balls.append(Ball(pg.mouse.get_pos()))
        pg.display.update()

main()
