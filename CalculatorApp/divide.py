from getTwoNumbers import *

def divide():
    nums = getTwoNumbers()
    if nums[1] == 0:
        print("Cannot divide by 0.")
    else:
        return nums[0] / nums[1]