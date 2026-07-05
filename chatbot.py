from datetime import datetime
import random

print("=" * 40)
print("      RULE-BASED AI CHATBOT")
print("=" * 40)
print("Type 'help' to see available commands.")
print("Type 'exit' to quit.\n")

jokes = [
    "Why did the computer go to the doctor? Because it caught a virus!",
    "Why do programmers prefer Python? Because it's easy to read!",
    "Why was the computer cold? It forgot to close its Windows!"
]

while True:
    user = input("You: ").lower().strip()

    if user == "exit":
        print("Bot: Thank you! Have a great day.")
        break

    elif user in ["hi", "hello", "hey"]:
        print("Bot: Hello! Welcome.")

    elif user == "how are you":
        print("Bot: I am doing great. How about you?")

    elif user == "what is your name":
        print("Bot: I am a Rule-Based AI Chatbot.")

    elif user == "who created you":
        print("Bot: I was created using Python.")

    elif user == "what can you do":
        print("Bot: I can answer basic predefined questions.")

    elif user == "python":
        print("Bot: Python is a powerful and easy-to-learn programming language.")

    elif user == "ai":
        print("Bot: Artificial Intelligence enables machines to perform tasks that normally require human intelligence.")

    elif user == "time":
        print("Bot: Current Time:", datetime.now().strftime("%I:%M:%S %p"))

    elif user == "date":
        print("Bot: Today's Date:", datetime.now().strftime("%d-%m-%Y"))

    elif user == "good morning":
        print("Bot: Good Morning! Have a wonderful day!")

    elif user == "good afternoon":
        print("Bot: Good Afternoon! Hope you're having a great day!")

    elif user == "good evening":
        print("Bot: Good Evening! Hope your day went well!")

    elif user == "good night":
        print("Bot: Good Night! Sweet dreams!")

    elif user == "thank you":
        print("Bot: You're welcome! Happy to help.")

    elif user == "bye":
        print("Bot: Goodbye! Have a nice day.")

    elif user == "joke":
        print("Bot:", random.choice(jokes))

    elif user == "calculator":
        try:
            num1 = float(input("Enter first number: "))
            op = input("Enter operator (+, -, *, /): ")
            num2 = float(input("Enter second number: "))

            if op == "+":
                print("Bot: Result =", num1 + num2)
            elif op == "-":
                print("Bot: Result =", num1 - num2)
            elif op == "*":
                print("Bot: Result =", num1 * num2)
            elif op == "/":
                if num2 != 0:
                    print("Bot: Result =", num1 / num2)
                else:
                    print("Bot: Cannot divide by zero.")
            else:
                print("Bot: Invalid operator.")

        except ValueError:
            print("Bot: Please enter valid numbers.")

    elif user == "help":
        print("""
Available Commands:
- hi / hello / hey
- how are you
- what is your name
- who created you
- what can you do
- python
- ai
- date
- time
- calculator
- joke
- thank you
- good morning
- good afternoon
- good evening
- good night
- bye
- exit
""")

    else:
        print("Bot: Sorry, I don't understand that. Type 'help' to see available commands.")
