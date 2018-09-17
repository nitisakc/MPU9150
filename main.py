from mpu9150 import mpu9150
from threading import Thread
import time
import curses
import smbus
import math
 

def draw_menu(stdscr):
    k = 0
    cursor_x = 0
    cursor_y = 0

    stdscr.clear()
    stdscr.refresh()

    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

    while (k != ord('q')):
        stdscr.clear()
        height, width = stdscr.getmaxyx()

        sensor.get_all_data()

        stdscr.addstr( 0, 0, "Gyroskop")
        stdscr.addstr( 1, 0, "--------")
        stdscr.addstr( 2, 0, "x: "+ str("%.3f" % sensor.gyro['x']))
        stdscr.addstr( 3, 0, "y: "+ str("%.3f" % sensor.gyro['y']))
        stdscr.addstr( 4, 0, "z: "+ str("%.3f" % sensor.gyro['z'])) 
        
        stdscr.addstr( 6, 0, "Accel")
        stdscr.addstr( 7, 0, "--------")
        stdscr.addstr( 8, 0, "x: "+ str("%.3f" % sensor.accel['x']))
        stdscr.addstr( 9, 0, "y: "+ str("%.3f" % sensor.accel['y']))
        stdscr.addstr(10, 0, "z: "+ str("%.3f" % sensor.accel['z']))


        stdscr.addstr(12, 0, "Magnetometer")
        stdscr.addstr(13, 0, "--------")
        stdscr.addstr(14, 0, "x: "+ str("%.1f" % sensor.magn['x']))
        stdscr.addstr(15, 0, "y: "+ str("%.1f" % sensor.magn['y']))
        stdscr.addstr(16, 0, "z: "+ str("%.1f" % sensor.magn['z']))


        stdscr.addstr(18, 0, "Other")
        stdscr.addstr(19, 0, "--------")
        stdscr.addstr(20, 0, "Temp: " +  str("%.2f" % sensor.temp))
        

        time.sleep(0.25)

        stdscr.refresh()

def main():
    curses.wrapper(draw_menu)

if __name__ == "__main__":
    sensor = mpu9150(0x68)
    main()
