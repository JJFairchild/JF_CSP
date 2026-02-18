# JF Time of Day

import time
t=time.localtime().tm_hour
if t<6: print("WHY ARE YOU AWAKE RIGHT NOW?!")
elif t<9: print("Good morning!")
elif t<12: print("Good day to you!")
elif t<20: print("Good afternoon!")
else: print("Good night!")