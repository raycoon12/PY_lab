import curses


def main(stdscr):
    stdscr.erase()
    stdscr.key()


if __name__ == "__main__":
    curses.wrapper(main)