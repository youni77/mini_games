#wite inputimeout 
from inputimeout import inputimeout, TimeoutOccurred
import random

num1 = random.randint(10, 99)
num2 = random.randint(10, 99)

try:
    answer = inputimeout(
        prompt=f"{num1} × {num2} = ",
        timeout=10
    )

    if int(answer) == num1 * num2:
        print("Correct!")
    else:
        print(" Wrong!")

except TimeoutOccurred:
    print(" Time is up!")