import webbrowser
import time

total_breaks = 3
break_count = 0

while (break_count < total_breaks):

    print ( "This program starts on " + time.ctime())
    time.sleep(10)
    webbrowser.open("http://www.google.ca")
    break_count = break_count + 1 
