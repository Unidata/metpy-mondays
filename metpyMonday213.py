# - Metpy Monday
# - 213 - Manipulating the Screen Cursor
# - https://www.youtube.com/watch?v=Nwe_28WV6Xw

# - Original code in: https://gist.github.com/jrleeman/3259cf7a2218af9d1d79634cfee22e4e


import time
from console.screen import sc
from math import floor
from console import fg, bg, fx
import random
from datetime import datetime

colors = [fg.green, fg.yellow, fg.blue, fg.red, fg.default,
          fg.royalblue, fg.lightslateblue, fg.steelblue,
          fg.magenta, fg.violet, fg.mediumpurple,
          fg.bisque1, fg.peachpuff1, fg.springgreen1,
          fg.chartreuse1, fg.sienna1, fg.salmon1]

target_time = datetime(2023, 1, 1, 1, 38)

while(1):
    # Check if we are in the minute before!
    seconds_till = (target_time - datetime.utcnow()).seconds

    if seconds_till > 60:
        i = 0
    else:
        i = 60 - seconds_till
    if datetime.utcnow() > target_time:
        i = 60

    with sc.location(3, 0):
        for j in range(3 + floor(i/2)):
            print('              ***              ')
        print(random.choice(colors), "         , - ~ ~ ~ - ,         ")
        print("     , '               ' ,     ")
        print("   ,                       ,   ")
        print("  ,                         ,  ")
        print(" ,                           , ")
        if datetime.utcnow() >= target_time:
            print(" ,          UNIDATA          , ")
        else:
            print(" ,                           , ")
        print(" ,                           , ")
        print("  ,                         ,  ")
        print("   ,                       ,   ")
        print("     ,                  , '    ")
        print("       ' - , _ _ _ ,  '        ", fg.default)
        for j in range(31 - floor(i/2)):
            print('              ***              ')
        time.sleep(.2)
        print(datetime.strftime(datetime.utcnow(), '     %m-%d-%Y %H:%M:%S'))
