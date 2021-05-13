import pygame.draw
import main


class Paddle:
    def __init__(self, position, color):
        self.w = 10
        self.h = 50
        self.speed = 5
        self.score = 0

        if position == 'right':
            self.x = main.Game.width - main.Game.border_size - self.w
        elif position == 'left':
            self.x = main.Game.border_size

        self.y = main.Game.height / 2
        self.color = color

    def show(self):
        pygame.draw.rect(main.Game.screen, self.color, [self.x, self.y, self.w, self.h])

    def move(self, new_y, ball=None):
        # user move
        if (ball is None) and (main.Game.border_size < new_y < main.Game.height - self.h - main.Game.border_size):
            self.y = new_y

        # cpu move
        if (new_y is None) and (ball is not None) and (
                main.Game.width * 0.75 < ball.x or ball.x < main.Game.width / 4):
            if self.y <= ball.y - self.speed:
                self.y += self.speed
            elif self.y >= ball.y + self.speed:
                self.y -= self.speed

            if self.y < main.Game.border_size:
                self.y = main.Game.border_size + 1
            if self.y > main.Game.height - self.h - main.Game.border_size:
                self.y = main.Game.height - self.h - main.Game.border_size - 1
