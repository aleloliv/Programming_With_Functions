import math

manufactured = int(input("Enter the number of items: "))
packed = int(input("Enter the number of items per box: "))

calc = manufactured / packed

print(f"For {manufactured} items, packing {packed} items in each box, you will need {math.ceil(calc)} boxes.")
