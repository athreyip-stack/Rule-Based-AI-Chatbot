# Rule-Based AI Chatbot

A simple and interactive ***Rule-Based AI Chatbot** built using **Python**. This chatbot uses predefined rules and conditional statements (`if-elif-else`) to understand user input and provide appropriate responses. It is designed as a beginner-friendly Artificial Intelligence project to demonstrate the fundamentals of conversational programming without using machine learning or external AI libraries.

---

## Project Overview

The Rule-Based AI Chatbot simulates a basic conversation with users by responding to predefined commands and questions. It continuously accepts user input until the user types **exit**. Apart from answering common questions, the chatbot also provides useful utilities such as displaying the current date and time, telling random jokes, and performing simple mathematical calculations.

This project showcases the use of:
- Conditional Statements (`if-elif-else`)
- Loops (`while`)
- User Input Handling
- Functions from Python Standard Library
- Exception Handling
- Basic Artificial Intelligence Concepts



## Features

- Greets the user
- Responds to common questions
- Introduces itself
- Displays the current time
- Displays today's date
- Performs basic calculations
- Tells random jokes
- Responds to greetings like Good Morning, Good Afternoon, Good Evening, and Good Night
- Replies to Thank You messages
- Displays available commands using the Help menu
- Runs continuously until the user types **exit**
- Handles unknown inputs gracefully



## Technologies Used

- Python 3
- datetime module
- random module

---

## Project Structure

```
Rule-Based-AI-Chatbot/
│
├── chatbot.py
├── README.md


### Navigate to the project folder

```bash
cd Rule-Based-AI-Chatbot
```

### Run the chatbot

```bash
python chatbot.py
```


## Example Output


========================================
        RULE-BASED AI CHATBOT
========================================

Type 'help' to see available commands.
Type 'exit' to quit.

You: hi
Bot: Hello! Welcome.

You: what is your name
Bot: I am a Rule-Based AI Chatbot.

You: time
Bot: Current Time: 10:45:23 AM

You: joke
Bot: Why do programmers prefer Python? Because it's easy to read!

You: calculator
Enter first number: 20
Enter operator (+,-,*,/): *
Enter second number: 5
Bot: Result = 100

You: exit
Bot: Thank you! Have a great day.
```

---

## Available Commands

- hi
- hello
- hey
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
- help
- exit

---

## How It Works

1. The chatbot starts with a welcome message.
2. It continuously waits for user input.
3. User input is converted to lowercase for easy comparison.
4. The chatbot checks the input using `if-elif-else` statements.
5. If a predefined command is matched, an appropriate response is displayed.
6. If the command is unknown, the chatbot displays a default message.
7. The conversation continues until the user enters **exit**.

---

## Concepts Demonstrated

- Artificial Intelligence (Rule-Based System)
- Conditional Statements
- Infinite Loops
- User Interaction
- Exception Handling
- Python Modules
- Random Response Generation

---

## Future Improvements

- Add voice input and speech output
- Create a graphical user interface (GUI)
- Integrate Natural Language Processing (NLP)
- Connect with APIs for live weather and news
- Store chat history
- Add user authentication
- Expand the chatbot knowledge base

---

## Learning Outcomes

By completing this project, you will understand:

- Building a rule-based chatbot
- Python programming fundamentals
- Decision-making using conditional statements
- Working with loops
- Handling user input
- Using Python's built-in libraries
- Creating interactive console applications

---


⭐ If you found this project helpful, consider giving it a **Star** on GitHub!# Rule-Based-AI-Chatbot
A Python-based rule-based AI chatbot that responds to predefined user inputs, featuring greetings, date &amp; time, calculator, jokes, and interactive conversations.
