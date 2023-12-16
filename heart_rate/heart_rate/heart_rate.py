
# When you physically exercise to strengthen your heart, you
# should maintain your heart rate within a range for at least 20
# minutes. To find that range, subtract your age from 220. This
# difference is your maximum heart rate per minute. Your heart
# simply will not beat faster than this maximum (220 - age).
# When exercising to strengthen your heart, you should keep your
# heart rate between 65% and 85% of your heart’s maximum rate.


age = eval(input("Enter your age: "))

heartRange = 220 - age

fastestHeartBeat = heartRange * (85/100)

slowestHeartBeat = heartRange * (65/100)

print(f"Your ideal heart beat is in between {slowestHeartBeat:.0f}bpm and {fastestHeartBeat:.0f}bpm")