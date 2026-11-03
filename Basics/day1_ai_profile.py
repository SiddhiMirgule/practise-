print("Welcome to your AI Engineering journey ! ")
name =input("Enter your name: ")

while True:
    try:
        time =int(input("How many hours they can study each day: "))

        if 0 < time <=24:
            print("hours are validated")
            break
        else:
            print("please enter a number between 1 and 24.")
    except ValueError :
        print("Enter valid number of hours ")

topic = input("Which AI topic they want to learn first?: ")

print(f"{name} your weekly study target is {time}. Your first topic is {topic} . Keep learning consistently.")


