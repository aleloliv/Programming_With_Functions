from datetime import datetime
import math

width = float(input("Enter the width of the tire in mm (ex 205): "))

ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))

diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))

pi = math.pi

volume = (pi * pow(width, 2) * ratio * (width * ratio + 2540 * diameter)) / 10000000000

print(f"The approximate volume is {volume:.2f} liters")

buy = False
choice = "no"
phone = 0
repeat = "no"

while True:
	if(width==175):
		if(ratio==65):
			if(diameter==14):
				print(f"For a tire with width of {width}mm, a ratio of {ratio} and a diameter of {diameter} inches the price is R$ 389,00")
				choice = input("Would you like to buy this tire? (Yes or No) ")
				if(choice.lower()=="yes"):
					phone = int(input("What is your phone number? "))
					break
				elif(choice.lower()=="no"):
					repeat = input(print("Ok, would you like to select another tire specifications? (Yes or No) "))
					if(repeat.lower()=="yes"):
						continue
					elif(repeat.lower()=="no"):
						break
				break
			elif(diameter==15):
				print(f"For a tire with width of {width}mm, a ratio of {ratio} and a diameter of {diameter} inches the price is R$ 290,00")
				choice = input("Would you like to buy this tire? (Yes or No) ")
				if(choice.lower()=="yes"):
					phone = int(input("What is your phone number? "))
					break
				elif(choice.lower()=="no"):
					repeat = input(print("Ok, would you like to select another tire specifications? (Yes or No) "))
					if(repeat.lower()=="yes"):
						continue
					elif(repeat.lower()=="no"):
						break
				break
			else:
				print("Please select a valid diameter (14 or 15)")
		elif(ratio==70):
			if(diameter==15):
				print(f"For a tire with width of {width}mm, a ratio of {ratio} and a diameter of {diameter} inches the price is R$ 746,20")
				choice = input("Would you like to buy this tire? (Yes or No) ")
				if(choice.lower()=="yes"):
					phone = int(input("What is your phone number? "))
					break
				elif(choice.lower()=="no"):
					repeat = input(print("Ok, would you like to select another tire specifications? (Yes or No) "))
					if(repeat.lower()=="yes"):
						continue
					elif(repeat.lower()=="no"):
						break
				break
			else:
				print("Please select a valid diameter (15)")
		else:
			print("Please select a valid ratio (65 or 70)")
	elif(width==235):
		if(ratio==35):
			if(diameter==19):
				print(f"For a tire with width of {width}mm, a ratio of {ratio} and a diameter of {diameter} inches the price is R$ 2101,00")
				choice = input("Would you like to buy this tire? (Yes or No) ")
				if(choice.lower()=="yes"):
					phone = int(input("What is your phone number? "))
					break
				elif(choice.lower()=="no"):
					repeat = input(print("Ok, would you like to select another tire specifications? (Yes or No) "))
					if(repeat.lower()=="yes"):
						continue
					elif(repeat.lower()=="no"):
						break
				break
			else:
				print("Please select a valid diameter (19)")
		else:
			print("Please select a valid ratio (35)")
	else:
		print("Please select a valid width (175 or 235)")
				

current_date_and_time = datetime.now()

with open("volumes.txt", "at") as volumes_file:
	print(f"{current_date_and_time:%Y-%m-%d}", file=volumes_file)
	print(f"{width:.0f}, {ratio:.0f}, {diameter:.0f}, {volume:.2f}", phone, file=volumes_file)