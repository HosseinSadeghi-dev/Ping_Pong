import numpy as np
import pygame
import main
import random
from shared.color import Color


class Ball:
    def __init__(self):
        self.r = 10
        self.x = main.Game.width / 2
        self.y = main.Game.height / 2
        self.speed = 10
        self.color = Color.white

        np.set_printoptions(precision=1)
        # dir_x should not be zero because it will move just vertical
        self.dir_x = random.choice([-1, 1])
        self.dir_y = np.random.uniform(-1, 1)

    def show(self):
        pygame.draw.circle(main.Game.screen, self.color, [self.x, self.y], self.r)

    def move(self, paddles):
        # collied to wall
        if not (main.Game.border_size < self.y < main.Game.height - main.Game.border_size):
            self.dir_y *= -1

        # hit paddle
        elif pygame.Rect(self.x, self.y, self.r, self.r).colliderect(
                pygame.Rect(paddles[0].x, paddles[0].y, paddles[0].w + 10, paddles[0].h)) or pygame.Rect(
                self.x, self.y, self.r, self.r).colliderect(
                pygame.Rect(paddles[1].x, paddles[1].y, paddles[1].w + 10, paddles[1].h)):
            self.dir_x *= -1

        # hit corner of paddles
        elif pygame.Rect(self.x, self.y, self.r, self.r).colliderect(
                pygame.Rect(paddles[0].x, paddles[0].y - paddles[0].h / 4, paddles[0].w + 10, paddles[0].h / 4)) \
                or pygame.Rect(self.x, self.y, self.r, self.r).colliderect(
                pygame.Rect(paddles[1].x, paddles[0].y - paddles[0].h / 4, paddles[1].w + 10, paddles[1].h / 4)) \
                or pygame.Rect(self.x, self.y, self.r, self.r).colliderect(
                pygame.Rect(paddles[0].x, paddles[0].y + paddles[0].h / 4, paddles[0].w + 10, paddles[0].h / 4)) \
                or pygame.Rect(self.x, self.y, self.r, self.r).colliderect(
                pygame.Rect(paddles[1].x, paddles[0].y + paddles[0].h / 4, paddles[1].w + 10, paddles[1].h / 4)):
            self.dir_y *= 1.5

        elif self.x < 0:
            # check which user is looser and is in left side
            if paddles[0].x < main.Game.width / 2:
                paddles[1].score += 1
            else:
                paddles[0].score += 1
            return False

        elif self.x > main.Game.width:
            # check which user is looser and is in right side
            if paddles[0].x > main.Game.width / 2:
                paddles[1].score += 1
            else:
                paddles[0].score += 1
            return False

        self.y += self.dir_y * self.speed
        self.x += self.dir_x * self.speed
