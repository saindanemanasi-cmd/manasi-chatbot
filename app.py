from flask import Flask, render_template, request

app = Flask(__name__)

def chatbot_response(user_input):

    user_input = user_input.lower()

    if "hi" in user_input or "hello" in user_input:
        return "Hello! Welcome to Manasi ChatBot 🤖"

    elif "python course" in user_input:
        return "Python course fee is 11800/-"

    elif "python batch timings" in user_input:
        return "23rd Feb to 20th March - Mon to Fri - 9pm to 11pm"

    elif "java course" in user_input or "java fee" in user_input:
        return "Java course fee is 12000/-"

    elif "java class timing" in user_input or "java timing" in user_input:
        return "Java classes run from 6 PM to 8 PM - Mon to Fri."

    elif "machine learning course" in user_input or "ml course" in user_input:
        return "Machine Learning course fee is 15000/-"

    elif "machine learning timing" in user_input or "ml timing" in user_input:
        return "Machine Learning classes run from 7 PM to 9 PM - Mon to Fri."

    elif "location" in user_input or "class location" in user_input:
        return "Classes are conducted at KC Training Institute, Thane."

    elif "online" in user_input or "offline" in user_input:
        return "Classes are available in both Offline and Online modes."

    elif "bye" in user_input:
        return "Thank you for chatting! Have a great day 😊"

    else:
        return "Sorry, I didn't understand your question."

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    user_text = request.args.get("msg")
    return chatbot_response(user_text)


if __name__ == "__main__":
    app.run()