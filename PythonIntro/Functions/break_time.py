import webbrowser
import time 

counter = 1

while counter <= 3:
	print ("current time is now "+time.ctime())
	time.sleep(10)
	webbrowser.open("https://www.youtube.com/watch?v=bhplCNECg9E")
	counter += 1