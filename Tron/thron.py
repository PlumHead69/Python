import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_DOWN, KEY_UP
import random

WIDTH = 120
HEIGHT = 30
MAX_X = WIDTH - 2
MAX_Y = HEIGHT - 2
SNAKE_LENGTH = 1

SNAKE_X = 1
SNAKE_Y = 27

SNAKEBOT_X = 110
SNAKEBOT_Y = 20

TIMEOUT = 1

global_body_list = []


class Snake(object):
    REV_DIR_MAP = {
        KEY_UP: KEY_DOWN, KEY_DOWN: KEY_UP,
        KEY_LEFT: KEY_RIGHT, KEY_RIGHT: KEY_LEFT,
    }

    def __init__(self, x, y, window):
        self.hit_score = 0
        self.timeout = TIMEOUT
        self.body_list = []

        global_body_list.append(Body(x, y))
        self.body_list.append(Body(x, y))
        self.window = window
        self.direction = KEY_RIGHT

        self.direction_map = {
            KEY_UP: self.move_up,
            KEY_DOWN: self.move_down,
            KEY_LEFT: self.move_left,
            KEY_RIGHT: self.move_right
        }

    @property
    def collided(self):
        if self.head.y < 1:
            return True

        if self.head.y > MAX_Y:
            return True

        if self.head.x < 1:
            return True

        if self.head.x > MAX_X:
            return True

        return any([body.coor == self.head.coor
                    for body in global_body_list[:-1]])

    @property
    def obstacle(self):
        if self.head.y <= 1 and self.direction == KEY_UP:
            return True

        if self.head.y >= MAX_Y and self.direction == KEY_DOWN:
            return True

        if self.head.x <= 1 and self.direction == KEY_LEFT:
            return True

        if self.head.x >= MAX_X and self.direction == KEY_RIGHT:
            return True

        return any([body.coor == self.ahead()
                    for body in global_body_list[:-1]])

    def ahead(self):
        if self.direction == KEY_RIGHT:
            ahead_coor = self.head.x+1, self.head.y
            return ahead_coor

        if self.direction == KEY_LEFT:
            ahead_coor = self.head.x-1, self.head.y
            return ahead_coor

        if self.direction == KEY_DOWN:
            ahead_coor = self.head.x, self.head.y+1
            return ahead_coor

        if self.direction == KEY_UP:
            ahead_coor = self.head.x, self.head.y-1
            return ahead_coor

    def update(self):
        global_body_list.append(Body(self.head.x, self.head.y))
        self.body_list.append(Body(self.head.x, self.head.y))
        self.direction_map[self.direction]()

    def change_direction(self, direction):
        self.direction = direction

    def render(self):
        for body in self.body_list:
            self.window.addstr(body.y, body.x, body.char)
    def set_dir(snake):
        if snake.obstacle == True:
            if snake.direction == KEY_DOWN or snake.direction == KEY_UP:
                snake.change_direction(KEY_RIGHT)

                if snake.obstacle == True:
                    snake.change_direction(KEY_LEFT)
            elif snake.direction == KEY_LEFT or snake.direction == KEY_RIGHT:
                snake.change_direction(KEY_UP)

                if snake.obstacle == True:
                    snake.change_direction(KEY_DOWN)

    @property
    def head(self):
        return self.body_list[-1]

    @property
    def coor(self):
        return self.head.x, self.head.y

    def move_up(self):
        self.head.y -= 1

    def move_down(self):
        self.head.y += 1

    def move_left(self):
        self.head.x -= 1

    def move_right(self):
        self.head.x += 1


class Body(object):
    def __init__(self, x, y, char='#'):
        self.x = x
        self.y = y
        self.char = char

    @property
    def coor(self):
        return self.x, self.y


if __name__ == '__main__':
    curses.initscr()
    curses.beep()
    curses.beep()
    window = curses.newwin(HEIGHT, WIDTH, 0, 0)
    window.timeout(TIMEOUT)
    window.keypad(1)
    curses.noecho()
    curses.curs_set(0)
    window.border(0)

    snake = Snake(SNAKE_X, SNAKE_Y, window)
    snake_bot1 = Snake(SNAKEBOT_X, SNAKEBOT_Y, window)
    #snake_bot2 = Snake(12, 4, window)
    #snake_bot3 = Snake(20, 20, window)

    while True:
        window.clear()
        window.border(0)
        snake.render()
        snake_bot1.render()
        #snake_bot2.render()
        #snake_bot3.render()

        rDirection = random.choice([KEY_UP, KEY_LEFT, KEY_DOWN, KEY_RIGHT])
        event = window.getch()

        if event == 27:
            break

        if event in [KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT]:
            snake.change_direction(event)

        if event == 32:
            key = -1
            while key != 32:
                key = window.getch()

        snake_bot1.set_dir()
        #snake_bot2.set_dir()
        #snake_bot3.set_dir()

        snake.update()
        snake_bot1.update()
        #snake_bot2.update()
        #snake_bot3.update()
        if snake.collided:
            break
        if snake_bot1.collided:
            break
        """if snake_bot2.collided:
            break
        if snake_bot3.collided:
            break"""


curses.endwin()
