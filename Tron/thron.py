import curses as c
from curses import KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT
import time
screen = c.initscr()
c.noecho()
c.cbreak()


def snakeWin(snakeName):
    
    screen.keypad(True)
    screen.addstr(0,0, snakeName)
    screen.refresh()
    time.sleep(10)
    c.endwin()


def main():

    c.initscr()
    win = c.newwin(30, 120, 0, 0)
    win.keypad(1)
    c.noecho()
    c.curs_set(0)
    win.border(0)
    win.nodelay(1)

    key = KEY_RIGHT  # Initializing values
    key2 = ord("d")
    snake = [[4, 10], [4, 9], [4, 8]]  # Initial snake co-ordinates
    snake2 = [[24, 10], [24, 9], [24, 8]] 

    

    while key != 27:  # While Esc key is not pressed
        win.border(0)
        win.addstr(0, 27, ' TRON ')  # 'SNAKE' strings
        win.timeout(
            10
        )  # Increases the speed of Snake as its length increases for speed

        prevKey = key  # Previous key pressed
        event = win.getch()
        key = key if event == -1 else event

        if key not in [KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN,
                       27]:  # If an invalid key is pressed
            key = prevKey


        prevKey2 = key2  # Previous key pressed
        key2 = key2 if event == -1 else event


        if key2 not in [ord("a"),ord("d"),ord("w"),ord("s"),
                       27]:  # If an invalid key is pressed
            key2 = prevKey2



        # Calculates the new coordinates of the head of the snake.
        # NOTE: len(snake) increases.

        snake.insert(0, [
            snake[0][0] + (key == KEY_DOWN and 1) + (key == KEY_UP and -1),
            snake[0][1] + (key == KEY_LEFT and -1) + (key == KEY_RIGHT and 1)
        ])

        snake2.insert(0, [
            snake2[0][0] + (key2 == ord("s") and 1) + (key2 ==ord("w") and -1),
            snake2[0][1] + (key2 == ord("a") and -1) + (key2 == ord("d") and 1)
        ])


        # If snake crosses the boundaries, make it enter from the other side
        if snake[0][0] == 0:
            screen.keypad(True)
            screen.addstr(0,0, snake2)
            screen.refresh()
            time.sleep(10)
    
        if snake[0][1] == 0:
            snakeWin(snake2)
        if snake[0][0] == 29:
            snakeWin(snake2)
        if snake[0][1] == 119:
            snakeWin(snake2)
        if snake[0] in snake[1:]:
            snakeWin(snake2)
        #snake2 dieing
        if snake2[0][0] == 0:
            snakeWin(snake)
        if snake2[0][1] == 0:
            snakeWin(snake)
        if snake2[0][0] == 29:
            snakeWin(snake)
        if snake2[0][1] == 119:
            snakeWin(snake)
        if snake2[0] in snake2[1:]:
            snakeWin(snake)
        
        #snake collision
        if snake2[0] in snake[1:]:
            snakeWin(snake)
        if snake[0] in snake2[1:]:
            snakeWin(snake2)

        win.addch(snake[0][0], snake[0][1], 'X')
        win.addch(snake2[0][0], snake2[0][1], 'O')

    c.endwin()


if __name__ == '__main__':
    main()
