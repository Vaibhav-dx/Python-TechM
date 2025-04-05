# Problem 1: Bank Loan Eligibility System
# Create a program to check if a user is eligible for a bank loan based on salary, age, and credit score using nested conditionals.

def loan_eligibility(age, salary, credit_score):
    if 21 <= age <= 60:  
        if salary >= 20000:  
            if credit_score >= 650:  
                return "Loan Approved!"
            else:
                return "Loan Denied: Low Credit Score."
        else:
            return "Loan Denied."
    else:
        return "Age not within eligible range."


age = int(input("Enter your age: "))
salary = float(input("Enter your monthly salary: "))
credit_score = int(input("Enter your credit score: "))

result = loan_eligibility(age, salary, credit_score)
print(result)

#Problem 2: AI Chatbot with Conditional Responses
# Design a simple chatbot that responds differently based on user input (e.g., greetings, questions, or farewell messages).
def chatbotresponse(userinput):
    userinput = userinput.lower()

    
    greetings = ["hello", "hi", "hey", "greetings"]
    if userinput in greetings:
        return "Hello! How can I assist you today?"

    
    farewells = ["bye", "goodbye", "see you"]
    if userinput in farewells:
        return "Goodbye! Have a great day!"

    
    if "how are you" in userinput:
        return "I'm just a bot, but I'm doing great! How about you?"
    elif "your name" in userinput:
        return "I am ChatBot, your virtual assistant!"
    elif "help" in userinput:
        return "how can I help U?"
    
    
    return "Can you ask something else?"


print("AI Chatbot: 'bye' to exit.")
while True:
    user_input = input()
    if user_input.lower() == "bye":
        print("Chatbot: Goodbye! Have a great day!")
        break
    response = chatbotresponse(user_input)
    print(f"Chatbot: {response}")

# Problem 3: Traffic Light Simulation
# Simulate a traffic light system using conditionals and loops.
import time  
def traffic_light():
    lights = [("RED", 5), ("YELLOW", 2), ("GREEN", 5)]  
    print("Traffic Light Simulation (Press Ctrl + C to stop) \n")

    while True: 
        for light, duration in lights:
            print(f"{light} - Wait for {duration} seconds")
            time.sleep(duration)  
            print("\n")  

traffic_light()  

# Problem 4: Smart Home Automation
# Implement a conditional-based smart home system where temperature, humidity, and motion sensors determine actions (e.g., turning lights and fans on/off).

def smarthome(temp,humidity,motion):
    if temp>30:
        fan="ON"
    else:
        fan="OFF"

    if humidity>70:
        dehumidifier="ON"
    else:
        dehumidifier="OFF"
    
    if motion:
        light="ON"
    else:
        light="OFF"

    print("\n Smart Home Status:")
    print(f"Temperature: {temp}°C → Fan: {fan}")
    print(f"Humidity: {humidity}% → Dehumidifier: {dehumidifier}")
    print(f"Motion: {'Detected' if motion else 'No Motion'} → Lights: {light}")
    
while True:
    temp = int(input("\nEnter Temperature (°C): "))
    humidity = int(input("Enter Humidity (%): "))
    motion = input("motion detected? (yes/no): ").strip().lower() == "yes"

    smarthome(temp, humidity, motion)

# 7. Password Strength Checker
# Classify passwords as "Weak", "Medium", or "Strong" based on length, numbers, uppercase/lowercase letters, and special characters.
# Loop until a "Strong" password is entered.
def passwordstrength(password):
    strength = 0
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    special_chars = "!@#$%^&*(),.?\":{}|<>"


    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special = True
    
    
    if len(password) >= 8:
        strength += 1
    if has_digit:
        strength += 1
    if has_upper and has_lower:
        strength += 1
    if has_special:
        strength += 1

    
    if strength == 4:
        return "Strong"
    elif strength == 3:
        return "Medium"
    else:
        return "Weak"


while True:
    password = input("Enter your password: ")
    result = passwordstrength(password)
    print(f"Password Strength: {result}")
    
    if result == "Strong":
        print("Password accepted!")
        break
    else:
        print("Try a stronger password.")

# 8. Banking System with ATM Functionality
# Simulate an ATM system for checking balance, withdrawal, and deposit.
# Use loops for multiple transactions and conditionals to prevent overdraft.

# Initial balance
balance = 1000

while True:
    print("\nWelcome to the ATM")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print(f"\nYour current balance is: {balance}")
    elif choice == "2":
        deposit = float(input("Enter deposit amount: ₹"))
        if deposit > 0:
            balance += deposit
            print(f"\n {deposit} deposited.")
        else:
            print("\nInvalid deposit amount!")
    elif choice == "3":
        withdrawal = float(input("Enter withdrawal amount: "))
        if withdrawal > balance:
            print("\n Insufficient balance!")
        else :
            balance -= withdrawal
            print(f"\n ₹{withdrawal} withdrawn. ")
        
    elif choice == "4":
        print("\n Thank you!")
        break
    else:
        print("\n Please try again.")
