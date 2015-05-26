import time
import webbrowser

total_breaks = 3
break_count = 0

print("this program started on"+time.ctime())
while(break_count < total_breaks):
    time.sleep(10)
    webbrowser.open("https://www.google.co.in/?gfe_rd=cr&ei=Nb5iVbq2MO_I8AfH4YGYBA&gws_rd=ssl")
    break_count = break_count + 1
