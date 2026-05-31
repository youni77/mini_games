#wite out inputimeout
import random
import threading

def get_answer():
    global user_answer
    try:
        user_answer = input("What will be the result? ")
    except:
        pass

while True:
    num1 = random.randint(10, 99)
    num2 = random.randint(10, 99)
    result = num1 * num2

    print(f"\n{num1} × {num2}")
    print("You have 10 seconds!")

    user_answer = None

    t = threading.Thread(target=get_answer)
    t.daemon = True
    t.start()

    t.join(10) 

    if user_answer is None:
        print(f"⏰ Time is up! Answer was {result}")

    else:
        try:
            if int(user_answer) == result:
                print(f" Correct! {num1}×{num2}={result}")
            else:
                print(f" Wrong! Correct answer: {num1}×{num2}={result}")
        except ValueError:
            print(f" Invalid input! Answer was {result}")

    play_again = input("Do you want to play again? (y/n): ")

    if play_again.lower() == "n":
        print("👋 Goodbye!")
        break