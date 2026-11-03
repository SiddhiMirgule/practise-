# validate external input and handle errors deliberately
age_text = input("Enter your age : ")
age = int(age_text)

try:
    if age < 0 :
        print("age cannot be negative")
    else:
        print(f"Next year your age will be {age+1}")

except ValueError :
    print("Please enter a valid number")
