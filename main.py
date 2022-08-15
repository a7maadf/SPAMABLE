import pyautogui
import time
def app():
	conunt2 = 1

	print("Choose the mode")
	print("1. Normal")
	print("2. Advanced (Allows you to customize the number of times of times and the sleep timer)")
	mode = int(input("Choose the mode number: "))

	if mode == 1:
		msg = input("Enter the message: ")
		n = "100000000000000000"
		sleep = 0
	elif mode == 2:
		msg = input("Enter the message: ")
		n = input("How many times ? ")
		sleep = int(input("How much time you want between each two messages? "))
		showCountWithTheMessage = input("Do you want to show the count next to the message? (y/n): ")
		#conunt2 = int(input("Custom Count? "))
	else:
		print("Error")





	print("Countdown...")

	count = 5
	while(count != 0):
		print(str(count) + "s remaining")
		time.sleep(1)
		count -= 1

	print("Fireeeeeeeeeeeeeeeee.....................................................")

	#for i in range(0,int(n)):
		#pyautogui.typewrite(msg + '\n')
		#time.sleep(sleep)
	conunt2 = 0


	while True:
		if conunt2 != int(n):
			if showCountWithTheMessage.lower() == "y":
				pyautogui.typewrite(msg + " " + str(conunt2 + 1) + '\n')
				time.sleep(sleep)
				conunt2 = conunt2 + 1
			elif showCountWithTheMessage.lower() == "n":
				pyautogui.typewrite(msg + '\n')
				time.sleep(sleep)
				conunt2 = conunt2 + 1
		else:
			print("Done")
			print("")
			print("")
			break
            
	app()
app()