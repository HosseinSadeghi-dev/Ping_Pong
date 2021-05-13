import random
import pygame
from shared.color import Color
import ball
import paddle
import time


class Game:
    width = 700
    height = 400
    border_size = 10
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Ping Pong')
    clock = pygame.time.Clock()
    fps = 60

    @staticmethod
    def play():
        pygame.mouse.set_visible(False)
        pygame.init()
        font = pygame.font.Font('assets/fonts/arial.ttf', 40)
        # set paddles
        side = random.choice(['left', 'right'])
        if side == 'left':
            user = paddle.Paddle(side, Color.blue)
            cpu = paddle.Paddle('right', Color.red)
        else:
            user = paddle.Paddle(side, Color.blue)
            cpu = paddle.Paddle('left', Color.red)
        # set ball
        bl = ball.Ball()
        while True:

            Game.screen.fill(Color.black)
            # border
            pygame.draw.rect(Game.screen, Color.white, [0, 0, Game.width, Game.height], Game.border_size)
            # halfLine
            pygame.draw.aaline(Game.screen, Color.white, (Game.width / 2, 0), (Game.width / 2, Game.height))

            for event in pygame.event.get():
                if event.type == pygame.MOUSEMOTION:
                    user.move(pygame.mouse.get_pos()[1])
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    exit()

            user.show()
            cpu.show()

            # check is ball is in goal
            if bl.move([user, cpu]) == False:
                del bl
                bl = ball.Ball()
            bl.show()
            cpu.move(None, bl)

            # user is on left side
            if user.x < Game.width / 2:
                user_score = font.render(f'{user.score}', True, Color.blue)
                you_box = user_score.get_rect(center=(Game.width / 4, 40))
                #
                cpu_score = font.render(f'{cpu.score}', True, Color.red)
                cpu_box = cpu_score.get_rect(center=(Game.width * 0.75, 40))
                # user is on right side
            else:
                user_score = font.render(f'{user.score}', True, Color.blue)
                you_box = user_score.get_rect(center=(Game.width * 0.75, 40))

                cpu_score = font.render(f'{cpu.score}', True, Color.red)
                cpu_box = cpu_score.get_rect(center=(Game.width / 4, 40))
            #
            Game.screen.blit(user_score, you_box)
            Game.screen.blit(cpu_score, cpu_box)
            pygame.display.update()
            Game.clock.tick(Game.fps)

    @staticmethod
    def intro():
        pygame.init()
        font = pygame.font.Font('assets/fonts/arial.ttf', 50)
        timer = 3

        while timer > 0:
            you = font.render('YOU', True, Color.blue)
            you_box = you.get_rect(center=(Game.width / 2, Game.height / 2 - 70))

            cpu = font.render('CPU', True, Color.red)
            cpu_box = cpu.get_rect(center=(Game.width / 2, Game.height / 2))

            txt_1 = font.render(f"Game Start In {timer}", True, (255, 255, 255))
            text_1 = txt_1.get_rect(center=(Game.width / 2, Game.height / 2 + 120))

            Game.screen.fill(Color.black)
            Game.screen.blit(you, you_box)
            Game.screen.blit(cpu, cpu_box)
            Game.screen.blit(txt_1, text_1)
            pygame.display.update()
            timer -= 1
            time.sleep(1)

        Game.play()


def main():
    Game.intro()


if __name__ == "__main__":
    main()
